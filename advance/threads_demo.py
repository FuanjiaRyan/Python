from concurrent.futures import thread
from threading import Thread
from time import sleep, time


def download(file_name):
    print("Downloading File...", file_name)
    sleep(0.5)
    print("Downloaded")

if __name__ == '__main__':

    files = ["video.mp4", "Image.png", "data.csv"]
    start = time()
    for f in files:
        download(f)
    end = time()
    print(f" Serial time {end - start:.2f} seconds")

    threads = []

    for f in files:
        t = Thread(target=download, args=(f,))
        threads.append(t)

    start = time()

    for t in threads:
        t.start()

    for t in threads:
        t.join

    end = time()

    print(f" parallel with threads time {end - start:.2f} seconds")

    print("Bye")