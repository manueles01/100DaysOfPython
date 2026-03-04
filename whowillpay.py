import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
winner = random.choice(friends)
print(winner)
#another way to do this:
random_index = random.randint(0,len(friends)-1)
print(friends[random_index])
