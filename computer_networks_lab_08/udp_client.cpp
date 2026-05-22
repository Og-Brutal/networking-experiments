#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

using namespace std;

// Data structure to hold the numbers and the operator
struct Data {
    int a;
    int b;
    char op;
};

int main() {
    int sockfd;
    struct sockaddr_in servaddr;

    // Create a UDP socket (SOCK_DGRAM)
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        cerr << "Socket creation failed" << endl;
        return -1;
    }

    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(8081);
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    Data d;

    cout << "Enter first number: ";
    cin >> d.a;

    cout << "Enter second number: ";
    cin >> d.b;

    cout << "Enter operator (+ - * /): ";
    cin >> d.op;

    // Send data structure to the server over UDP
    sendto(sockfd, &d, sizeof(d), 0, (struct sockaddr*)&servaddr, sizeof(servaddr));

    int result;
    socklen_t len = sizeof(servaddr);

    // Receive calculation result from the server over UDP
    recvfrom(sockfd, &result, sizeof(result), 0, (struct sockaddr*)&servaddr, &len);

    cout << "Result = " << result << endl;

    // Close the socket descriptor
    close(sockfd);
    return 0;
}
