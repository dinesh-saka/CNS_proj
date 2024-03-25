import rsa


class Encoder:
    def encode(self):
        """Encodes an integer PIN using RSA with user-specified hash function."""

        with open("public.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open("private.pem", "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        # Prompt for PIN and ensure it's an integer
        while True:
            try:
                pin = input("Enter your PIN: ")
                break
            except ValueError:
                print("Invalid PIN.")

        # Prompt for and validate hash function selection
        valid_hashes = ["SHA-256", "SHA-384", "SHA-512"]
        while True:
            hash_function = input(
                "Select a hash function (SHA-256, SHA-384, or SHA-512): "
            ).upper()
            if hash_function in valid_hashes:
                break
            else:
                print(
                    f"Invalid hash function. Please choose from: {', '.join(valid_hashes)}"
                )

        # Sign the hash with the private key
        signature = rsa.sign(pin.encode(), private_key, hash_function)

        # Write the signature to a file (consider secure storage alternatives)
        with open("signature", "wb") as f:
            f.write(signature)

        print("PIN encoded and signature created successfully.")
