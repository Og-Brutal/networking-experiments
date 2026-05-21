#include <iostream>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

using namespace std;

int main() {

    int sockfd;
    char buffer[1024];
    struct sockaddr_in serverAddr, clientAddr;
    socklen_t len = sizeof(clientAddr);

    // 1. Create UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    if (sockfd < 0) {
        cout << "Socket creation failed\n";
        return 1;
    }

    // 2. Setup server address
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    // 3. Bind socket
    bind(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr));

    cout << "UDP Server running on port 8080...\n";

    // 4. Receive message from client
    recvfrom(sockfd, buffer, sizeof(buffer), 0,
             (struct sockaddr*)&clientAddr, &len);

    cout << "Client says: " << buffer << endl;

    // 5. Send response
    char response[] = "Hello from UDP Server";
    sendto(sockfd, response, strlen(response), 0,
           (struct sockaddr*)&clientAddr, len);

    close(sockfd);

    return 0;
}
