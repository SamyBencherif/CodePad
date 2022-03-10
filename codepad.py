import subprocess
import readline

def clear():
    """Clear the screen."""
    subprocess.call("clear", shell=1)

def write(c):
    """Write character to cursor location"""
    print(c, end="") 

def call(c):
    """Execute an ANSI escape code"""
    write(f"\u001b[{c}") 

def nl():
    """Reset color and write newline."""
    color(reset)
    write("\n")

brite = 60
fg = 30; bg = 40;
black = 0; red = 1; green = 2;
yellow = 3; blue = 4; magenta = 5;
cyan = 6; white = 7;
reset = 8;
def color(x):
    """Set the foreground text color (FG) or the cell background color (BG).

Parameters are added together. Ex:
color(fg+red+brite)
color(bg+blue)
color(reset)

`brite` serves to expose a lighter version of the original palette, allowing for
16 colors total.

In general the following sums are acceptable:
SCOLOR+MODE+brite
COLOR+MODE
reset

where COLOR is black, red, green, yellow, blue, magenta, cyan, white, or reset
SCOLOR stands for Strict Color, it is the same as COLOR except it excludes reset
MODE is either fg or bg

As a special case reset can be called without a MODE, in which case it will reset
both the fg and the bg. And of course reset cannot be brightened.
    """
    if x == reset:
        call("0m")
    else:
        call(f"{x}m")

def cursor(x,y,delta=False):
    if not delta:
        # home position (0,)
        call('H')
    if x:
        # move right x times
        call(f"{x}C")  
    if y:
        # move down y times
        call(f"{y}B")  

def size():
    return (
        int(subprocess.check_output("tput cols", shell=1)),
        int(subprocess.check_output("tput lines", shell=1))
    )

frameNumber = 0
promptValue = ""
def prompt():
    """Get the prompt input that came before this frame."""
    return promptValue

def ploop():
    """Place this in the condition of the main loop.
Ex:
while ploop():
    write("Prompt value: " + promptValue + " " + frameNumber + "\\n:")

It will provide one prompt per frame and leave the collected input in a variable
called promptValue.
    """
    global promptValue, frameNumber
    try:
        # no input before first frame
        if frameNumber:
            try:
               promptValue = input()
            except KeyboardInterrupt:
                nl()
                exit(0) 
            except EOFError:
                nl()
                exit(0) 
        frameNumber += 1
        return True
    except KeyboardInterrupt:
       return False

def place(x,y,s):
    """
    Puts a string on screen with some special features.

    (1) Parts of the string that go past the screen boundary are clipped
    (2) Newlines stay on the same column without overwritting preceeding content
    (3) Character \\0 can be used as a transparent value
    """
    if x < 0:
        place(0,y,s[-x:])
        return
    if y < 0:
        place(0,0,'\n'.join(s.split('\n')[-y:]))
        return
    W,H = size()
    if x+len(s) >= W:
        place(x,y,s[:W-x])
        return
    if y+len(s.split("\n")) >= H:
        place(0,0,'\n'.join(s.split('\n')[:H-y]))
        return

def pix(x,y,c):
    """Shorthand for cursor(x,y); color(bg+c); write(" ")"""
    cursor(x,y); color(bg+c); write(" "); color(reset)

if __name__ == "__main__":

    while ploop():
        clear()
        W,H = size()

        for i in range(8):
            color(fg+brite+i)
            color(bg+reset)
            write("hello world"); nl()

        cursor(0,1)
        write("Said " + promptValue)
        cursor(0,0)
        write("Say: ")

    # ON EXIT
    W,H = size()

    # keep screen output
    cursor(0, H-1)
    
    # OR discard it
    #cursor(0,0)

