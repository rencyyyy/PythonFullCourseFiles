# Multiprocessing - running tasks in parallel on different cpu cores, bypasses GIL used for threading

# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound task (waiting around)

from multiprocessing import Process, cpu_count
import time
def counter(num):
    count = 0
    while count < num:
        count += 1
def main():
    print(cpu_count()) # To check count of cores of my cpu
    # NOTE: I dont know why but, in my case the 2 processed is much slower than single processed.

    # 1 SLOW PROCESSED
    # a = Process(target=counter, args=(1000000000,))
    # a.start()
    # a.join()
    # Processed finished in 65784.9760128 seconds

    # 2 PROCESSED - shorter
    # a = Process(target=counter, args=(500000000,))
    # b = Process(target=counter, args=(500000000,))
    #
    # a.start()
    # b.start()
    #
    # a.join()
    # b.join()
    # Processed finished in 65960.6042711 seconds

    # 4 PROCESSED
    # a = Process(target=counter, args=(250000000,))
    # b = Process(target=counter, args=(250000000,))
    # c = Process(target=counter, args=(250000000,))
    # d = Process(target=counter, args=(250000000,))
    #
    # a.start()
    # b.start()
    # c.start()
    # d.start()
    #
    # a.join()
    # b.join()
    # c.join()
    # d.join()
    # Processed finished in 66275.3416568 seconds

    # 8 PROCESSED
    # a = Process(target=counter, args=(125000000,))
    # b = Process(target=counter, args=(125000000,))
    # c = Process(target=counter, args=(125000000,))
    # d = Process(target=counter, args=(125000000,))
    # e = Process(target=counter, args=(125000000,))
    # f = Process(target=counter, args=(125000000,))
    # g = Process(target=counter, args=(125000000,))
    # h = Process(target=counter, args=(125000000,))
    #
    # a.start()
    # b.start()
    # c.start()
    # d.start()
    # e.start()
    # f.start()
    # g.start()
    # h.start()
    #
    # a.join()
    # b.join()
    # c.join()
    # d.join()
    # e.join()
    # f.join()
    # g.join()
    # h.join()
    # Processed finished in 66760.2140989 seconds

    # 16 PROCESSED
    a = Process(target=counter, args=(62500000,))
    b = Process(target=counter, args=(62500000,))
    c = Process(target=counter, args=(62500000,))
    d = Process(target=counter, args=(62500000,))
    e = Process(target=counter, args=(62500000,))
    f = Process(target=counter, args=(62500000,))
    g = Process(target=counter, args=(62500000,))
    h = Process(target=counter, args=(62500000,))
    i = Process(target=counter, args=(62500000,))
    j = Process(target=counter, args=(62500000,))
    k = Process(target=counter, args=(62500000,))
    l = Process(target=counter, args=(62500000,))
    m = Process(target=counter, args=(62500000,))
    n = Process(target=counter, args=(62500000,))
    o = Process(target=counter, args=(62500000,))
    p = Process(target=counter, args=(62500000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()
    m.start()
    n.start()
    o.start()
    p.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()
    m.join()
    n.join()
    o.join()
    p.join()
    # Processed finished in 67133.2269697 seconds
    print(f"Processed finished in {time.perf_counter()} seconds")

if __name__ == '__main__':
    main()