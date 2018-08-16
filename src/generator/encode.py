# Encode input ASCII as binary.
payload = input()
for char in payload:
    print(format(ord(char), 'b') + ' ', end='')
