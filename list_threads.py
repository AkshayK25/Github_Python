from _thread import start_new_thread
import time


def numbers():
    my_list = ['1: Akshay', '2: Acadview', '3: 9am', '4: python', '5: MorningBatch']
    for x in my_list:
     print(my_list[0])
     secondstosleep = int(2)

     print('\r')
     print(' sleeping for %d seconds...' % (secondstosleep))
     time.sleep(secondstosleep)
     print(my_list[1])
     secondstosleep = int(4)

     print('\r')
     print(' sleeping for %d seconds...' % (secondstosleep))
     time.sleep(secondstosleep)
     print(my_list[2])
     secondstosleep = int(6)

     print('\r')
     print(' sleeping for %d seconds...' % (secondstosleep))
     time.sleep(secondstosleep)
     print(my_list[3])
     secondstosleep = int(8)

     print('\r')
     print(' sleeping for %d seconds...' % (secondstosleep))
     time.sleep(secondstosleep)
     print(my_list[4])
     secondstosleep = int(10)

     print('\r')
     print(' sleeping for %d seconds...' % (secondstosleep))
     time.sleep(secondstosleep)
     return "hello bhai"


start_new_thread(numbers, ())

c = input("Waiting for threads to be displayed...\n")
