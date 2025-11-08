import sys #so that the script works with an argument

from bs4 import BeautifulSoup as bs 
dom1 = bs(open(sys.argv[1]).read(), features="lxml-xml") #reads the xtml, the features make it so that an annoying message doesnt pop up

if __name__ == "__main__":
  print(str(dom1.find_all('iupacname')).replace('<iupacname>','').replace('</iupacname>, ','\n').replace('</iupacname>','')[1:-1]) 
  #makes a string out of all iupacname elements, then deletes unecessary xml bloat and replaces the ends of the element with a line break, 
