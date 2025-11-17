#!/usr/bin/env python3
import sys
import os
import glob
from itertools import combinations

from openbabel import openbabel as ob

from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit import RDLogger
from rdkit.DataStructs import TanimotoSimilarity

# Silence RDKit warnings
RDLogger.DisableLog("rdApp.error")


def obabel_cdxml_to_molblocks(filename):
    """
    Convert CDXML → list of MOL blocks.
    Skip file if OpenBabel cannot read it.
    """
    conv = ob.OBConversion()
    if not conv.SetInFormat("cdxml"):
        return []

    conv.SetOutFormat("mol")

    mol = ob.OBMol()
    molblocks = []

    # Try reading first molecule
    if not conv.ReadFile(mol, filename):
        # Completely unreadable CDXML
        return []

    molblocks.append(conv.WriteString(mol))

    # Read subsequent molecules (if any)
    while conv.Read(mol):
        molblocks.append(conv.WriteString(mol))

    return molblocks


def find_output_sdf(args):
    """Select output SDF file per assignment rules."""
    for a in args:
        if a.lower().endswith(".sdf") and not os.path.exists(a):
            return a
    return "cdxml2sdf.sdf"


def main():
    if len(sys.argv) < 2:
        print("Usage: cdxml2sdf.py '*.cdxml' [output.sdf]")
        sys.exit(1)

    input_files = []
    for arg in sys.argv[1:]:
        input_files.extend(glob.glob(arg))

    cdxml_files = [f for f in input_files if f.lower().endswith(".cdxml")]
    if not cdxml_files:
        print("No CDXML files found.")
        sys.exit(1)

    output_sdf = find_output_sdf(sys.argv[1:])
    writer = Chem.SDWriter(output_sdf)

    mols = []
    names = []

    # ---- Load each CDXML file ----
    for f in cdxml_files:
        molblocks = obabel_cdxml_to_molblocks(f)
        if not molblocks:
            print(f"WARNING: OpenBabel could not parse {f} — skipped")
            continue

        for i, mb in enumerate(molblocks):
            mol = Chem.MolFromMolBlock(mb, sanitize=True)
            if mol:
                name = os.path.basename(f)
                if len(molblocks) > 1:
                    name += f"#{i+1}"

                mol.SetProp("_Name", name)
                mols.append(mol)
                names.append(name)
                writer.write(mol)
            else:
                print(f"WARNING: RDKit failed to load molecule in {f}")

    writer.close()
    print(f"Written {len(mols)} molecules → {output_sdf}")

    if not mols:
        print("No valid molecules loaded.")
        sys.exit(1)

    # ---- Compute fingerprints ----
    fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
    fps = [fpgen.GetFingerprint(m) for m in mols]

    # ---- Find most similar pair ----
    best_pair = None
    best_sim = -1.0

    for i, j in combinations(range(len(mols)), 2):
        sim = TanimotoSimilarity(fps[i], fps[j])
        if sim > best_sim:
            best_sim = sim
            best_pair = (names[i], names[j])

    print(f"Most similar pair: {best_pair[0]},{best_pair[1]}. Similarity: {best_sim:.4f}")


if __name__ == "__main__":
    main()
