from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad #Counter, unpad

def invertbit(plain_input, b):
    bit_list = []
    for bit in plain_input:
            bit_list.append(bin(bit)[2:].zfill(8))
            bit_seq = ''.join(bit_list)
            if b < len(bit_seq):
                temp = '1' if bit_seq[b] == '0' else '0'
                bit_seq = bit_seq[:b] + temp + bit_seq[b + 1:]
                plain_input = bytes(int(bit_seq[i: i + 8], 2) for i in range(0, len(bit_seq), 8))
    return plain_input


def bit_diff(org_cipher, diff_cipher):
    num = 0
    for org, diff in zip(org_cipher, diff_cipher):
        if org == diff:
            continue
        t1, t2 = bin(org)[2:].zfill(8), bin(diff)[2:].zfill(8)
        num += sum(t1[i] != t2[i] for i in range(len(t1)))
    return num

def aes_input_av_test(plain_input, key, list):
    # pad the input with zeros
    if len(plain_input) % 16 != 0:
        plain_input += b'\x00' * (16 - len(plain_input) % 16)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plain_input)
    results = []
    for pos in list:
        flipped_plaintext = bytearray(plain_input)
        flipped_plaintext[pos // 8] ^= 1 << (pos % 8)
        flipped_ciphertext = cipher.encrypt(bytes(flipped_plaintext))
        num_changed_bits = sum(bin(a ^ b).count('1') for a, b in zip(ciphertext, flipped_ciphertext))
        results.append(num_changed_bits)
    return results

def aes_key_av_test(plain_input, key, list):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plain_input)
    results = []
    for pos in list:
        flipped_key = bytearray(key)
        flipped_key[pos // 8] ^= 1 << (pos % 8)
        flipped_ciphertext = cipher.encrypt(plain_input, bytes(flipped_key))
        num_changed_bits = sum(bin(a ^ b).count('1') for a, b in zip(ciphertext, flipped_ciphertext))
        results.append(num_changed_bits)
    return results

def aes_key_av_test(plain_input, key, list):
    cipher = AES.new(key, AES.MODE_ECB)
    # pad the input with zeros
    if len(plain_input) % 16 != 0:
        plain_input += b'\x00' * (16 - len(plain_input) % 16)
    ciphertext = cipher.encrypt(plain_input)
    results = []
    for pos in list:
        flipped_key = bytearray(key)
        flipped_key[pos // 8] ^= 1 << (pos % 8)
        flipped_cipher = AES.new(bytes(flipped_key), AES.MODE_ECB)
        flipped_ciphertext = flipped_cipher.encrypt(plain_input)
        num_changed_bits = bitwise_hamming_distance(ciphertext, flipped_ciphertext)
        results.append(num_changed_bits)
    return results

def des_input_av_test(plaintext, key, bit_pos_list):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    num_bits_changed = []
    for bit_pos in bit_pos_list:
        modified_plaintext = bytearray(plaintext)
        modified_plaintext[bit_pos // 8] ^= (1 << (7 - bit_pos % 8))
        modified_ciphertext = cipher.encrypt(bytes(modified_plaintext))
        num_bits_changed.append(bitwise_hamming_distance(ciphertext, modified_ciphertext))
    return num_bits_changed


def des_key_av_test(plaintext, key, bit_pos_list):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    num_bits_changed = []
    for bit_pos in bit_pos_list:
        modified_key = bytearray(key)
        modified_key[bit_pos // 8] ^= (1 << (7 - bit_pos % 8))
        modified_cipher = DES.new(bytes(modified_key), DES.MODE_ECB)
        modified_ciphertext = modified_cipher.encrypt(plaintext)
        num_bits_changed.append(bitwise_hamming_distance(ciphertext, modified_ciphertext))
    return num_bits_changed


def bitwise_hamming_distance(bytes1, bytes2):
    distance = 0
    for b1, b2 in zip(bytes1, bytes2):
        distance += bin(b1 ^ b2).count('1')
    return distance


if __name__ == "__main__":
    plaintext = b'thisoneis16bytes'
    key = b'deskey!!'
    input_bits_to_flip = [3, 25, 36]
    key_bits_to_flip = [3, 25, 36]
    input_av_test_results = des_input_av_test(plaintext, key, input_bits_to_flip)
    key_av_test_results = des_key_av_test(plaintext, key, key_bits_to_flip)
    print('DES Input AV Test Results:', input_av_test_results)
    print('DES Key AV Test Results:', key_av_test_results)
    print(aes_input_av_test(b'isthis16bytes?', b'veryverylongkey!', [5, 29, 38]))
    print(aes_key_av_test(b'isthis16bytes?', b'veryverylongkey!', [5, 29, 38]))