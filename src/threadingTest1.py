import threading
from time import sleep
from datetime import datetime

loops = [4, 2]
date_time_format = '%Y-%M-%d %H:%M:%S'


def date_time_str():
    return datetime.now().strftime(date_time_format)
    # return datetime.strftime(date_time, date_time_format)


def loop(n_loop, n_sec):
    print('线程(', n_loop, ')开始执行：', date_time_str(), '先休眠(', n_sec, ')秒')
    sleep(n_sec)
    print('线程(', n_loop, ')休眠结束于：', date_time_str())


def main():
    print('---所有线程开始执行:', date_time_str())
    threads = []
    n_loops = range(len(loops))
    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in n_loops:
        threads[i].start()
        sleep(0.01)

    for i in n_loops:
        threads[i].join()

    print('---所有线程执行完成于:', date_time_str())


if __name__ == '__main__':
    main()
