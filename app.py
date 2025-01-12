from flask import Flask, render_template, request
from CybrFunctions import CybrFunctions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form
        cybr = CybrFunctions()
        result = cybr.form_to_json(form_data)

        return f"JSON: {result}"
    
    # If it's a GET request, show the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)