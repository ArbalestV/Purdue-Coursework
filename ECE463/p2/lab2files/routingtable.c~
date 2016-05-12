#include "ne.h"
#include "router.h"

struct route_entry routingTable[MAX_ROUTERS]; //the routing table
int numRoutes = 0; //number of routes in the routing table, including the self-loop

void InitRoutingTbl (struct pkt_INIT_RESPONSE *InitResponse, int myID) //initialize the routing table
{
  int tot_nbr = InitResponse->no_nbr; //get the total number of neighbors
  //first make a route to itself
  routingTable[0].dest_id = myID;
  routingTable[0].next_hop = myID;
  routingTable[0].cost = 0;
  numRoutes++;
  
  //now build the initial routing table based on neighbor information
  int i;
  for (i = 0; i < tot_nbr; i++)
    {
      routingTable[i + 1].dest_id = InitResponse->nbrcost[i].nbr; //get the neighbor id
      routingTable[i + 1].cost = InitResponse->nbrcost[i].cost; //get the cost to the neighbor
      routingTable[i + 1].next_hop = InitResponse->nbrcost[i].nbr; //the next hop will be the neighbor itself when the routing table is initialized
      numRoutes++; //increment the number of routes in the routing table
    } //the initial routing table is now built
  return;
} //end of InitRoutingTbl routine

int UpdateRoutes(struct pkt_RT_UPDATE *RecvdUpdatePacket, int costToNbr, int myID) //this will be the routine wherein the forced update and split update rules will be applied whenever any update is received from a neighbor of the node
{
  int changed; //the return value depending on updation being made or not
  changed = 0;
  
  //brute force checking technique for each neighbor
  int i;
  if (myID == 0) {
      printf("PREV\ncostToNbr: %d\n", costToNbr);
      for (i = 0; i < numRoutes; i++) {
          if (routingTable[i].dest_id == 1) {
              printf("R2->R1: %d\n", routingTable[i].cost);
          }
      }
  }
  //printf("Number of routes in the received update packet: %d\n", RecvdUpdatePacket->no_routes);
  for (i = 0; i < RecvdUpdatePacket->no_routes; i++) //for each node in neighbor of the node sending the update message
    {
      int j;
      int found;
      found = 0;
      int probable_new_distance;
      probable_new_distance = costToNbr + RecvdUpdatePacket->route[i].cost; //cost from xtoz + cost from ztoy = cost from xtoy via z
      for (j = 0; j < numRoutes; j++) //cross-reference with the routing table of the current node
	{	  
	  if (RecvdUpdatePacket->route[i].dest_id == routingTable[j].dest_id) //only if the destinations are equal
	    {
	      found = 1;
	      //printf("\nPrinting the probable new distance :%d\n", probable_new_distance);
	      //printf("\nmy ID value : %d\n", myID);
	      //now implement forced update and split horizon
	      if ( (routingTable[j].next_hop == RecvdUpdatePacket->sender_id) ||
		   ( (probable_new_distance < routingTable[j].cost) && 
		     (myID != RecvdUpdatePacket->route[i].next_hop) )
		   ) //forced update or split-horizon rule
		{
		  //now update the cost and the next hop values
		  //printf("Inside the update..\n");
		  int previous_cost; //to check for the forced update rule
		  previous_cost = routingTable[j].cost;
		  //routingTable[j].cost = probable_new_distance; 
		  if (probable_new_distance >= INFINITY) 
		    {
		      routingTable[j].cost = INFINITY;
		    }
		  else
		    {
		      routingTable[j].cost = probable_new_distance;
		    }
		  if (routingTable[j].cost != previous_cost)//technically be changed only when the previous cost is not coincidentally equal
		    {
		      //printf("\nInside changed = 1\n");
		      changed = 1;
		    }
		  /*else
		    {
		      changed = 0;
		    }*/
		  routingTable[j].next_hop = RecvdUpdatePacket->sender_id;
		  //changed = 1; //since there was an updation
		  //printf("Changed due to forced update/split horizon.\n");
		} //end of forced update and split horizon rule
	      break; //go to the next router table
	    } //end of outer if within the inner for 
	} //end of inner for
      if (found == 0) //that means the path didn't exist
	{
	  //make a new table in the routing table with the next hop as the sender
	  //printf("\nnow adding a new route to the routing table.\n");
	  routingTable[numRoutes].dest_id = RecvdUpdatePacket->route[i].dest_id;
	  routingTable[numRoutes].cost = probable_new_distance; 
	  routingTable[numRoutes].next_hop = RecvdUpdatePacket->sender_id;
	  /*
	  ///////////////////////////////////////////////////////////////////////////////
	  printf("\nWill be checking what happens when a new node is added to the routing table.\n");
	  printf("The two Costs: %d %d\n", routingTable[numRoutes].cost, probable_new_distance);
	  printf("The two dest_ids: %d %d\n", routingTable[numRoutes].dest_id, RecvdUpdatePacket->route[i].dest_id);
	  printf("The two next_hops: %d %d\n", routingTable[numRoutes].next_hop, RecvdUpdatePacket->route[i].next_hop);
	  ///////////////////////////////////////////////////////////////////////////////
	  */
	  numRoutes++; //increase the number of routes
	  changed = 1; //since there was an updation
	}
    } //end of outer for
  //printf("Total number of nodes now: %d\n", numRoutes);
  if (myID == 0) {
      printf("AFTER\ncostToNbr: %d\n", costToNbr);
      for (i = 0; i < numRoutes; i++) {
          if (routingTable[i].dest_id == 1) {
              printf("R2->R1: %d\n", routingTable[i].cost);
          }
      }
  }
  return changed; //return whether or not an update occured
} //end of UpdateRoutes routine

