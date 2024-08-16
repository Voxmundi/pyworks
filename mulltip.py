import multiprocessing
import time

start = time.perf_counter()


def do_sth():
    print ('sleeping 1 second...')
    time.sleep(1)
    print ('Done sleeping')


# p1 = multiprocessing.Process(target= do_sth)
# p2 = multiprocessing.Process(target= do_sth)

# p1.start()
# p2.start()

# p1.join()
# p2.join()



def over_loop():
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target= do_sth)
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()

over_loop()



finish = time.perf_counter()

print (f"time passed for execution {round(finish-start, 2)} seconds ")