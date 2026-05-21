#include <iostream>
#include <unistd.h>
#include <arpa/inet.h>
#include <cstring>

using namespace std;

int main() {
    int server_fd, client_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};

    // 1. Create socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    if (server_fd == 0) {
        cout << "Socket failed\n";
        return 1;
    }

    // 2. Define server address
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);

    // 3. Bind socket
    bind(server_fd, (struct sockaddr *)&address, sizeof(address));

    // 4. Listen
    listen(server_fd, 3);
    cout << "Server waiting for connection...\n";

    // 5. Accept client
    client_socket = accept(server_fd, (struct sockaddr *)&address,
                     (socklen_t*)&addrlen);

    // 6. Receive request
    read(client_socket, buffer, 1024);
    cout << "Client says: " << buffer << endl;

    // 7. Send response
    char response[] = "Hello from Server";
    send(client_socket, response, strlen(response), 0);

    close(client_socket);
    close(server_fd);

    return 0;
}
