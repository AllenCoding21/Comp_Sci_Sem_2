mynumbers = [6,9,32,28,15,22,3,18]

minimum = mynumbers[0]
for i in mynumbers:
    if i < minimum:
        minimum = i 
print("Minimum: " + str(minimum))

maximum = mynumbers[0]
for i in mynumbers:
    if i > maximum:
        maximum = i 
        
print("Maximum: " + str(maximum))

average = 0
number = 0 
for i in mynumbers:
    average = average + i 
    number = number + 1
average = average / number 

print ("average: " + str(average))



