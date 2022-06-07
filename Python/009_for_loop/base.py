length = int(input("Please enter line length: "))
vh = input("Vertical or horizontal line? ")

if vh == "horizontal":
    for x in range(0,length):
        print("*", end="")
        
if vh == "vertical":
    for x in range(0,length):
        print("*")


    