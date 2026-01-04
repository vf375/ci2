How to use the application:

1. Clone from github:
```bash
git clone https://github.com/vf375/ci2.git
```
2. Change directory
```bash
cd ci2/A09
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
Also make sure you have openbabel and povray installed.
5. Run the app:
```bash
python app.py
```
6. Open browser at the suggested URL
7. Enter canonical smiles into the search field

The returned page will contain the SMILES, Chembl ID, logarithm of partition coefficient, molecular weight, name and image of the given compound. 
