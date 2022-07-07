import random
answer = input("Ask the 8 ball whatever you want.: ")
possibilities = ["Yes", "No", "Maybe", "Definitely not", "Get real", "Why don't you ask me later"]
if answer in answer:
    print(random.choice(possibilities))