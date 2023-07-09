import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

received_packets = {}  # Store the received packets
offset = 0

try:
    # Send a request to the server
    fileName = input('Enter the file name: ')
    print(fileName)
    client_socket.sendto(fileName.encode(), (HOST, PORT))

    while True:
        # Receive the chunk of file data from the server
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
        print('PART DATA IS: ' + partData)
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

    # # Receive the file data from the server
    # data, server_address = client_socket.recvfrom(4096)  # Specify the buffer size as needed

    # File path to save the received file
    save_path = r'C:\Users\USER\Desktop\result.txt'

    # Save the received file data
    with open(save_path, 'wb') as file:
        for i in range(0, offset + 1):
            if i not in received_packets.keys():
                raise Exception("PART NOT FOUND!!")

            file.write(received_packets[i])

    # # Save the received file data
    # with open(save_path, 'wb') as file:
    #     file.write(data)

    print('File data received and saved successfully.')
except Exception as e:
    print('Error occurred while communicating with the server:', str(e))
finally:
    # Close the client socket
    client_socket.close()
