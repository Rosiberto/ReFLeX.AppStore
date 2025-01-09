from flask import Flask, jsonify, render_template
import docker 
import subprocess 

app = Flask(__name__)

@app.route('/')    
def index(): 
 return render_template("page.html") 

@app.route('/start_container', methods=['GET']) 
def start_container(): 
    try: 
        # Cria uma instância do cliente Docker 
        client = docker.from_env() 

        # Baixa a imagem fiware/orion:latest caso não esteja presente localmente         
        client.images.pull('mysql:latest') 

        # Subindo o container 
        container = client.containers.run( "mysql:latest", 
                                          detach=True, 
                                          ports={"3306/tcp": 3306}, 
                                          environment={"CONTROLLER": "true", 
                                                       "MYSQL_ROOT_PASSWORD":"123",
                                                       "MYSQL_ROOT_HOST":"%"}, 
                                          name="mysql" ) 
        
        #print(container.id +" "+ container.name + " "+container.status)
        
        # Retorna resposta de sucesso 
        return jsonify({ "status": "success", 
                         "container_id": container.id, 
                         "container_name": container.name }) 
    except Exception as e: 
        print(e)
        
        # Caso ocorra erro, retornamos uma resposta de erro 
        return jsonify({ "status": "error", "message": str(e) }) 
    
    
    
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=5000) 