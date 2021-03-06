import sys
import time

import zmq
import numpy

def main():
    if len (sys.argv) != 4:
        print 'usage: publisher <bind-to> <array-size> <array-count>'
        sys.exit (1)

    try:
        bind_to = sys.argv[1]
        array_size = int(sys.argv[2])
        array_count = int (sys.argv[3])
    except (ValueError, OverflowError), e:
        print 'array-size and array-count must be integers'
        sys.exit (1)

    ctx = zmq.Context(1,1)
    s = ctx.create_socket(zmq.PUB)
    s.bind(bind_to)

    # We need to sleep to allow the subscriber time to connect
    time.sleep(1.0)

    for i in range(array_count):
        a = numpy.random.rand(array_size, array_size)
        s.send_pyobj(a)

    time.sleep(1.0)

if __name__ == "__main__":
    main()