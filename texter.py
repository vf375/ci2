import sys

class LineCounter:
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        linecount = 0
        sed_linecount = 0

        with open(self.file_name, "r") as f:
            for line in f:
                linecount += 1
                if line.lower().split().count("sed") > 0:
                    sed_linecount += 1

        print("Lines:", linecount)
        print("Lines containing 'sed':", sed_linecount)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Invalid input. Proper input: texter.py <file_name.txt>")
    else:
        counter = LineCounter(sys.argv[1])
        counter.run()
