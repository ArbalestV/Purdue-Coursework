#include "ne.h"
#include "router.h"
#include <time.h> //to calculate the time functions for checking convergence and failure
//#include "endian.c"
extern struct route_entry routingTable[MAX_ROUTERS];

struct router_neighbors { //structure to keep a record of what neighbors are connected to the router
  int nbr_id; //to store the id of the neighbor
  int nbr_cost; //the cost to the neighbor
  int is_active; //to check whether or not the neighbor is active
  time_t last_update; //when was the last update received by the neighboring node
};

int total_neighbors; //global variable to store the total number of neighbors at any time
int open_listenfd_udp(int);
void NeighborInitialize(struct pkt_INIT_RESPONSE *, struct router_neighbors *);
void writeConvergence(FILE*, time_t);
void checkIfNeighborsDied(struct router_neighbors *);

int main(int argc, char **argv)
{
  //check for incorrect number of arguments
   if (argc != 5) 
     {
       exit(1);
     }
  int listenfd_udp, port_udp;
  port_udp = atoi(argv[4]); //the client udp port
  listenfd_udp = open_listenfd_udp(port_udp);
  
  int router_id; //this will be the router id, and will be used in a variety of ways
  router_id = atoi(argv[1]);
  
  struct sockaddr_in serveraddr;
  socklen_t servlen = sizeof(serveraddr);
  bzero((char *) &serveraddr, sizeof(serveraddr)); 
  inet_aton(argv[2],&serveraddr.sin_addr); //to specify the address from the command line
  serveraddr.sin_family = AF_INET;  
  serveraddr.sin_port = htons((unsigned short)atoi(argv[3]));  

  struct pkt_INIT_REQUEST req;  
  req.router_id = htonl(router_id); //since we are sending it over the network, so convert from host to network order
  if ((sendto(listenfd_udp, &req, sizeof(struct pkt_INIT_REQUEST), 0, (struct sockaddr *)&serveraddr, (socklen_t)servlen)) < 0) 
    {
      perror("Failed to send.!!");
      return -1;
    }

  //printf("1\n");
  //now send it back to the client
  struct pkt_INIT_RESPONSE resp;
  if (recvfrom(listenfd_udp, &resp, sizeof(struct pkt_INIT_RESPONSE), 0, (struct sockaddr *)&serveraddr, &servlen) == -1) 
    {
      perror("Failed to receive.!!");
      return -1;
    }
  //printf("2\n");
  //printf("%c\n", &resp);

  //now convert the response packet to host order from network order and initialize the routing tables for the node
  ntoh_pkt_INIT_RESPONSE (&resp);
  //at the initial routing bootstrap, print the contents to the log file
  char * logFileName = malloc(sizeof(char) * 11);//routerx.log, where x = 0-9
  strcpy(logFileName, "router");
  strcat(logFileName, argv[1]);
  strcat(logFileName, ".log"); //get the correct name of the log file corresponding to this router
  FILE * fp = fopen(logFileName, "w"); //open the file using the file pointer
  //now that the initial packet information has been received, it is time to update the neighboring routers 
  //before updating the neighboring routers info, let us initialize this router's routing table
  InitRoutingTbl(&resp, router_id); //call using the response packet and the router id
  time_t initial_time;
  initial_time = time(NULL); //the first time that 
  time_t last_time_changed; //to check then the last time the routing table had changed. When the router is initialized for the first time with bootstrap information, initialize with the time it takes to initialize
  last_time_changed = time(NULL);
  PrintRoutes(fp, router_id); //call the print function to print the initial bootstrap info to the log file
  struct router_neighbors neighbors[MAX_ROUTERS]; //array of neighbors with information for each
  int neighbor_active; //to check if an earlier neighbor is active or not
  NeighborInitialize(&resp, neighbors); //initialize the neighboring nodes with information on initial response

  //now the initialization is over, it is time to check for receiving updates and sending updates at time_outs using the select line
  int maxfd; //the maximum file descriptor for the select line
  fd_set rfds;
  struct timeval tv; //to store the timer time-out value
  
  int has_converged; //to check if a convergence has occured
  has_converged = 0; //initialize to 0

  time_t check_if_update_time; //to check with the current time for sending updates to other neighbors
  check_if_update_time = initial_time; //initialize to the time when router initializes
  //printf("\nfinished bootstrapping.\n");
  
  while (1) //basically go in an infinite loop 
    {
      tv.tv_sec = UPDATE_INTERVAL;//the router sends out an update to its neighbors every 1 sec
      tv.tv_usec = 0; //wait upto UPDATE_INTERVAL seconds
      FD_ZERO(&rfds);
      FD_SET(listenfd_udp, &rfds);
      maxfd = listenfd_udp + 1;
      /*int retval = */
      select(maxfd, &rfds, NULL, NULL, &tv);
      
      //now check if a UDP packet has been received, if yes then update routing table. If not, then check for dead neighbor or convergence, and send update packet to the ne
      if (FD_ISSET(listenfd_udp, &rfds))//if receiving an update packet
	{
	  //printf("\nbeginning of receviving an incoming packet..\n");
	  neighbor_active = 0; //basically every time an update is received we don't know if the neighbor was dead earlier
	  struct pkt_RT_UPDATE updatePkt;
	  recvfrom(listenfd_udp, &updatePkt, sizeof(struct pkt_RT_UPDATE), 0, (struct sockaddr *)&serveraddr, &servlen); //receive the update packet from the ne for one of the neighbors of the router
	  ntoh_pkt_RT_UPDATE (&updatePkt); //convert from network to host order
          //printf("Received RT_UPDATE from R%u containing %u routes\n", updatePkt.sender_id, updatePkt.no_routes);
	  //printf("\nreceived the update packet from neighbor.\n");
	  int dead_neighbor_live_again;
	  int i, j, k;
          for (j = 0; j < updatePkt.no_routes; j++) {
              if (updatePkt.route[j].dest_id == 0)
                  break; 
          }
	  for (i = 0; i < total_neighbors; i++)
	    {
	      if (neighbors[i].nbr_id == updatePkt.sender_id)
		{
		  dead_neighbor_live_again = i; //potentially useful when is_active == 0 for a dead router coming alive by sending an update packet
		}
	      if ((neighbors[i].is_active == 1) && (neighbors[i].nbr_id == updatePkt.sender_id))//only if the neighbor's id matches and it is active that we know that we will probably have to update the routes
		{	  
		  //printf("\npotentially changed.");
		  neighbor_active = 1; //the neighbor has been marked 
		  neighbors[i].last_update = time(NULL); //update the last update time whenever it is received
		  //now call the UpdateRoutes() function on the router for this particular neighbor node
		  int changed; //to check whether the routing table has been changed, which would dictate whether or not the log file needs to be written to
                  if (router_id == 0) {
                      for (k = 0; k < MAX_ROUTERS; k++) {
                          if (routingTable[k].dest_id == 1) {
                              printf("prev\nR0->R1: %d\n", routingTable[k].cost);
                              break;
                          }
                      }
                  }
		  changed = UpdateRoutes(&updatePkt, neighbors[i].nbr_cost, router_id); //call the update routes function to check if the routing table has changed or not
                  if (router_id == 0) {
                      for (k = 0; k < MAX_ROUTERS; k++) {
                          if (routingTable[k].dest_id == 1) {
                              printf("after\nR0->R1: %d\n", routingTable[k].cost);
                              break;
                          }
                      }
                  }
                  /*if (router_id == 3 && updatePkt.sender_id == 2) {
		    //printf("Cost R%u->R%u: %d => UpdateRoutes()\nChanged: %d\n", updatePkt.sender_id, updatePkt.route[j].dest_id, updatePkt.route[j].cost, changed);
                      for (k = 0; k < MAX_ROUTERS; k++) {
                          if (routingTable[k].dest_id == 0) {
                              printf("Cost in RoutingTable R%u->R%u: %d\n", router_id, routingTable[k].dest_id, routingTable[k].cost);
                              break;
                          }
                      }
                  }*/
		  //printf("\nChanged? %d\n", changed);
		  
		  if (changed == 1) //if changed then print the new routing table to a log file
		    {
		      //printf("\nWill print the new routing table only now.\n");
		      PrintRoutes(fp, router_id); //call the print function to print the new routing table to the log file 
		      has_converged = 0; //obviously with the new update it may not have converged
		      last_time_changed = time(NULL); //check the last time that a change had occured in the routing table. This will be used to check for the convergence checking.
		      changed = 0;
		    } //end of if (changed == 1)
		  //break; //break away from the for loop
		} //end of if ((neighbors[i].is_active == 1) && (neighbors[i].nbr_id == updatePkt.sender_id))
	    } //end of for

	  //now this will only occur when a previously dead neighbor is live again and is sending an update
	  if (neighbor_active == 0)
	    {

	      int changed; //to check whether the routing table has been changed, which would dictate whether or not the log file needs to be written to      
	      changed = UpdateRoutes(&updatePkt, neighbors[dead_neighbor_live_again].nbr_cost, router_id); //call the update routes function to check if the routing table has changed or not
	      //printf("\nChanged? %d\n", changed);
	      
	      if (changed == 1) //if changed then print the new routing table to a log file
		{
		  //printf("\nWill print the new routing table only now.\n");
		  printf("\nUpdate received from : %d\n", updatePkt.sender_id);
		  PrintRoutes(fp, router_id); //call the print function to print the new routing table to the log file 
		  has_converged = 0; //obviously with the new update it may not have converged
		  last_time_changed = time(NULL); //check the last time that a change had occured in the routing table. This will be used to check for the convergence checking.
		  changed = 0;
		} //end of if (changed == 1)


	      //use the dead_neighbor_live_again found in the previous loop
	      neighbors[dead_neighbor_live_again].is_active = 1; //now that it is live again, mark as active
	      neighbors[dead_neighbor_live_again].last_update = time(NULL); //update the last update time

	      //neighbors[dead_neighbor_live_again].nbr_cost = 
	    } //end of if (neighbor_active == 0)
	  //printf("\nbefore the end of the block.\n");
	} //end of if (FD_ISSET(listenfd_udp, &rfds))


      //else //the timer has gone off now
	//{
      //we will also be checking for dead routers using (FAILURE_DETECTION == 3 * timeout)
      //at this stage, we will be sending the update update to other neighbors of the router
      //we will also be checking for convergence using (CONVERGE == 5 * timeout)
      
      //check if a neighbor has died
      int k/*, tmp*/;
      /*
      if (router_id == 0) {
          for (k = 0; k < MAX_ROUTERS; k++) {
              if (routingTable[k].dest_id == 1) {
                  tmp = routingTable[k].cost;
                  break;
              }
          }
      }
      */
      int tmp[MAX_ROUTERS];
      for (k = 0; k < MAX_ROUTERS; k++)
	{
	  tmp[k] = routingTable[k].cost;
	}
      
         
      checkIfNeighborsDied(neighbors); //check one by one if any neighboring router has died. If yes, we will mark each as being inactive and uninstall their routes accordingly
      /*
      if (router_id == 0) {
          for (k = 0; k < MAX_ROUTERS; k++) {
              if (routingTable[k].dest_id == 1) {
                  if (tmp != routingTable[k].cost)
                      PrintRoutes(fp, router_id);
                  printf("end-1\nR2->R1: %d\n", routingTable[k].cost);
                  break;
              }
          }
      }
      */
      for (k = 0; k < MAX_ROUTERS; k++)
	{
	  if (routingTable[k].cost != tmp[k])
	    {
	      PrintRoutes(fp, router_id);
	      last_time_changed = time(NULL);
	      has_converged = 0;
	      break;
	    }
	}

      //now send updates to all of the other neighboring routers
      if ( (int) (difftime(time(NULL), check_if_update_time)) >= UPDATE_INTERVAL) //send an update to other nodes
	{
	  //printf("\nabout to send updates..\n");
	  struct pkt_RT_UPDATE updatePkt_send;
	  ConvertTabletoPkt(&updatePkt_send, router_id); //convert the router's routing table to an update packet
	  check_if_update_time = time(NULL); //for the next round of updates
	  int j;
	  //printf("\nthe total no. of my neighbors: %d\n", total_neighbors);
	  for (j = 0; j < total_neighbors; j++) //send an update packet to every active neighboring router
	    {
	      if (neighbors[j].is_active == 1)
		{
		  //printf("\nsending update to %d\n", neighbors[j].nbr_id);
		  updatePkt_send.dest_id = neighbors[j].nbr_id; //destination is each neighbor
		  //printf("\nDestination id of the update packet and sender id    %d     %d\n", updatePkt_send.dest_id, updatePkt_send.sender_id);
		  hton_pkt_RT_UPDATE(&updatePkt_send); //convert from host to network order
		  //printf("\n2\n");
		  sendto(listenfd_udp, &updatePkt_send, sizeof(struct pkt_RT_UPDATE), 0, (struct sockaddr *)&serveraddr, (socklen_t)servlen); //send the update packet, one to each neighbor that is active
		  //printf("\nend of the if for %d\n", neighbors[j].nbr_id);
		  ntoh_pkt_RT_UPDATE(&updatePkt_send); //convert it back to host order for subsequent iterations
		}
	    }
	  //check_if_update_time = time(NULL); //for the next round of updates
	  //printf("\nthe next check_if_update_time %d\n", (int) check_if_update_time);
	}
      //printf("\nmade out of receive updates, now going to checking for convergence.");

      //checking for convergence
      int checking_convergence;
      checking_convergence = (int) (difftime(time(NULL), last_time_changed)); //get the difference in times since the last time the router was changed. Convert from double to int
      //printf("\nhas_converged value: %d\n", has_converged);
      //printf("\nThe checking convergence value: %d\n", checking_convergence);
      if ( (checking_convergence > CONVERGE_TIMEOUT) && (has_converged == 0)) //check if the converge time out has ended and it has not yet converged
	{
	  has_converged = 1; //so that it does not keep printing the convergence
	  writeConvergence(fp, initial_time); //write to the file when the convergence happened
	} //end of if (checking_convergence > CONVERGE_TIMEOUT)
	  //} //end of else condition ie the timer has gone off, thereby sending update to all its neighbors and check for convergence and unresponsive neighbors
      if (router_id == 0) {
          for (k = 0; k < MAX_ROUTERS; k++) {
              if (routingTable[k].dest_id == 1) {
                  printf("end\nR0->R1: %d\n", routingTable[k].cost);
                  break;
              }
          }
      }
   
    } //end of while (1)
  return 0;
}

