import sys

from bs4 import BeautifulSoup as bs
dom1 = bs(open(sys.argv[1]).read(), features="lxml-xml")

print(str(dom1.find_all('cmpdname')).replace('<cmpdname>','').replace('</cmpdname>, ','\n').replace('</cmpdname>','')[1:-1])
