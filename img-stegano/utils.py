import sys

# Convert a string of ascii characters to binary
def ascii_to_bin(msg: str) -> str:
    if type(msg) != str:
        sys.exit(f"Cannot convert {msg} to binary :(")
    
    msg_bin = ''.join(format(ord(i), '08b') for i in msg)
    return msg_bin