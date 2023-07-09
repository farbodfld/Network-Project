import socket

def send_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(request.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Response: {response}")

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 80

    operator = input("Enter the operator: ")
    op1 = float(input("Enter operand 1: "))
    op2 = float(input("Enter operand 2 (if applicable): "))

    request = f"{operator} {op1} {op2}"
    send_request(host, port, request)