void checkIfNeighborsDied(struct router_neighbors * neighbors) //to check for neighbors' death and update accordingly
{
  time_t limit_time;
  limit_time = time(NULL);
  int i;
  for (i = 0; i < total_neighbors; i++)
    {
      if ( ((int) (difftime(limit_time, neighbors[i].last_update)) > FAILURE_DETECTION) && (neighbors[i].is_active == 1)) //no updates received from an active router for more than FAILURE_DETECTION seconds, that means it is dead
	{
	  printf("\nneighbor %d has died.\n", neighbors[i].nbr_id);
	  //neighbors[i].nbr_cost = INFINITY;
	  neighbors[i].is_active = 0; //mark as being inactive
	  UninstallRoutesOnNbrDeath(neighbors[i].nbr_id); //uninstall the router
	}
    }
}

void writeConvergence(FILE* fp, time_t initial_time) //whenever there is a convergence write to the log file
{
  int time_since_initialization; //to store the time since the router was initialized
  time_since_initialization = (int) (difftime(time(NULL), initial_time)); //get the difference in times since the beginning of initialization. Convert from double to int
  //printf("%d:Converged\n", time_since_initialization);
  fprintf(fp, "%d:Converged\n", time_since_initialization); //write the converged with the seconds since initialization
  fflush(fp); //to to flush the changes into the file buffer in case of an abrupt end to the program 
}

