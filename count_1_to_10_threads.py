from threading import Thread
import time


def print_numbers_in_range(x, y):
    while x <= y:
        print(x)
        x += 1
        time.sleep(1)

# making threads
t1 = Thread(name='Thread1', target=print_numbers_in_range, args=(1, 10))
t2 = Thread(name='Thread2', target=print_numbers_in_range, args=(1, 10))
t3 = Thread(name='Thread3', target=print_numbers_in_range, args=(1, 10))
t4 = Thread(name='Thread4', target=print_numbers_in_range, args=(1, 10))
t5 = Thread(name='Thread5', target=print_numbers_in_range, args=(1, 10))
t6 = Thread(name='Thread6', target=print_numbers_in_range, args=(1, 10))
t7 = Thread(name='Thread7', target=print_numbers_in_range, args=(1, 10))
t8 = Thread(name='Thread8', target=print_numbers_in_range, args=(1, 10))
t9 = Thread(name='Thread9', target=print_numbers_in_range, args=(1, 10))
t10 = Thread(name='Thread10', target=print_numbers_in_range, args=(1, 10))
# running threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
# waiting for the threads to end
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

print('All threads done')
