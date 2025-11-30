How to run the script:

1) Clone from github:
git clone https://github.com/vf375/ci2.git

2) Change directory
cd ci2/A06

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

python graph.py

What the script does:
Reads the file graph.csv, creates a default graph using matplotlib and exports the plot as "graph.png"