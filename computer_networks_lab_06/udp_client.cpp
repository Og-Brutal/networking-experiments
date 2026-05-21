#include <iostream>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

using namespace std;

int main() {

    int sockfd;
    char buffer[1024];
    struct sockaddr_in serverAddr;

    // 1. Create UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);

    inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr);

    // 2. Send request
    char message[] = "Hello UDP Server";

    sendto(sockfd, message, strlen(message), 0,
           (struct sockaddr*)&serverAddr, sizeof(serverAddr));

    // 3. Receive response
    socklen_t len = sizeof(serverAddr);

    recvfrom(sockfd, buffer, sizeof(buffer), 0,
             (struct sockaddr*)&serverAddr, &len);

    cout << "Server reply: " << buffer << endl;

    close(sockfd);

    return 0;
}