void NeighborInitialize(struct pkt_INIT_RESPONSE *InitResponse, struct router_neighbors *neighbors) //function to initialize the neighbors with information on receiving an init response
{
  int i;
  total_neighbors = InitResponse->no_nbr; //get the total number of neighbors
  //printf("\nno. of neighboring nodes: %d", total_neighbors);
  for (i = 0; i < InitResponse->no_nbr; i++) //iterate in a loop for all the neighbors identified by the ne's initial response packet
    {
      neighbors[i].nbr_id = InitResponse->nbrcost[i].nbr; //get the neighbor id
      //printf("\nneighbor id: %d", neighbors[i].nbr_id);
      neighbors[i].nbr_cost = InitResponse->nbrcost[i].cost; //get the neighbor cost
      //printf("\nneighbor cost: %d", neighbors[i].nbr_cost);
      neighbors[i].is_active = 1; //active since ne initial response has them
      neighbors[i].last_update = time(NULL); //get the current time, store this as the last update received. This will obviously be changed upon receiving updates specifically from the neighbors.
    }
}

int open_listenfd_udp(int port_udp)
{
  int listenfd, optval = 1; 
  struct sockaddr_in serveraddr; 
  
  /* Create a socket descriptor */ 
  if ((listenfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
    perror("Cannot create UDP socket.!");
    return -1;
  }
  /* Eliminates "Address already in use" error from bind. */ 
  if (setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR,(const void *)&optval , sizeof(int)) < 0) { 
    return -1; 
  }
  /* Listenfd will be an endpoint for all requests to port on any IP address for this host */ 
  bzero((char *) &serveraddr, sizeof(serveraddr)); 
  serveraddr.sin_family = AF_INET;  
  serveraddr.sin_addr.s_addr = htonl(INADDR_ANY);  
  serveraddr.sin_port = htons((unsigned short)port_udp);  
  
  if (bind(listenfd, (struct sockaddr *)&serveraddr, sizeof(serveraddr)) < 0) {
    perror("Bind failed.!");
    return -1; 
  }
  return listenfd;
}




