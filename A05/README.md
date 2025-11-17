How to run the script:

1) clone from github:
git clone https://github.com/vf375/ci2.git

2) change directory
cd ci2/A05

3) Create venv in directory:

On macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

On Windows:
python -m venv venv
venv\Scripts\activate

4) Install requirements using pip:

pip install -r requirements.txt

5) Run the script:

python3 cdxml2sdf.py "*.cdxml" <output_name.sdf> #either this for all .cdxml files in directory

python3 cdxml2sdf.py <molecule.cdxml> <output_name.sdf> #or this for specific arguments
#output_name.sdf can be omitted

What the script does:
Converts all valid cdxml files in directory into mol format, and then creates 1 sdf file out of those, which it saves
in directory. Default output name is cdxml2sdf.sdf, and it overwrites any orginal file. It also creates Morgan fingerprints (radius 2, size 2048) for all the mol files and searches for the combination with the highest Tanimoto coefficient. The result gets printed as output.