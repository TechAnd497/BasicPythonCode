# BasicPythonCode
Here are some basic Python code I have created. I stuggle with remmbering how to code, so wanted to practice with writing up these easy programs/codes. This code allows you to have the affect of the typewriter where it types/prints one letter at a time on the screen. This was use for me in my intro of a video I made. 


import sys, time  - Gets your systems time

message = "Hello there, I am ?? and this is my code. You can use this code to create a typewriter with delay. I used it for a video as the intro. Use as you want." -This is where you write the text you want the program to display on the screen, one letter at a time.

for char in message:  - slpits the type into single characters
    sys.stdout.write(char) -type outs the each letter
    sys.stdout.flush() 
    time.sleep(0.1) - the delay the program will use to display the next letter. 
