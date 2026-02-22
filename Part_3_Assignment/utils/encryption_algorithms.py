"""
Encryption and Decryption Algorithms for E91 Workshop
======================================================

This module provides simple encryption algorithms for demonstrating
the practical use of quantum-generated keys.
"""

def encrypt_xor_repeating_key(message: str, key: str) -> str:
    """
    Encrypt the message using the repeating-key XOR algorithm.
    
    Args:
        message: String of the message to encrypt
        key: String representing the encryption key (binary string from E91)
    
    Returns:
        Hex string representing the encrypted message
    """
    encrypted_bytes = bytearray()
    for i, ch in enumerate(message):
        key_ch = key[i % len(key)]
        encrypted_byte = ord(ch) ^ ord(key_ch)
        encrypted_bytes.append(encrypted_byte)
    return encrypted_bytes.hex()


def decrypt_xor_repeating_key(encrypted_message: str, key: str) -> str:
    """
    Decrypt the message using the repeating-key XOR algorithm.
    
    Args:
        encrypted_message: Hex string representing the encrypted message
        key: String representing the encryption key (binary string from E91)
    
    Returns:
        Decrypted message string
    """
    encrypted_bytes = bytes.fromhex(encrypted_message)
    decrypted_chars = []
    for i, byte in enumerate(encrypted_bytes):
        key_ch = key[i % len(key)]
        decrypted_char = chr(byte ^ ord(key_ch))
        decrypted_chars.append(decrypted_char)
    return "".join(decrypted_chars)


def encrypt_caesar_cipher(message: str, key: str) -> str:
    """
    Encrypt the message with a Caesar cipher.
    The key is provided as a binary string.
    
    Args:
        message: Message to encrypt
        key: Binary string representing the encryption key
    
    Returns:
        Encrypted message
    """
    shift = int(key, 2) % 26  # Convert binary to int, mod 26 for alphabet
    result = []
    for ch in message:
        if ch.isupper():
            shifted = (ord(ch) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(shifted))
        elif ch.islower():
            shifted = (ord(ch) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(shifted))
        else:
            result.append(ch)
    return "".join(result)


def decrypt_caesar_cipher(encrypted_message: str, key: str) -> str:
    """
    Decrypt the message encrypted with a Caesar cipher.
    
    Args:
        encrypted_message: Encrypted message
        key: Binary string representing the encryption key
    
    Returns:
        Decrypted message
    """
    shift = int(key, 2) % 26
    result = []
    for ch in encrypted_message:
        if ch.isupper():
            shifted = (ord(ch) - ord('A') - shift) % 26 + ord('A')
            result.append(chr(shifted))
        elif ch.islower():
            shifted = (ord(ch) - ord('a') - shift) % 26 + ord('a')
            result.append(chr(shifted))
        else:
            result.append(ch)
    return "".join(result)
