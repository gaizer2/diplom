from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend


class CRYPTO:
    def save_private_key(self, private_key):
        filename = 'private_key.pem'
        with open(filename, 'wb') as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

    def load_private_key(self):
        filename = 'private_key.pem'
        with open(filename, 'rb') as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        return private_key

    def __init__(self):
        # Проверка существования ключа
        global private_key
        try:
            # Загружаем приватный ключ, если он существует
            private_key = self.load_private_key()
            print("Загружаем ключ")
        except FileNotFoundError:
            # Если ключа нет, создаем новый и сохраняем
            print("Создаем ключ")
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            self.save_private_key(private_key)
        self.shifor("qwewqew")

    def shifor(self, s):
        public_key = private_key.public_key()

        plaintext = s.encode("utf-8")
        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("Зашифрованный текст:", ciphertext)
        # return ciphertext, private_key
        self.re_shifor(ciphertext)

    def re_shifor(self, s):
        decrypted_text = private_key.decrypt(
            s,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        z = str(decrypted_text)
        f = len(z) - 1
        z = z[2:f]

        print(z)


if __name__ == "__main__":
    CRYPTO()
