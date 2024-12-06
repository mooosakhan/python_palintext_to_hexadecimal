from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
from binascii import hexlify

# 1. Generate a random AES key and IV (Initialization Vector)
key = get_random_bytes(16)  # AES key size 128-bit (16 bytes)
iv = get_random_bytes(AES.block_size)  # AES block size (16 bytes)

# Display the key and IV in hexadecimal format
print("Key:", hexlify(key).decode())
print("IV:", hexlify(iv).decode())

# 2. Input plaintext for encryption
plaintext = "This is a secret message!"
print("Plaintext:", plaintext)


# 3. Encrypt the plaintext using the AES key and IV
cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(plaintext.encode())

# Convert the ciphertext to a hexadecimal string for readability

encoded_ciphertext = hexlify(ciphertext).decode()
print("ciphertext:", ciphertext)
# Display the ciphertext in hexadecimal format
print("Ciphertext (Hex):", encoded_ciphertext)

# 4. Decrypt the ciphertext back into plaintext
# For decryption, we need to initialize the AES cipher with the same key and IV
decipher = AES.new(key, AES.MODE_CFB, iv)
decryptedtext = decipher.decrypt(ciphertext).decode()

# Display the decrypted text (should match the original plaintext)
print("Decrypted Text:", decryptedtext)
