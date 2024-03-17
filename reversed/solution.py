# # local_28 = bytearray.fromhex('540345434c75637f')
# # for i in range(len(local_28)):
# #     local_28[i] ^= 0x37

# # string_28 = local_28.decode('utf-8')[::-1]

# # print(string_28)

# local_28 = 0x540345434c75637f
# local_28_bytes = local_28.to_bytes(8, byteorder='little')  # Convert integer to bytes

# # Reverse the string by XOR-ing each byte with 0x37
# reversed_local_28_bytes = bytes([byte ^ 0x37 for byte in local_28_bytes])

# reversed_local_28_string = reversed_local_28_bytes.decode('utf-8')  # Decode bytes to string

# print(reversed_local_28_string)


# local_20 = 0x45f4368505906
# local_20_bytes = local_20.to_bytes(8, byteorder='little')  # Convert integer to bytes
# reversed_local_20_bytes = bytes([byte ^ 0x37 for byte in local_20_bytes])
# reversed_local_20_string = reversed_local_20_bytes.decode('utf-8')

# print(reversed_local_20_string)

# uStack_19 = 0x68
# reversed_uStack_19 = uStack_19 ^ 0x37
# reversed_uStack_19_string = chr(reversed_uStack_19)
# print(reversed_uStack_19_string)


# uStack_18 = 0x374a025b5b0354
# uStack_18_bytes = uStack_18.to_bytes(7, byteorder='little')  # Convert integer to bytes
# reversed_uStack_18_bytes = bytes([byte ^ 0x37 for byte in uStack_18_bytes])
# reversed_uStack_18 = reversed_uStack_18_bytes.decode('utf-8')
# print(reversed_uStack_18)

# print(reversed_local_28_string + reversed_local_20_string + reversed_uStack_19_string + reversed_uStack_18)

local_28 = 0x540345434c75637f
local_20 = 0x45f4368505906
uStack_19 = 0x68
uStack_18 = 0x374a025b5b0354

# Reverse local_28
reversed_local_28 = local_28 ^ 0x3737373737373737

# Reverse local_20
reversed_local_20 = local_20 ^ 0x373737373737

# Reverse uStack_19
reversed_uStack_19 = uStack_19 ^ 0x37

# Reverse uStack_18
reversed_uStack_18 = uStack_18 ^ 0x37373737373737

# Convert to UTF-8 strings
local_28_str = reversed_local_28.to_bytes((reversed_local_28.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
local_20_str = reversed_local_20.to_bytes((reversed_local_20.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
uStack_19_str = chr(reversed_uStack_19)
uStack_18_str = reversed_uStack_18.to_bytes((reversed_uStack_18.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

string_28 = local_28_str[::-1]
string_20 = local_20_str[::-1]
string_18 = uStack_18_str[::-1]

print("Reversed local_28:", string_28)
print("Reversed local_20:", string_20)
print("Reversed uStack_19:", uStack_19_str)
print("Reversed uStack_18:", string_18)

print(string_28 + string_20 + uStack_19_str + string_18)