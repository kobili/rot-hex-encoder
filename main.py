import sys
from ast import literal_eval
from io import TextIOWrapper

from decoder import Decoder
from encoder import Encoder

assert len(sys.argv) == 3, f"Missing argument(s): Have {len(sys.argv)}, need 3"
assert sys.argv[1] in ["unhide", "hide"], "Argument must be one of 'hide' or 'unhide'"

decode_mode = sys.argv[1] == "unhide"
file_path = sys.argv[2]

ROT_N = 47
HEX_SEPARATOR = " 263a "

decoder = Decoder(ROT_N, HEX_SEPARATOR)
encoder = Encoder(ROT_N, HEX_SEPARATOR)

def overwrite_file(file: TextIOWrapper, new_content):
    file.seek(0)
    file.write(str(new_content))
    file.truncate()

with open(file_path, "r+") as file:
    if decode_mode:
        # expecting a string of space separated hex bytes
        secret = file.read()
        overwrite_file(file, str(decoder.decode_hex_dump(secret)))
    else:
        # expecting a list of strings
        items = literal_eval(file.read())
        overwrite_file(file, encoder.encode_list(items))
