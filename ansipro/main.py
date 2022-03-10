import readline
import subprocess

def write(x):
  print(x, end="");

def escB():
  write("\u001b[");

def call(x):
  escB(); write(x);

def clear():
  call("2J")

def cursor(x,y):
  call("H");
  if x:
    call(f"{x}C");
  if y:
    call(f"{y}B");
 
BLACK = 0; RED = 1; GREEN = 2; YELLOW = 3; BLUE = 4; MAGENTA = 5
CYAN = 6; WHITE = 7;

def fg(c):
  call(f"3{c}m");

def bg(c):
  call(f"4{c}m");

def reset():
  call("0m");

def pix(x,y,c):
  cursor(1+x,1+y);
  bg(c); fg(c);
  write("*");

def window(x=1,y=1,w=20,h=20, col=BLUE, fill=False):
  reset();
  cursor(x,y)

  # top of window
  if h>0:
    bg(col)
    write(" "*w)
    reset(); 

  for i in range(h-2):
    cursor(x,y+1+i)
    # left side
    bg(col); write(" ");
    if fill:
      W = int(subprocess.check_output("tput cols", shell=1))
      bg(BLACK); write(" "*(W-2));
    reset();
    cursor(x+w-1,y+1+i)
    # right side
    bg(col); write(" ");
    reset(); 

  # bottom of window
  if h>1:
    bg(col)
    cursor(x,y+h-1)
    write(" "*w)
  reset(); write("\n");
  
  reset()
  print()

API = {
  "pix": pix,
  "BLACK": BLACK, "RED": RED, "GREEN": GREEN, "YELLOW": YELLOW, 
  "BLUE": BLUE, "MAGENTA": MAGENTA, "CYAN": CYAN, "WHITE": WHITE,
}

def redraw(clearScreen=False):
  W = int(subprocess.check_output("tput cols", shell=1))
  H = int(subprocess.check_output("tput lines", shell=1))
  window(0,0,W,int(H/2),fill=clearScreen)
  window(0,int(H/2),W,1,col=GREEN)

if __name__ == "__main__":
  clear()
  redraw(1)
  W = int(subprocess.check_output("tput cols", shell=1))
  H = int(subprocess.check_output("tput lines", shell=1))
  i=int(H/2)+1
  hist = ""
  while True:
    cursor(0,i)
    cmd = input(">>> ")
    if '=' in cmd:
      API[cmd.split('=')[0].strip()] = eval(cmd.split('=')[1])
    else:
      exec(cmd or "None", API)
    reset()
    redraw()
    i+=1
