import random 

resturant = ["Subway", "Panda Express", "McDonalds"]

SubwayItems = ["Tuna Sub", "Turkey Sub", "Ham Sub"]
PandaExpressItems = ["Orange Chicken", "Beef and Broccoli", "Walnut Shrimp"]
McDonaldsItems = ["Happy Meal", "French Fries", "Chicken Nuggets" ]

resturantchoice = input("Which resturant would you like to go to? Subway, Panda Express, or McDonalds?")

if resturantchoice == "Subway":
    print("Today's Special:")
    print(SubwayItems[random.randrange(0,2)])
    SubwayItems = input("What would you like a Tuna, Ham or Turkey sub?")
    
if resturantchoice == "Panda Express":
    print("Today's Special :")
    print(PandaExpressItems[random.randrange(0,2)])
    PandaExpressItems = input("Orange Chicken", "Beef and Broccoli", "Walnut Shrimp")
    
if resturantchoice == "McDonalds":
    print("Today's Special :")
    print(McDonaldsItems[random.randrange(0,2)])
    McDonalds = input("Happy Meal", "Chicken Nuggets", "French Fries")
    