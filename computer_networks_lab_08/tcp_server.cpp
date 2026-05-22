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
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    // Create a TCP socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == 0) {
        cerr << "Socket creation failed" << endl;
        return -1;
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);

    // Bind the socket to the address and port
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        cerr << "Bind failed" << endl;
        close(server_fd);
        return -1;
    }

    // Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        cerr << "Listen failed" << endl;
        close(server_fd);
        return -1;
    }

    cout << "Server waiting for connection...\n";

    // Accept an incoming connection
    new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen);
    if (new_socket < 0) {
        cerr << "Accept failed" << endl;
        close(server_fd);
        return -1;
    }

    Data d;
    // Receive data structure from the client
    recv(new_socket, &d, sizeof(d), 0);

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
    send(new_socket, &result, sizeof(result), 0);

    cout << "Result sent to client\n";

    // Close sockets
    close(new_socket);
    close(server_fd);
    return 0;
}
