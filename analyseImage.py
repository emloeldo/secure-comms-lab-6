from collections import Counter

#rb reads it in binary
encrypted_image = open("aes.bmp.enc", "rb").read()

#puts data into 16 byte blocks
aes_blocks = [encrypted_image[i:i+16] for i in range(0, len(encrypted_image)-15, 16)]

aesBlock_frequency = Counter(aes_blocks)

print("Number of AES blocks:", len(aes_blocks))

print("Different encrypted blocks:", len(aesBlock_frequency))

print("Top 5 repeated blocks:", aesBlock_frequency.most_common(5))
