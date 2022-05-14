# f = open("number.txt", "r")

with open('number.txt') as f:
    for line in f:
        print(line)
