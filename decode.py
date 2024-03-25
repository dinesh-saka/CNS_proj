import rsa


class Decoder:
    def decode(self):
        with open("public.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open("private.pem", "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        pin = input("Decode pin: ")

        with open("signature", "rb") as f:
            signature = f.read()

        print(rsa.verify(pin.encode(), signature, public_key))
