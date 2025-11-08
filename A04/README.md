How to run the script:

1)Clone from github: git clone <https://github.com/vf375/ci2.git>;
cd ci2/A04

2) Create venv in directory:

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

On Windows:
python -m venv venv
venv\Scripts\activate

3) run the script with city.csv as an argument:
python db.py world/city.csv

What the script does: Counts the number of rows with CountryCode: ALB in a given csv file

 
