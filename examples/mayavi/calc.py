import sys
import time

import zmq
import numpy

def main():
    if len (sys.argv) == 4:
        try:
            bind_to = sys.argv[1]
            array_size = int(sys.argv[2])
            array_count = int (sys.argv[3])
        except (ValueError, OverflowError), e:
            print 'array-size and array-count must be integers'
            sys.exit (1)
    else:
        print 'usage: calc <bind-to> <array-size> <array-count>'
        print
        print 'Using default parameters:'
        print '$ python calc.py tcp://127.0.0.1:8341 100 1000'
        bind_to = 'tcp://127.0.0.1:8341'
        array_size = 100
        array_count = 1000


    ctx = zmq.Context(1,1)
    s = ctx.create_socket(zmq.PUB)
    s.bind(bind_to)

    print "Sending arrays..."
    for i in range(array_count):
        a = numpy.random.rand(array_size, array_size)
        s.send_pyobj(a)
    print "   Done."

if __name__ == "__main__":
    main()
