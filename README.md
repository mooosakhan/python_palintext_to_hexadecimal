# AES Encryption and Decryption using `pycryptodome`

This Python program demonstrates how to perform AES encryption and decryption using the `pycryptodome` library. It generates a random AES key and IV (Initialization Vector), encrypts a plaintext message, and then decrypts it back to the original message. The ciphertext is displayed in hexadecimal format for better readability.

## Libraries Used

- **pycryptodome**: A self-contained cryptographic library for Python that provides various cryptographic functions like AES encryption.
- **binascii**: A module in Python for converting binary data to ASCII-encoded binary representations (e.g., converting binary ciphertext to hexadecimal).

## Features

- **AES Encryption**: The program uses AES (Advanced Encryption Standard) with a randomly generated key and IV.
- **Hexadecimal Ciphertext**: The ciphertext is converted to hexadecimal format for readability.
- **Secure Random Key and IV Generation**: The key and IV are generated using secure random number generation.
- **Padding Handling**: The program automatically handles padding for encryption and decryption.

## Installation

Before you run the program, make sure you have `pycryptodome` installed. If not, install it via `pip`.

### Step 1: Install Dependencies

```bash
pip install pycryptodome
```

### Step 2: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

## How to Use

### Step 1: Modify the `main.py`

You can modify the `plaintext` variable in the `main.py` file to change the message you want to encrypt. Here's how the code works:

1. **Key and IV Generation**: A random 128-bit AES key and a random 16-byte IV are generated.
2. **Encryption**: The plaintext message is encrypted using the AES algorithm in CFB (Cipher Feedback) mode.
3. **Hexadecimal Output**: The ciphertext is output in hexadecimal format for easy readability.
4. **Decryption**: The ciphertext is decrypted back to the original plaintext using the same key and IV.

### Step 2: Run the Script

To run the program, use the following command in your terminal or command prompt:

```bash
python main.py
```

### Example Output

```bash
Key: 0a0b12d34c56f7128f96da78b32b4a0c
IV: b93f2c5a31f1ad5c4f0c22f9d87ef9ed
Plaintext: This is a secret message!
Ciphertext (Hex): 1f07da3e6a90c6fdd6ff6d4f38b1f8fe
Decrypted Text: This is a secret message!
```

### Step 3: View the Results

- The **Key** and **IV** are displayed in hexadecimal format.
- The **Ciphertext** is also shown in hexadecimal format.
- The **Decrypted Text** should match the original plaintext, demonstrating that the encryption and decryption process was successful.

## Code Walkthrough

### Key and IV Generation

```python
key = get_random_bytes(16)  # 16 bytes = 128 bits key for AES
iv = get_random_bytes(AES.block_size)  # AES block size (16 bytes for AES)
```

- `get_random_bytes(16)` generates a random 128-bit AES key.
- `get_random_bytes(AES.block_size)` generates a random 16-byte IV for AES.

### Encryption

```python
cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(plaintext.encode())
```

- We create a new AES cipher object using the key and IV, and choose the CFB mode for encryption.
- The plaintext is encoded into bytes and encrypted.

### Hexadecimal Conversion

```python
encoded_ciphertext = hexlify(ciphertext).decode()  # Convert binary to hex
```

- The binary ciphertext is converted into a readable hexadecimal string using `hexlify()`.

### Decryption

```python
decipher = AES.new(key, AES.MODE_CFB, iv)
decryptedtext = decipher.decrypt(ciphertext).decode()
```

- The same key and IV are used to create a decryption object.
- The ciphertext is decrypted back into plaintext.

### Padding Handling

- The program uses `unpad()` (though not explicitly needed in this specific example, since CFB mode doesn’t require padding) to handle padding during encryption and decryption for block ciphers that do require padding (like CBC mode).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Feel free to open issues or pull requests for improvements. If you'd like to contribute to the code, follow the steps below:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request

## Author

- [Your Name](https://github.com/mooosakhan)
