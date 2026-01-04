document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM loaded");
    
    const form = document.getElementById('chem-form');
    const input = document.getElementById('smiles-input');
    const loadingDiv = document.getElementById('loading');
    const resultsSection = document.getElementById('results-section');
    const errorDiv = document.getElementById('error-msg');
    
    // Result elements
    const resId = document.getElementById('res-id');
    const resName = document.getElementById('res-name');
    const resMw = document.getElementById('res-mw');
    const resLogp = document.getElementById('res-logp');
    const resImage = document.getElementById('res-image');

    // Ensure processing text is hidden on load
    if(loadingDiv) loadingDiv.classList.add('hidden');

    if (!form) {
        console.error("Critical Error: Form not found!");
        return;
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const smiles = input.value.trim();
        if (!smiles) {
            alert("Please enter a SMILES string");
            return;
        }

        // Reset UI state
        if(resultsSection) resultsSection.classList.add('hidden');
        if(errorDiv) errorDiv.classList.add('hidden');
        if(loadingDiv) loadingDiv.classList.remove('hidden');

        try {
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ smiles: smiles })
            });
            
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Server error occurred');
            }

            // Update Text Data
            resId.textContent = data.chembl_id || "N/A";
            resName.textContent = data.name || "Unknown";
            resMw.textContent = data.molecular_weight || "N/A";
            resLogp.textContent = data.logp || "N/A";
            
            // Update Image
            resImage.src = data.image_url;
            
            // Show results
            if(resultsSection) resultsSection.classList.remove('hidden');
            
        } catch (err) {
            console.error("Error:", err);
            if(errorDiv) {
                errorDiv.textContent = err.message;
                errorDiv.classList.remove('hidden');
            }
        } finally {
            if(loadingDiv) loadingDiv.classList.add('hidden');
        }
    });
});