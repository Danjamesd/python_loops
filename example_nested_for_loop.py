x = [[1, 2, 3], ["a", "b", "c"]]
for i in x:
    for j in i: # iterate the two lists separately
        print(j, end="")
    #end is used to separate the two lists
    print()
    # print the resultant lists as two separate lines as per the first for loop
    