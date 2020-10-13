import os
import sys
import time

from ttsdemo.settings import MEDIA_ROOT


def clean():
    now = time.time()
    try:
        names = os.listdir(MEDIA_ROOT)
        for name in names:
            path = os.path.join(MEDIA_ROOT, name)
            if not os.path.isfile(path):
                continue
            create_time = os.path.getctime(path)
            if (now - create_time) > 30 * 60:
                os.remove(path)
    except Exception as e:
        print(e)
    


if __name__ == '__main__':
    if len(sys.argv) == 1:
        while True:
            clean()
            time.sleep(30 * 60)

    elif len(sys.argv) == 2 and sys.argv[1] == '1':
        clean()
    else:
        print('Unknown arguments: ', sys.argv[1:])