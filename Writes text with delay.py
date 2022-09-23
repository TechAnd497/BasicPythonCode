import sys, time

message = "Hello there, I am ?? and this is my code. You can use this code to create a typewriter with delay. I used it for a video as the intro. Use as you want."

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
