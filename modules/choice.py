#It wont return random number. It will return a random object from the given list or tuple

from random import*
list=["ABC","DEF","GHI","KLM"]
for i in range(10):
    print(choice(list))
