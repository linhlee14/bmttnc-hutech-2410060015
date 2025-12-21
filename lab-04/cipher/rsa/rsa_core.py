import rsa
import os
import pickle


class RSACipher:
    def __init__(self):
        self.private_key_file = "private_key.pem"
        self.public_key_file = "public_key.pem"

    # Generate RSA key pair and save to files
    def generate_keys(self, key_size=1024):
        public_key, private_key = rsa.newkeys(key_size)

        with open(self.public_key_file, "wb") as f:
            f.write(public_key.save_pkcs1())

        with open(self.private_key_file, "wb") as f:
            f.write(private_key.save_pkcs1())

    # Load RSA keys from files
    def load_keys(self):
        if not os.path.exists(self.private_key_file) or not os.path.exists(self.public_key_file):
            raise FileNotFoundError("RSA keys not found. Please generate keys first.")

        with open(self.public_key_file, "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open(self.private_key_file, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        return private_key, public_key

    # Encrypt message (string) using public key
    def encrypt(self, message, key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return rsa.encrypt(message, key)

    # Decrypt ciphertext (bytes) using private key
    def decrypt(self, ciphertext, key):
        decrypted = rsa.decrypt(ciphertext, key)
        return decrypted.decode("utf-8")

    # Sign message using private key
    def sign(self, message, private_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return rsa.sign(message, private_key, "SHA-256")

    # Verify signature using public key
    def verify(self, message, signature, public_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        try:
            rsa.verify(message, signature, public_key)
            return True
        except rsa.VerificationError:
            return False
