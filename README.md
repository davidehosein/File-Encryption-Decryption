# File-Encryption-Decryption
Program to encrypt and decrypt files.

This is a program for encrypting and decrypting files using a key.

Instructions for encrypting a file:

1. Run file_encrypter_decrypter.py
2. Enter "E" for file encryption.
3. Place the file to be encrypted in the "file" directory.
4. Enter the name for the key file. The key will be generated and stored in the "key" directory.
5. Enter the name of the file to be encrypted. Ensure that this file is present in the "file" directory.
6. The file will be encrypted and stored in the "encrypted" directory.

Instructions for decrypting a file:

1. Run file_encrypter_decrypter.py
2. Enter "D" for file decryption.
3. Place the key file in the "key" directory.
4. Place the encrypted file in the "encrypted" directory.
5. Enter the name of the key file to be used for decrypting the file.
6. Enter the name of the encrypted file in the "encrypted" directory.
7. The file will be decrypted and stored in the "decrypted" directory.

It is extremely important to not lose the key file, as this is the ONLY key that can be used to decrypt the file.

## Note: This program uses the following external package: cryptography

If you do not have this package installed, you can install it with pip.<br/>
On Windows, execute the following command: pip install cryptography<br/>
On Linux/macOS, execute the following command: pip3 install cryptography<br/>