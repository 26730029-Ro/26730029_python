def printpattern(rows=5, cols=5, char="*"):

    for _ in range(rows):
        for _ in range(cols):
            print(char, end="")
        print()



printpattern(5, char="A")
