class Encoder:
    def __init__(self, rot_n: int = 47, hex_separator: str = " 263a "):
        self.rot_n = rot_n
        self.hex_separator = hex_separator

        self.plain_chars = [chr(i) for i in range(33, 127)]
        self.cipher = [self.plain_chars[(i + self.rot_n) % len(self.plain_chars)] for i in range(0, len(self.plain_chars))]

        self.plain_chars_index_map = {self.plain_chars[i]:i for i in range(0, len(self.plain_chars))}
        self.cipher_index_map = {self.cipher[i]:i for i in range(0, len(self.cipher))}

    def encode(self, text: str) -> str:
        encoded_string = ""

        for c in text:
            encoded_string += self.cipher[self.plain_chars_index_map[c]]

        hex_string = ""
        for c in encoded_string:
            hex_string += hex(ord(c)).split("x")[1] + " "

        return hex_string.strip()
    
    def encode_list(self, texts: list[str]) -> str:
        hex_dump = ""

        for i in range(0, len(texts)):
            hex_dump += self.encode(texts[i])
            if i != len(texts) - 1:
                hex_dump += self.hex_separator

        return hex_dump.strip()
