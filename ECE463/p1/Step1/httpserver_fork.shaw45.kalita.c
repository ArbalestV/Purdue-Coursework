#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <unistd.h> //for the access() functions

#define MAXLINE 1024
#define LISTENQ 20



void process_request(int connfd)
{
        char filename[MAXLINE];
        char buf[MAXLINE];
	FILE * ifile;
	while (read(connfd, buf, MAXLINE) != 0)
	{
	  /*
		ifile = fopen(filename,"r");
		while (fread(buf, strlen(buf), 1, ifile) )
		{
			write(connfd, buf, strlen(buf));
		}
	  */
	  //printf("\nName of the filename received from the client: %s", buf);
	  //printf("\nSize of initial buffer: %d", sizeof(buf));
	  ///print("In here");


	  
	  //now the current content of buf[] is "GET Name_Of_File" HTTP/1.0"
	  //therefore, we will start from location 4, and iterate until we get the first space, which will be j
	  //the name of the file that we will need will be buf[4:j-1]
	  //then we will terminate it with the null string character '\0'
	  int i = 4;
	  int for_slash_fd = 0;
	  if (buf[4] == '/'){
	    i = 5;
	    for_slash_fd = 1;
	  }
	  //printf("\ni = %d", i);
	  while (buf[i] != ' '){
	    //printf("\ni in loop now = %d and corresponding character = %c", i, buf[i]);
	    //filename[i - 4] = buf[i];
	    //printf("\n Assigned filename index = %d, character: %c", (i - 4), filename[i - 4]);
	    if (for_slash_fd == 0) {
	      filename[i - 4] = buf[i];
	    }
	    else if (for_slash_fd == 1){
	      filename[i - 5] = buf[i];
	    }
	    i++;
	  }
	  //filename[i - 4] = '\0';
	  if (for_slash_fd == 0) {
	    filename[i - 4] = '\0';
	  }
	  else if (for_slash_fd == 1){
	    filename[i - 5] = '\0';
	  }
	  //printf("\nFilename now: %s", filename);
	  //printf("\nnow will try to open the file");
	  //printf("\nSize of filename: %d", sizeof(filename));
	  
	  
	  //now, we will try to check one by one if the file is readable and if the file exists. If either of these two conditions are not satisfied, then we will print the appropriate error message and return. Else, we will go to read from the file and display its contents on the client side.
	  
	  char buf_client_write[MAXLINE];
	  
	  int is_existing = access(filename, F_OK);
	  //printf("\n\nexisting = %d", is_existing);
	  if (is_existing == -1) {//i.e, does not exists
	    strcpy(buf_client_write, "HTTP/1.0 404 Not Found\r\n\r\n");
	    write(connfd, buf_client_write, strlen(buf_client_write));
	    return;
	  }

	  int is_readable = access(filename, R_OK);
	  //printf("\n\nis_readable = %d", is_readable);
	  if (is_readable == -1) {//i.e, not readable
	    strcpy(buf_client_write, "HTTP/1.0 403 Forbidden\r\n\r\n");
	    write(connfd, buf_client_write, strlen(buf_client_write));
	    return;
	  }
	  
	  //now, the file exists and is readable. so, just open the file using a file pointer, display the appropriate message, and then display its contents.
	  FILE * fp = NULL;
	  fp = fopen(filename, "r");
	  //now read data from the file and send it to client
	  strcpy(buf_client_write, "HTTP/1.0 200 OK\r\n\r\n");
	  write(connfd, buf_client_write, strlen(buf_client_write));
	  while (1){
	    //first read file in chunks of 256 bytes
	    //printf("\n\n\nIn here.");	    
	    unsigned char buff_display[256] = {0};
	    int check_num_read = fread(buff_display, 1, 256, fp);
	    if (check_num_read > 0){ //i.e, the read was successful, then write
	      write(connfd, buff_display, check_num_read);
	    }
	    if (check_num_read < 256) {//basically this means that the file either has less than 256 bytes to begin with, or that it is in its last iteration of 256 bytes
	      return; //end the server connection
	    }
	    }
	  
	}
}

int main(int argc, char **argv) 
{
	int listenfd, connfd, port, clientlen;
	struct sockaddr_in clientaddr;
	struct hostent *hp;
	char *haddrp;
	port = atoi(argv[1]); /* the server listens on a port passed on the command line */
	
	listenfd = open_listenfd(port); 

	while (1) 
	{
		clientlen = sizeof(clientaddr); 
		connfd = accept(listenfd, (struct sockaddr *)&clientaddr, &clientlen);
		//hp = gethostbyaddr((const char *)&clientaddr.sin_addr.s_addr, sizeof(clientaddr.sin_addr.s_addr), AF_INET);
		//haddrp = inet_ntoa(clientaddr.sin_addr);
		// printf("Fd %d connected to %s (%s:%d)	\n", connfd, hp->h_name, haddr p, ntohs(clientaddr.sin_port));
		int childpid;
		if ( ( childpid = fork()) == 0)
		  { /* child process */
		    close(listenfd);
		    process_request(connfd);
		    exit(0);
		  }
		//sleep(2000);
		close(connfd); //parent process
	}
}




int open_listenfd(int port)  
{ 
	int listenfd, optval=1; 
	struct sockaddr_in serveraddr; 

	/* Create a socket descriptor */ 
	if ((listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
		return -1; 

	/* Eliminates "Address already in use" error from bind. */ 
	if (setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR,(const void *)&optval , sizeof(int)) < 0) 
		return -1; 

	/* Listenfd will be an endpoint for all requests to port on any IP address for this host */ 
	bzero((char *) &serveraddr, sizeof(serveraddr)); 
	serveraddr.sin_family = AF_INET;  
	serveraddr.sin_addr.s_addr = htonl(INADDR_ANY);  
	serveraddr.sin_port = htons((unsigned short)port);  

	if (bind(listenfd, (struct sockaddr *)&serveraddr, sizeof(serveraddr)) < 0) 
		return -1; 

	/* Make it a listening socket ready to accept connection requests */ 

	if (listen(listenfd, LISTENQ) < 0) 
		return - 1; 

	return listenfd; 
} 
