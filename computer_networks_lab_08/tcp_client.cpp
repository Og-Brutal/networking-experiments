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
    int sock = 0;
    struct sockaddr_in serv_addr;

    // Create a TCP socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        cerr << "Socket creation error" << endl;
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(8080);

    // Convert IPv4 addresses from text to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        cerr << "Invalid address/ Address not supported" << endl;
        return -1;
    }

    // Connect to the server
    if (connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        cerr << "Connection failed" << endl;
        return -1;
    }

    Data d;

    cout << "Enter first number: ";
    cin >> d.a;

    cout << "Enter second number: ";
    cin >> d.b;

    cout << "Enter operator (+ - * /): ";
    cin >> d.op;

    // Send the data structure to the server
    send(sock, &d, sizeof(d), 0);

    int result;
    // Receive the calculation result from the server
    recv(sock, &result, sizeof(result), 0);

    cout << "Result = " << result << endl;

    // Close the socket connection
    close(sock);
    return 0;
}
