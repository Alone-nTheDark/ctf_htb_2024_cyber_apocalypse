from random import randint

def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def decrypt(ciphertext):
    decrypted_text = ''
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if not ch.isalpha():
            dch = ch
        else:
            dci = (to_identity_map(ch) - i) % 26
            dch = from_identity_map(dci)
        decrypted_text += dch
    return decrypted_text

print(decrypt("DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"))
