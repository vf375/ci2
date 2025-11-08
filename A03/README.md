How to run the script:

1)Clone repository:
git clone <https://github.com/vf375/ci2.git>
cd ci2/A03

2)Create venv in directory:

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

On Windows:
python -m venv venv
venv\Scripts\activate

3)Install requirements:
pip install -r requirements.txt

4)Run the script with the benzidine XML file:
python pubchem_parser.py PubChem_benzidine.xml

What the script does:
takes the xml file as an argument and prints each of its iupacname elements on a separate line


