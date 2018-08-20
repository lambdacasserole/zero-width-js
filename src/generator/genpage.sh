SCRIPT=$(cat -) # Read standard input to end.

# Hide and insert into document.
echo $SCRIPT | python3 encode.py | python3 hide.py | python3 substitute.py
