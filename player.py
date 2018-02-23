import signal
import subprocess
import threading
import time
import atexit
import os

URL = None
CHANGED = False
lock = threading.Lock()
process = None

def kill_child():
    if process:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)

def tick():
    global CHANGED, process
    while True:
        lock.acquire()
        if CHANGED:
            print(URL)
            kill_child()
            process = subprocess.Popen(['mpsyt','--debug'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, preexec_fn=os.setsid)
            process.stdin.write('set player mpv\n'.encode())
            process.stdin.write('playurl {}\n'.format(URL).encode())
            process.stdin.write('repeat 1\n'.encode())
            process.stdin.flush()
            CHANGED = False
        lock.release()
        time.sleep(1)


def play(url):
    global URL, CHANGED
    lock.acquire()
    URL = url
    CHANGED = True
    lock.release()

thread = threading.Thread(target=tick)
thread.start()
#play('https://www.youtube.com/watch?v=4zLfCnGVeL4')
#time.sleep(5)
atexit.register(kill_child)