void ConvertTabletoPkt(struct pkt_RT_UPDATE *UpdatePacketToSend, int myID) //the routine to convert the routing table into empty rt_update packet
{
  //the sender id and the number of routes
  //printf("\nInside convert table to pkt function.\n");
  UpdatePacketToSend->sender_id = myID;
  //printf("\nSender packet sender id: %d\n", UpdatePacketToSend->sender_id);
  UpdatePacketToSend->no_routes = numRoutes;
  //printf("Number of routes in the update packet: %d\n", UpdatePacketToSend->no_routes = numRoutes); 
  //UpdatePacketToSend->route = routingTable; //the routing table is assigned
  int i;
  for (i = 0; i < numRoutes; i++) //for each router in the routing table 
    {
      UpdatePacketToSend->route[i].dest_id = routingTable[i].dest_id;
      //printf("Dest id added to the update packet: %d\n", routingTable[i].dest_id);
      //printf("Dest id added to the update packet: %d\n", UpdatePacketToSend->route[i].dest_id);
      UpdatePacketToSend->route[i].next_hop = routingTable[i].next_hop;
      UpdatePacketToSend->route[i].cost = routingTable[i].cost;
    }
  //printf("Total number of nodes now in convert table to packet: %d\n", numRoutes);
  //printf("Number of routes in the packet: %d\n", UpdatePacketToSend->no_routes);
  return;
} //end of ConvertTabletoPkt routine

void PrintRoutes (FILE* Logfile, int myID) //the function to print routes to a file
{
  printf("Printing...\n");
  fprintf(Logfile, "Routing Table:\n");//the first line
  int i;
  for (i = 0; i < numRoutes; i++) //for each route in the routing table, print the link and the cost
    {
      if (routingTable[i].dest_id == 0)
          printf("cost: %d\n", routingTable[i].cost);
      fprintf(Logfile, "R%d -> R%d: R%d, %d\n", myID, routingTable[i].dest_id, routingTable[i].next_hop, routingTable[i].cost);
    }
  fflush(Logfile); //to flush the changes into the file buffer in case of an abrupt end to the program
  return;
} //end of PrintRoutes routine

void UninstallRoutesOnNbrDeath(int DeadNbr) //to change the cost of a dead neighbor to infinity when that neighbor is found to be dead
{
  int i;
  for (i = 0; i < numRoutes; i++) {
      printf("id: %d\n", routingTable[i].dest_id);
      if (routingTable[i].dest_id == DeadNbr) {
          printf("Cost to R%u: %d\n", DeadNbr, routingTable[i].cost);
          routingTable[i].cost = INFINITY;
          printf("Cost to R%u: %d\n", DeadNbr, routingTable[i].cost);
      break;
      }
  }
  printf("\nDead node: %d\n", DeadNbr);
  printf("Cost to R%u: %d\n", DeadNbr, routingTable[i].cost);
  for (i = 0; i < numRoutes; i++) //check for each neighbor if they use the dead neighbor as the next hop
    {
      if (routingTable[i].next_hop == DeadNbr) //if it is in fact using the dead neighbor as the next hop then change the cost to infinity
	{
	  routingTable[i].cost = INFINITY;
	  printf("\nConnection to: %d \n", i);
	  printf("\nNew cost: %d \n", routingTable[i].cost);
	}
    } //end of for
  return;
}

/*
void main(){
  return;
}
*/



