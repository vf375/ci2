import sys #so that the script works with an arguments

from bs4 import BeautifulSoup as bs 
dom1 = bs(open(sys.argv[1]).read(), features="lxml-xml") #reads the xtml, the features make it so that an annoying message doesnt pop up

print(str(dom1.find_all('cmpdname')).replace('<cmpdname>','').replace('</cmpdname>, ','\n').replace('</cmpdname>','')[1:-1]) #makes a string out of all cmpdname elements, then deletes unecessary xml bloat and replaces the ends of the element with a line break, 
