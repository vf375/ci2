How to use the web application:

1. Clone from github:
```bash
git clone https://github.com/vf375/ci2.git
```
2. Change directory
```bash
cd ci2/A08
```
3. Create venv in directory:
On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
4. Install requirements using pip:
```bash
pip install -r requirements.txt
```
5. Run the app:
```bash
python app.py
```
6. Open browser at the suggested URL
7. Enter canonical smiles into the search field

The returned page will contain the name, CHEMBL ID, molecular formula, molecular weight, logarithm of partition coefficient and molecule type of the given molecule.

Example of a search result (text content):
Compound information:
CHEMBL ID: CHEMBL1398657
Name: PHENOLSULFONIC ACID
Molecular formula: C6H6O4S
Molecular weight: 174.18
ALogP: 0.64
Molecule Type: Small molecule