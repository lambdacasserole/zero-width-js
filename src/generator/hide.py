# Convert binary to zero-width string.
binary = input()
lookup = {'0': '\u200b', '1': '\u200c', ' ': '\u200d'}
for char in binary:
    print(lookup[char], end = '')
