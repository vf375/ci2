import os

# Get the folder where this script is located to avoid FileNotFoundError
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'ala.pov')

# Read the original file content
with open(file_path, 'r') as f:
    lines = f.readlines()

new_lines = []
skip_block = False
brace_count = 0

for line in lines:
    stripped = line.strip()
    
    # 1. LOGIC TO DELETE SCENE ELEMENTS (Camera, Light, Background)
    if skip_block:
        # We are inside a block to be deleted.
        # We still need to count braces to know when the block ends.
        brace_count += line.count('{')
        brace_count -= line.count('}')
        if brace_count <= 0:
            skip_block = False
            brace_count = 0
        # Do NOT append the line. Just continue to the next one.
        continue
    
    # Identify start of Camera, Background, or Light Source blocks
    if stripped.startswith('camera') or \
       stripped.startswith('background') or \
       stripped.startswith('light_source'):
        
        # Check if the block opens and closes on the same line
        current_braces = line.count('{') - line.count('}')
        if current_braces > 0:
            skip_block = True
            brace_count = current_braces
        
        # Do NOT append this line.
        continue

    # 2. LOGIC TO DELETE RENDERING DIRECTIVES
    # Remove #render text
    if stripped.startswith('#render'):
        continue

    # Remove the immediate instantiation of 'mol_0'
    if stripped == 'mol_0':
        continue

    # Keep all other lines (atoms, bonds, definitions)
    new_lines.append(line)

# 3. ADD THE NEW OBJECT DECLARATION
new_lines.append('\n// Declaring the molecule object for external use\n')
new_lines.append('#declare Alanine_Mol = object { mol_0 }\n')

# Write the modified content back to the file
with open(file_path, 'w') as f:
    f.writelines(new_lines)

print(f"Success! {file_path} has been cleaned and converted to an object file.")