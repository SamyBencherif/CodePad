from codepad import *

if __name__ == "__main__":

    while ploop():
        clear()
        W,H = size()

        # standard bottom of screen input
        cursor(0,H-1)
        write(":")

    # ON EXIT
    W,H = size()

    # keep screen output
    cursor(0, H-1)
    
    # OR discard it
    #cursor(0,0)

