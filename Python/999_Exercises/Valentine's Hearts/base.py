people_list = ["Your denist", "Big Brother", "Kanye West", "small brother", "Grandmother"]
comp_list = ["is cool", "is fantastic", "Is a girl boss", "has nice hair", "is kind", "looking good","is smart"]

import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] + " " + comp_list[num_comp])