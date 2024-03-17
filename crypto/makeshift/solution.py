def decode_flag(encoded_flag):
    reversed_flag = encoded_flag[:]
    decoded_flag = ''
    for i in range(0, len(reversed_flag), 3):
        decoded_flag += reversed_flag[i+2]
        decoded_flag += reversed_flag[i]
        decoded_flag += reversed_flag[i+1]
    return decoded_flag[::-1]

flag = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"

print(decode_flag(flag))