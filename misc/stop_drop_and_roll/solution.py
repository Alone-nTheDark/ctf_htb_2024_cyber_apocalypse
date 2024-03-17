import socket
from time import sleep

def send_message(sock, message):
    sock.sendall(message.encode())

def receive_message(sock):
    received_data = sock.recv(1024)
    return received_data.decode()

def parse_response(scenarios):
    responses = []
    for scenario in scenarios:
        if scenario == 'GORGE':
            responses.append('STOP')
        elif scenario == 'PHREAK':
            responses.append('DROP')
        elif scenario == 'FIRE':
            responses.append('ROLL')
    return '-'.join(responses)

def play_game():
    HOST = '94.237.53.3'  # The server's hostname or IP address
    PORT = 55670        # The port used by the server
    in_game = False
    data = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data.extend(receive_message(s).strip().split("\n"))
            print(data)

            if "What do you do?" in data[-1]:
                prev = data.pop()
                sc = data.pop()
                scenarios = sc.strip().split(', ')
                response = parse_response(scenarios)
                print(response)
                send_message(s, response + "\n")
            elif "Are you ready?" in data[-1]:
                # response = input("Are you ready? (y/n): ").strip().lower()
                send_message(s, "y\n")
                data.pop()
            elif "HTB{" in data[-1]:
                print("Flag found:", data[-1])
                break
            elif "Ok then! Let's go!" in data[-1]:
                data.pop
            elif "Unfortunate! You died!" in data[-1]:
                break
            else:
                data.pop()
            
            sleep(3)

if __name__ == "__main__":
    play_game()