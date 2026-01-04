import os
import subprocess
import time
from flask import Flask, render_template, request, jsonify, url_for
from chemistry_api import search_molecule

app = Flask(__name__)

# Ensure the static folder exists
STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')
if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)

# Get the absolute path to the project folder (where app.py and .inc file are)
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

def generate_3d_image(smiles, output_filename):
    sdf_path = os.path.join(STATIC_FOLDER, f"{output_filename}.sdf")
    pov_path = os.path.join(STATIC_FOLDER, f"{output_filename}.pov")
    img_path = os.path.join(STATIC_FOLDER, f"{output_filename}.png")
    
    # --- STEP 1: SMILES -> SDF (Calculate 3D structure) ---
    try:
        subprocess.run(
            ['obabel', '-ismi', '-', '-osdf', '-O', sdf_path, '--gen3d', '-h'], 
            input=smiles, text=True, check=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print(f"Obabel Step 1 Failed: {e.stderr}")
        return None

    # --- STEP 2: SDF -> POV (Generate Scene) ---
    try:
        subprocess.run(
            ['obabel', '-isdf', sdf_path, '-O', pov_path],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print(f"Obabel Step 2 Failed: {e.stderr}")
        return None

    # --- STEP 3: RENDER (POV -> PNG) ---
    # We add the +L flag to tell POV-Ray to look in the current project folder
    # for include files (like povray.inc or babel_povray3.inc).
    try:
        subprocess.run(
            [
                'povray', 
                f'+I{pov_path}', 
                f'+O{img_path}', 
                '+W500', '+H500', 
                '+Q9', '+A', '+FN', '+UA', '-D',
                f'+L{PROJECT_FOLDER}'  # <--- CRITICAL FIX: Look in project folder
            ],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        # Capture the POV-Ray error to show the user if needed
        error_msg = e.stderr.decode('utf-8', errors='ignore')
        print(f"POV-Ray Failed: {error_msg}")
        raise Exception(f"POV-Ray Render Error: {error_msg}")

    # Cleanup temporary files (SDF and POV)
    try:
        if os.path.exists(sdf_path): os.remove(sdf_path)
        # Optional: Remove POV file if you don't need to debug it
        # if os.path.exists(pov_path): os.remove(pov_path)
    except: pass
        
    return f"{output_filename}.png"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def api_search():
    data = request.get_json()
    smiles = data.get('smiles', '').strip()

    if not smiles:
        return jsonify({'error': 'Please enter a valid SMILES string.'}), 400

    chem_data = search_molecule(smiles)
    if not chem_data:
        return jsonify({'error': 'No compound found in ChEMBL.'}), 404

    filename_base = f"mol_{int(time.time())}"
    
    try:
        image_filename = generate_3d_image(smiles, filename_base)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    if not image_filename:
        return jsonify({'error': 'Unknown error generating 3D image.'}), 500

    chem_data['image_url'] = url_for('static', filename=image_filename)
    chem_data['smiles_used'] = smiles
    
    return jsonify(chem_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)