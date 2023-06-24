import threading, os


def print_nums(n):
    for i in range(n+1):
        print(f'print_nums: {i} executing in {threading.current_thread().name} with process id {os.getpid()}\n')


def print_squares(n):
    for i in range(n+1):
        print(f'print_squares: {i**2} executing in {threading.current_thread().name} with process id {os.getpid()}\n')


if __name__ == '__main__':
    t1 = threading.Thread(target=print_nums, args=(10,), name='t1')
    t2 = threading.Thread(target=print_squares, args=(10,), name='t2')

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("This is program ending..\n")
