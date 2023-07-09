import socket
from timeit import default_timer as timer
import datetime
import math

def perform_operation(operator, op1, op2=None):
    if operator == 'Add':
        return op1 + op2
    elif operator == 'Subtract':
        return op1 - op2
    elif operator == 'Multiply':
        return op1 * op2
    elif operator == 'Divide':
        if op2 != 0:
            return op1 / op2
        else:
            return "Error: Division by zero"
    elif operator == 'Sin':
        return math.sin(op1)
    elif operator == 'Cos':
        return math.cos(op1)
    elif operator == 'Tan':
        return math.tan(op1)
    elif operator == 'Cot':
        return 1 / math.tan(op1)
    else:
        return "Error: Invalid operator"

def parse_request(request):
    parts = request.split()
    operator = parts[0].strip()
    op1 = float(parts[1].strip())
    op2 = None
    if len(parts) > 2:
        op2 = float(parts[2].strip())
    return operator, op1, op2

def handle_request(request):
    operator, op1, op2 = parse_request(request)
    start_time = timer()
    result = perform_operation(operator, op1, op2)
    end_time = timer()
    calculation_time = end_time - start_time
    d = str(datetime.timedelta(seconds=calculation_time))
    return f"{d} {result}"

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server started on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connected to client: {client_address[0]}:{client_address[1]}")

            request = client_socket.recv(1024).decode('utf-8')
            response = handle_request(request)

            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 80
    start_server(host, port)
