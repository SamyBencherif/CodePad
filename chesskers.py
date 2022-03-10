from codepad import *

def black_cell():
    color(bg+black); color(fg+white); 
                      
def white_cell():
    color(bg+white); color(fg+black); 

art_pack = """
....###.....|.....##.....|....####....|....####....|....####....|
...#####....|...######...|...#....#...|...#.##.#...|...##..##...|
....###.....|..########..|..#......#..|..#.#..#.#..|..#.#.#..#..|
...#####....|..########..|..#......#..|..#.#..#.#..|..#.##...#..|
...#####....|...######...|...#....#...|...#.##.#...|...##.###...|
..#######...|.....##.....|....####....|....####....|....####....|
------------|------------|------------|------------|------------|
...#.#.#....|....###.....|.....#......|.....#......|...#.#.#....|
...#####....|...######...|....###.....|...#####....|...#####....|
...#####....|...####.....|....###.....|....###.....|....###.....|
....###.....|...#####....|.....#......|.....#......|.....#......|
...#####....|...#####....|....###.....|...#####....|...#####....|
...#####....|...#####....|....###.....|..#######...|..#######...|
"""[1:-1]

def subblock(s,x,y,w,h):
    pass

def draw_art(s, x,y):
    px,py = x,y
    for i in s:
        if (i == "\n"):
            px = x;
            py += 1
        elif i=="#":
            pix(px,py,red);
            px += 1
        else:
            px+=1

if __name__ == "__main__":

    while ploop():
        clear()
        W,H = size()
        
        cursor(2,1)

        # draw chesskers board
        cell_height = 6
        cell_width = 12
        for j in range(4):
            # normally is " ", set to something else for debug
            c = " "
            for _ in range(cell_height):
                for i in range(4):
                    white_cell(); write(c*cell_width)
                    black_cell(); write(c*cell_width); 
                nl(); cursor(2,0,True)
            for _ in range(cell_height):
                for i in range(4):
                    black_cell(); write(c*cell_width); 
                    white_cell(); write(c*cell_width)
                nl(); cursor(2,0,True)

        pix(2+cell_width*2,1+cell_height*2,blue);
        draw_art(art_pack, 2, 1)


        # standard prompt
        cursor(0,H-1)
        write(":")

    # ON EXIT
    W,H = size()

    # keep screen output
    cursor(0, H-1)
    
    # OR discard it
    #cursor(0,0)

