items = int(input("How many items "))

total = 0 
for i in range (0, items) :
    z = input("What is the item? ")
    price = int(input("How much is it "))
    print("Thanks for purchasing " + z )
    total = total + price
    
print("Your total is: " + str(total))