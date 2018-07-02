from _thread import start_new_thread

threadId = 1


def factorial(n):
    global threadId
    if n < 1:   # base case
        print("%s: %d" % ("Thread", threadId))
        threadId += 1
        return 1
    else:
        return_num = n * factorial(n - 1)  # recursive call
        print(str(n) + '! = ' + str(return_num))
        return return_num


start_new_thread(factorial, (8, ))
start_new_thread(factorial, (9, ))

c = input("Waiting for threads to be displayed...\n")
