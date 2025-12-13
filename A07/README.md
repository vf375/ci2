How to generate the image:

1. Clone from github:
```bash
git clone https://github.com/vf375/ci2.git
```
2. Change directory
```bash
cd ci2/A07
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
5. Generate the an alanine scene using openbabel:
```bash
obabel ala.smi -O ala.pov --gen3D
```
6. Convert the scene into an object:
```bash
python3 Scene_to_Object.py 
```
7. Render the final scene using povray and ala5.pov:
```bash
povray +Iala5.pov +Oala5.png +W800 +H600 +A
```

ala5.png wil be generated as a result.
