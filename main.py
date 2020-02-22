#
# File created by Leonardo Cencetti on 2/22/2020
#
import threading

import client
import server


def main():
    t1 = threading.Thread(target=server.start)
    t2 = threading.Thread(target=client.start)
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
