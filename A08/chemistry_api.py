from chembl_webresource_client.new_client import new_client

def get_compound_by_smiles(smiles: str):
    molecule = new_client.molecule
    results = molecule.filter(
        molecule_structures__canonical_smiles=smiles
    )

    if not results:
        return None

    m = results[0]

    return {
        "chembl_id": m.get("molecule_chembl_id"),
        "name": m.get("pref_name"),
        "formula": m.get("molecule_properties", {}).get("full_molformula"),
        "mw": m.get("molecule_properties", {}).get("full_mwt"),
        "alogp": m.get("molecule_properties", {}).get("alogp"),
        "molecule_type": m.get("molecule_type")  # New field
    }
