from multiprocessing import Process, Pipe
import os

def talk(pipe):
    pipe.send('111')
    reply = pipe.recv()
    print('child get: %s' % reply)

if __name__ == '__main__':
    (con1, con2) = Pipe()
    child = Process(target = talk, args = (con1, ))
    child.start()
    print('parent get: %s' % con2.recv())
    con2.send('222')
    child.join()
    # child.terminate()
    print('Process End')
    