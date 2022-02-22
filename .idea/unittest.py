import mouse
import time
import random


while True:
    time.sleep(random.randrange(1, 10))
    mouse.move(2830, 250, absolute=True, duration=2)
    time.sleep(random.randrange(3, 10))
    mouse.move(2730, 450, absolute=True, duration=3)
    time.sleep(random.randrange(5, 10))
    mouse.move(250, 250, absolute=True, duration=1)
    time.sleep(random.randrange(3, 10))
    mouse.move(230, 450, absolute=True, duration=3)
    time.sleep(random.randrange(1, 6))
