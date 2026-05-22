#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

using namespace std;

// Data structure to hold the numbers and the operator (must match client)
struct Data {
    int a;
    int b;
    char op;
};

int main() {
    int sockfd;
    struct sockaddr_in servaddr, cliaddr;

    // Create a UDP socket (SOCK_DGRAM)
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        cerr << "Socket creation failed" << endl;
        return -1;
    }

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(8081);

    // Bind the socket to the address and port
    if (bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0) {
        cerr << "Bind failed" << endl;
        close(sockfd);
        return -1;
    }

    Data d;
    socklen_t len = sizeof(cliaddr);

    cout << "UDP Server listening on port 8081...\n";

    // Receive data from the client
    recvfrom(sockfd, &d, sizeof(d), 0, (struct sockaddr*)&cliaddr, &len);

    int result = 0;

    // Perform calculation based on operator using switch-case
    switch(d.op) {
        case '+': result = d.a + d.b; break;
        case '-': result = d.a - d.b; break;
        case '*': result = d.a * d.b; break;
        case '/': 
            if (d.b != 0) {
                result = d.a / d.b; 
            } else {
                cerr << "Division by zero!" << endl;
                result = 0;
            }
            break;
        default: 
            cerr << "Invalid operator received: " << d.op << endl;
            result = 0;
    }

    // Send calculation result back to client
    sendto(sockfd, &result, sizeof(result), 0, (struct sockaddr*)&cliaddr, len);

    cout << "Result sent to client\n";

    // Close socket
    close(sockfd);
    return 0;
}
