import os, random, sys, time


class Universe:

    def __init__(self, w, h):
        self.w, self.h, self.contents, self.generation = w, h, {}, 0
        for y in range(h):
            for x in range(w):
                self.contents[x, y] = 1 if random.randint(0, 4) == 0 else 0
    
    def display(self):
        os.system("cls" if os.name
 == "nt" else "clear")
        a = ""
        for y in range(self.h):
            for x in range(self.w):
                a += [" ", u"\u2588"][self.contents[x, y]]
            a += "\n"
        print(a)
        print("Generation: " + str(self.generation))

    def calculate(self):
        new = {}
        for y in range(self.h):
            for x in range(self.w):
                n = self.countNeighbours(x, y)
                if self.contents[x, y] == 1:
                    if n > 3:
                        new[x, y] = 0
                    elif n < 2:
                        new[x, y] = 0
                    else:
                        new[x, y] = 1
                else:
                    if n == 3:
                        new[x, y] = 1
                    else:
                        new[x, y] = 0
        self.generation += 1
        self.contents = new

    def countNeighbours(self, x, y):
        l = 0
        for b in range(y-1, y+2):
            for a in range(x-1, x+2):
                if (a, b) in self.contents and not (a == x and b == y):
                    l += self.contents[a, b]
        return l


WIDTH = int(sys.argv[1]) if len(sys.argv) > 1 else 119 # Insert default width.
HEIGHT = int(sys.argv[2]) if len(sys.argv) > 2 else 27 # Insert default height.
DELAY = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1 # Insert default delay.

universe = Universe(WIDTH, HEIGHT)

while True:
    universe.calculate()
    universe.display()
    time.sleep(DELAY)