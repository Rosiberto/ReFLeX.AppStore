from flask import Flask, render_template, jsonify 
import json 

app = Flask(__name__) 

# Carregar os dados do homelab a partir de um arquivo JSON 
def load_data(): 
    with open("app/homelab_data.json", "r") as f: 
        return json.load(f) 
    
@app.route('/')    
def index(): 
    data = load_data()    

    # Carrega os dados do homelab 
    return render_template("index1.html", services=data) 


@app.route('/api/refresh')
def refresh_data(): 
    # Simula a atualização dos dados (você pode integrar com API's reais) 
    data = load_data() 
    return jsonify({"status": "success", "data": data})
    

if __name__ == '__main__': 
    app.run(debug=True)