from _thread import start_new_thread
from random import randint
import time


def numbers(n):
    num = n
    for x in range(1, num):
     print(x)
     # Sleep for random time between 1 ~ 3 second
     secondstosleep = randint(1, 5)
     print('\r')
     print(' sleeping for %d seconds...' % (secondstosleep))
     time.sleep(secondstosleep)
    return "hello bhai"


start_new_thread(numbers, (11, ))

c = input("Waiting for threads to be displayed...\n")
