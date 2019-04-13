import sys

# Read standard input to end.
document = ' '.join(sys.stdin.readlines())

# Detect any forbidden characters in input.
forbidden = ['\u200b', '\u200c', '\u200d']
alert = False
for char in document:
  if char in forbidden:
    alert = True

# Show message depending on whether or not zero-width characters were found.
if alert:
    print('Document contains zero-width characters!')
else:
    print('Document does not contain zero-width characters!')
