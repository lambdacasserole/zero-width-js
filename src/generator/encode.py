import sys

# Encode input ASCII as binary.
payload = sys.stdin.read()
for char in payload:
    print(format(ord(char), 'b') + ' ', end='')
