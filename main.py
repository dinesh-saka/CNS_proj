from keyGeneration import KeyGenerator
from encode import Encoder
from decode import Decoder

def main():
    # Key generation
    key_gen = KeyGenerator()
    key_gen.generate_keys()

    # Encoding
    encoder = Encoder()
    encoder.encode()

    # Decoding
    decoder = Decoder()
    decoder.decode()

if __name__ == "__main__":
    main()
