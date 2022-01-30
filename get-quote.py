import random

def primary():
	print(" ")

f = open("quotes.txt")
quotes = f.readlines()
f.close()
last = len(quotes)-1
rnd = random.randint(0, last)
##for loop in range(0, rnd):
print(quotes[rnd])

if __name__== "__main__":
  primary()
