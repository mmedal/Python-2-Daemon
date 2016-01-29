#!/usr/bin/env python
import sys
import time

from daemon import Daemon


class MyDaemon(Daemon):
    def run(self):
        while True:
            time.sleep(1)


def main():
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "Usage: {0} start|stop|restart".format(sys.argv[0])
        sys.exit(2)


if __name__ == "__main__":
    main()
