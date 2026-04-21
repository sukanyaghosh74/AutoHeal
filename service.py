import time
import random

print("Service started")

while True:
    time.sleep(3)
    if random.randint(1,10) == 5:
        print("Simulating crash...")
        exit(1)
    print("Service running...")
