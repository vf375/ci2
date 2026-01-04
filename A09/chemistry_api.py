
from chembl_webresource_client.new_client import new_client

def search_molecule(smiles):
    """
    Searches ChEMBL for a molecule by SMILES.
    Returns a dictionary of data or None if not found.
    """
    try:
        molecule = new_client.molecule
        # Search by exact structure (using smiles)
        res = molecule.filter(molecule_structures__canonical_smiles__flexmatch=smiles).only(['molecule_chembl_id', 'pref_name', 'molecule_properties'])
        
        if not res:
            return None
            
        # Get the first result
        compound = res[0]
        props = compound.get('molecule_properties', {})
        
        return {
            'chembl_id': compound.get('molecule_chembl_id', 'N/A'),
            'name': compound.get('pref_name', 'Unknown'),
            'molecular_weight': props.get('full_mwt', 'N/A'),
            'logp': props.get('cx_logp', 'N/A')
        }
        
    except Exception as e:
        print(f"Error querying ChEMBL: {e}")
        return None