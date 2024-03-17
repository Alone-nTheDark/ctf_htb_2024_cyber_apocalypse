import subprocess
from time import sleep

def send_command_and_receive_response(host, port):
    index = 0
    final_response = ""

    while "}" not in final_response:
        # Connect to the server using nc
        connection = subprocess.Popen(
            ['nc', host, str(port)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Send the index as a command
        command = str(index) + "\n"
        connection.stdin.write(command)
        connection.stdin.flush()

        # Receive response
        response = connection.stdout.readline().strip()

        # Concatenate response to final_response
        final_response += response.split(":")[2].strip()
        print("Received:", index, final_response)

        # Close the connection
        connection.stdin.close()
        connection.stdout.close()
        connection.stderr.close()
        connection.wait()

        # Increment the index
        index += 1
        sleep(1)

    print("Received the final response:", final_response)

if __name__ == "__main__":
    host = "94.237.51.96"
    port = 30927
    send_command_and_receive_response(host, port)
