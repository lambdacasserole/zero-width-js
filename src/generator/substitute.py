import sys

# Load skeleton file text.
with open('skel.html', 'r') as content_file:
    content = content_file.read()

# Payload comes from input.
payload = sys.stdin.read()
print(content.replace('%PAYLOAD', payload))
