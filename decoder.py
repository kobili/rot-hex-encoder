class Decoder:
	def __init__(self, rot_n: int = 47, hex_separator: str = " 263a "):
		self.rot_n = rot_n
		self.hex_separator = hex_separator

		self.plain_chars = [chr(i) for i in range(33, 127)]
		self.cipher = [self.plain_chars[(i + self.rot_n) % len(self.plain_chars)] for i in range(0, len(self.plain_chars))]

		self.plain_chars_index_map = {self.plain_chars[i]:i for i in range(0, len(self.plain_chars))}
		self.cipher_index_map = {self.cipher[i]:i for i in range(0, len(self.cipher))}

	def decode(self, hex_string: str) -> str:
		encoded_string = "".join([chr(int(s, 16)) for s in hex_string.split(" ")])

		decoded_string = ""
		for c in encoded_string:
			decoded_string += self.plain_chars[self.cipher_index_map[c]]

		return decoded_string

	def decode_hex_dump(self, hex_input: str) -> list[str]:
		hex_strings = hex_input.split(self.hex_separator)

		decoded_strings = []

		for s in hex_strings:
			decoded_strings.append(self.decode(s))

		return decoded_strings
