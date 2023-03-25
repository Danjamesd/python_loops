x = "Hey there. How are you?"

for i in x :
    if i == "." :
        break # exits the loop and prints "Hey there"
    # in other words it prints x verbatim until before the "."
    print (i, end="") # each character in x is printed with nothing in between it.
    