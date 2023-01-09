import sys
import time

def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()
