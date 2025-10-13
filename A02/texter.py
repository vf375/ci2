import sys

class LineCounter:
    def __init__(self, file_name):
        self.file_name = file_name #class with a sigle variable for the target text file

    def run(self): #a method for the LineCounter to run which can be triggered later
        linecount = 0
        sed_linecount = 0

        with open(self.file_name, "r") as f:
            for line in f:
                linecount += 1
                if line.lower().split().count("sed") > 0: #lower solves issue with case. split makes it count the standalone word as opposed to parts of words
                    sed_linecount += 1

        print("Lines:", linecount)
        print("Lines containing sed:", sed_linecount)

if __name__ == "__main__": #checks if not imported
    if len(sys.argv) == 1: #one argument would mean script name only
        print("Invalid input. Proper input: texter.py <file_name.txt>")
    else:
        counter = LineCounter(sys.argv[1]) #uses run method with what is meant to be the target text file
        counter.run()
