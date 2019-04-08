import sys

# Convert binary to zero-width string.
binary = sys.stdin.read()
lookup = {'0': '\u200b', '1': '\u200c', ' ': '\u200d'}
for char in binary:
    print(lookup[char], end = '')
