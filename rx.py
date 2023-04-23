import socket
import argparse
from pynput.keyboard import Key, Controller

keyboard = Controller()

host = '192.168.1.11'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET using IPV4 Internet protocol
# SOCK_DGRAM datagram data might come in random order
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)


def main(host, port):
    print(f'host: {host}, port: {port}')

    s.bind((host, int(port)))

    while True:
        try:
            BYTE = 8192
            message, address = s.recvfrom(BYTE)
            LIST_DATA = str(message).split(",")
            rcvd_len = len(LIST_DATA)
            expected_len = 17
            if rcvd_len == expected_len:
                gravity_data = LIST_DATA[-3:]
                for idx, gravity in enumerate(gravity_data):
                    gravity_data[idx] = float(gravity.strip()[:-1])
                gx, gy, gz = gravity_data
                print(f"current_state : {gx}, {gy}, {gz}")            
        
        except(KeyboardInterrupt, SystemExit):
            raise
        except:
            pass

if __name__ =='__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--port', default = 5555)
    args.add_argument('--host', default = '192.168.1.11')
    parsed_args = args.parse_args()
    main(parsed_args.host, parsed_args.port)