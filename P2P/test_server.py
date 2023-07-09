import socket
import os

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024


def serverMode():
    file_path = input('Enter a file path: ')
    print(file_path)

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Bind the socket to a specific address and port
        server_socket.bind((HOST, PORT))

        print('Server is listening for incoming connections...')

        while True:
            # Receive data from the client
            fileName, client_address = server_socket.recvfrom(BUFFER_SIZE)
            print('Connected to:', client_address)

            try:
                filepath = os.path.join(file_path, fileName.decode())
                print(filepath)
                if os.path.isfile(filepath):
                    try:
                        # Read file data in bytes
                        with open(filepath, 'rb') as file:
                            partNumber = 0
                            while True:
                                print(partNumber)
                                fileData = file.read(BUFFER_SIZE - 4)
                                print(fileData)
                                if not fileData:
                                    print('NO MORE DATA')
                                    break
                                offset = str(partNumber).zfill(4).encode()  # Convert part number to 4-byte
                                server_socket.sendto(offset + fileData, client_address)
                                partNumber += 1
                        print('File data sent successfully.')
                        return
                    except FileNotFoundError:
                        print(f"File '{filepath}' not found.")
                        return
                    except IOError:
                        print(f"Error reading file '{filepath}'.")
                        return
                else:
                    print('The specified file does NOT exist')
                    return
            except Exception as e:
                print('Error occurred while sending the file data:', str(e))
    except Exception as e:
        print('Error occurred while starting the server:', str(e))
    finally:
        # Close the server socket
        server_socket.close()
        return


# Call the serverMode function
serverMode()
