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

4)Run the script with your XML file:
python strankator.py <path/to/yourfile.xml>

What the script does:
takes an xml file as an argument and if said xml file has elements cmpdname, prints each of those in a separate line



