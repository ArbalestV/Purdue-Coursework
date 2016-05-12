#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

# define MAXLINE 500

//Client main
int main (int argc, char ** argv)
{
	if( argc < 3 )
	{
		fprintf(stderr, "Usage : ./httpclient <server name> <port> <filename>\n");
		exit(EXIT_FAILURE);
	}
	int clientfd, port; 
	char *host, buf[MAXLINE];
	char filename[MAXLINE];
	host = argv[1]; 
	port = atoi(argv[2]);
	strcpy(filename, argv[3]);
	clientfd = open_clientfd(host, port);
	// fprintf(stderr, "CLIENT FD: %d\n", clientfd);

	char * request_msg = (char *)calloc(strlen("GET  HTTP/1.0\r\n\r\n") + strlen(argv[3]) + 1, sizeof(char));
	strcpy(request_msg, "GET ");
	strcpy(request_msg + strlen("GET "), argv[3]);
	strcpy(request_msg + strlen("GET ") + strlen(argv[3]), " HTTP/1.0\r\n\r\n");
	
	write(clientfd, request_msg, strlen(request_msg));

	char c;
	while( read(clientfd, &c, 1) > 0 )
		fprintf(stdout, "%c", c);

	close(clientfd); 
	exit(0); 
	
}


int open_clientfd(char *hostname, int port) 
{ 
	int clientfd; 
	struct hostent *hp; 
	struct sockaddr_in serveraddr; 
	if ((clientfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
		return -1; /* check errno for cause of error */ 
	
	/* Fill in the server's IP address and port */ 
	if ((hp = gethostbyname(hostname)) == NULL) 
		return -2; /* check h_errno for cause of error */ 

	bzero((char *) &serveraddr, sizeof(serveraddr)); 
	serveraddr.sin_family = AF_INET; 
	bcopy((char *)hp->h_addr,
		(char *)&(serveraddr.sin_addr.s_addr), hp->h_length); 
	serveraddr.sin_port = htons(port); 
	
	/* Establish a connection with the server */ 
	if (connect(clientfd, (struct sockaddr *) &serveraddr, sizeof(serveraddr)) < 0) 
		return -1; 

	return clientfd; 
} 

