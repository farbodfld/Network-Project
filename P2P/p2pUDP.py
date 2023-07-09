import socket
import sys
import os

# Server configuration
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024


def serverMode(directory):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Bind the socket to a specific address and port
        server_socket.bind((HOST, PORT))

        print('Server is listening for incoming messages...')

        while True:
            # Receive a message and client address
            fileName, addr = server_socket.recvfrom(BUFFER_SIZE)
            print('Connected to:', addr)

            file_name = fileName.decode()
            print('file name is: ' + file_name)
            filepath = os.path.join(directory, file_name)

            if not os.path.isfile(filepath):
                print('The specified file does not exist')
                return

            try:
                # Read file data in chunks and send to the client
                with open(filepath, 'rb') as file:
                    partNumber = 0
                    while True:
                        print(partNumber)
                        data = file.read(BUFFER_SIZE - 4)
                        if not data:
                            print('NO MORE DATA')
                            break
                        offset = str(partNumber).zfill(4).encode()  # Convert part number to 4-byte ASCII representation
                        server_socket.sendto(offset + data, addr)
                        partNumber += 1
                print('File data sent successfully.')
            except FileNotFoundError:
                print(f"File '{filepath}' not found.")
            except IOError:
                print(f"Error reading file '{filepath}'.")
            except Exception as e:
                print('Error occurred while sending the file data:', str(e))
            finally:
                break
    except Exception as e:
        print('Error occurred while starting the server:', str(e))
    finally:
        # Close the server socket
        server_socket.close()


def clientMode(file_name):
    received_packets = {}  # Store the received packets
    offset = 0

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        client_socket.sendto(file_name.encode(), (HOST, PORT))

        # Receive the file data from the server
        while True:
            chunk, _ = client_socket.recvfrom(BUFFER_SIZE)

            if not chunk:
                print('NO MORE DATA FROM SERVER')
                break

            print(chunk)
            print('***************************************************************\n')

            decodedData = chunk.decode()
            print('DECODED DATA IS: \n' + decodedData)
            print('***************************************************************\n')

            partNumber_str = decodedData[:4]
            print('PART NUMBER IS: ' + partNumber_str)
            print('***************************************************************\n')

            partData = decodedData[4:]
            print('PART DATA IS: \n' + partData)
            print('***************************************************************\n')

            partNumber = int(partNumber_str)
            print(partNumber)
            print('***************************************************************\n')

            encodedData = partData.encode()  # Encode the data for save it at the dictionary.
            received_packets[partNumber] = encodedData

            if offset < partNumber:
                offset = partNumber

            if len(partData) < BUFFER_SIZE:
                break

        # File path to save the received file
        save_path = r'C:\Users\USER\Desktop\downloaded-file.txt'

        # Save the received file data
        with open(save_path, 'wb') as file:
            for i in range(0, offset + 1):
                if i not in received_packets.keys():
                    raise Exception("PART NOT FOUND!!")

                file.write(received_packets[i])

        print('File data received and saved successfully.')
    except Exception as e:
        print('Error occurred while communicating with the server:', str(e))
    finally:
        # Close the client socket
        client_socket.close()


def main():
    mode = sys.argv[1]
    if mode == '-server':
        if len(sys.argv) < 3:
            print('Directory not specified. Usage: python p2pUDP.py -server <directory>')
            return
        directory = sys.argv[2]
        if not os.path.isdir(directory):
            print('Invalid directory. Please provide a valid directory.')
            return
        serverMode(directory)
    elif mode == '-receive':
        if len(sys.argv) < 3:
            print('Filename not specified. Usage: python p2pUDP.py -receive <filename>')
            return
        filename = sys.argv[2]
        clientMode(filename)
    else:
        print('Invalid mode. Use -server or -receive.')


if __name__ == '__main__':
    main()
