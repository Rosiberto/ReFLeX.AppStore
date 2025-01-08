from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Flask
)
from werkzeug.exceptions import abort
import json 


server = Flask(__name__)

# Carregar os dados do homelab a partir de um arquivo JSON 
def load_data(): 
    with open("app/homelab_data.json", "r") as f:       
        return json.load(f) 
    

@server.route('/')
def index():
    data = load_data() 
    print(data)
    return render_template('index.html', services=data)
