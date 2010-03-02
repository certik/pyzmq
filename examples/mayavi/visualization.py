import sys
import time

import zmq
import numpy

def main():
    if len (sys.argv) == 2:
        connect_to = sys.argv[1]
    else:
        print 'usage: visualization <connect_to>'
        print
        print 'Using default parameters:'
        print '$ python visualization.py tcp://127.0.0.1:8341'
        connect_to = 'tcp://127.0.0.1:8341'


    ctx = zmq.Context(1,1)
    s = ctx.create_socket(zmq.SUB)
    print "Connecting..."
    s.connect(connect_to)
    print "   Done."
    s.setsockopt(zmq.SUBSCRIBE,'')

    start = time.clock()

    print "Receiving arrays..."
    array_count = 1000
    for i in range(array_count):
        a = None
        while a is None:
            a = s.recv_pyobj(zmq.NOBLOCK)
        print a
    print "   Done."

    end = time.clock()

    elapsed = (end - start) * 1000000
    if elapsed == 0:
    	elapsed = 1
    throughput = (1000000.0 * float (array_count)) / float (elapsed)
    message_size = a.nbytes
    megabits = float (throughput * message_size * 8) / 1000000

    print "message size: %.0f [B]" % (message_size, )
    print "array count: %.0f" % (array_count, )
    print "mean throughput: %.0f [msg/s]" % (throughput, )
    print "mean throughput: %.3f [Mb/s]" % (megabits, )

    time.sleep(1.0)

if __name__ == "__main__":
    main()
