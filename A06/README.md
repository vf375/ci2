How to run the script:

1. Clone from github:
```bash
git clone https://github.com/vf375/ci2.git
```

2. Change directory
```bash
cd ci2/A06
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

5. Run the script:
```bash
python graph.py
```

What the script does:
Reads the file graph.csv, creates a default graph using matplotlib and exports the graph as "graph.png"