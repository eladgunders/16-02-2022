from threading import Thread, Event
import random


def solve_me(a, b):
    result = None
    print(f'{a} + {b} =')
    while result != a + b:
        try:
            result = int(input('Please enter the solution of this exercise: '))
            if a + b != result:
                print('Wrong answer, try again.')
        except ValueError:
            print('Must enter an integer, try again.')
    print('nice')


def get_random_pairs_of_numbers(a, b, counter):
    random_numbers_ls = []
    for i in range(counter):
        x = random.randint(a, b)
        y = random.randint(a, b)
        random_numbers_ls.append((x, y))
    return random_numbers_ls


def math_test_for_user(e):
    random_numbers_ls = get_random_pairs_of_numbers(1, 100, 3)
    for pair in random_numbers_ls:
        solve_me(pair[0], pair[1])
    e.set()


def wait_for_correct_answers(e):
    e.wait()
    print('Well Done m8!')


if __name__ == '__main__':

    e = Event()
    t1 = Thread(name='Thread1', target=math_test_for_user, args=(e, ))
    t2 = Thread(name='Thread2', target=wait_for_correct_answers, args=(e, ))
    t1.start()
    t2.start()
