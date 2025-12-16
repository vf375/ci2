from flask import Flask, render_template, request
from chemistry_api import get_compound_by_smiles


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        smiles = request.form.get('smiles')
        compound = get_compound_by_smiles(smiles)


        if compound:
            return render_template('results.html', compound=compound)
        else:
            return render_template('results.html', error='No compound found.')


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
