
start = "0177532"
# n = 10000
n = 10

f = open("number.txt", "w")

for x in range(n):
    # print(int(start)*10000+1000+x)
    number = "0"+str(int(start)*10000+x)
    print(number)
    f.write(number + "\n")


f.close()
