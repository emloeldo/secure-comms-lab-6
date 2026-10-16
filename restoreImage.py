from collections import Counter
from PIL import Image

encryptedImage = open("aes.bmp.enc", "rb").read()

aesBlocks = [encryptedImage[i:i+16] for i in range(0, len(encryptedImage)-15, 16)]

#most repeated block
common = Counter(aesBlocks).most_common(1)[0][0]

#white for repeated blocks, black for others
pixels = b"".join(bytes([255 if b == common else 0]) * 16 for b in aesBlocks)

#og size image
image = Image.frombytes("RGB", (640, 480), pixels[:921600])

#didn't consider image may be flipped initially
image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

#save image
image.save("restoredImage.png")
