#include <iostream>
#include <unistd.h>
#include <arpa/inet.h>
#include <cstring>

using namespace std;

int main() {
    int sock;
    struct sockaddr_in serv_addr;
    char buffer[1024] = {0};

    // 1. Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(8080);

    // Convert IP address
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

    // 2. Connect to server
    connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

    // 3. Send request
    char message[] = "Hello Server";
    send(sock, message, strlen(message), 0);

    // 4. Receive response
    read(sock, buffer, 1024);
    cout << "Server reply: " << buffer << endl;

    close(sock);

    return 0;
}
