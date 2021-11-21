from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from users import users
from flask_mysqldb import MySQL
from encriptacion import encriptar
import os

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

try:
    app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
    app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
    app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
    app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
except:
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'users_api'


mysql = MySQL(app)


#Testing Route
@app.route('/', methods=['GET'])
def getDefault():
    return jsonify({'response': 'Hello to my users api!'})


#Get Users Routes
@app.route('/users')
def getUsers():
    # return jsonify(user)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users')
    data = cur.fetchall()
    res = []
    for i in data:
        user_n = {
            "id": i[0],
            "nombre": i[1],
            "apellidos": i[2],
            "dni": i[3],
            "email": i[4],
            "direccion": i[5],
            "telefono": i[6]
            }
        res.append(user_n)

    return jsonify(res)



#Get Workers Routes
@app.route('/workers')
def getWorkers():
    # return jsonify(user)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN workers where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        user_n = {
            "id": i[0],
            "nombre": i[1],
            "apellidos": i[2],
            "dni": i[3],
            "email": i[4],
            "direccion": i[5],
            "telefono": i[6],
            "worker_id": i[7],
            "pass": i[8],
            "user_id": i[9],
            "tipo": i[10]
            }
        res.append(user_n)

    return jsonify(res)



#Get External Workers Routes
@app.route('/externalWorkers')
def getExternalWorkers():
    # return jsonify(user)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN externalworkers where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        print(i)
        user_n = {
            "id": i[0],
            "nombre": i[1],
            "apellidos": i[2],
            "dni": i[3],
            "email": i[4],
            "direccion": i[5],
            "telefono": i[6],
            "ext_worker_id": i[7],
            "user_id": i[8],
            "ocupacion": i[9]
            }
        res.append(user_n)

    return jsonify(res)



#Get Clients Routes
@app.route('/clients')
def getClients():
    # return jsonify(user)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN clients where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        print(i)
        user_n = {
            "id": i[0],
            "nombre": i[1],
            "apellidos": i[2],
            "dni": i[3],
            "email": i[4],
            "direccion": i[5],
            "telefono": i[6],
            "ext_worker_id": i[7],
            "user_id": i[8],
            "clientePotencial": i[9]
            }
        res.append(user_n)

    return jsonify(res)



#Get economic managers Routes
@app.route('/gestores')
def getGestores():
    # return jsonify(user)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN gestor where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        user_n = {
            "id": i[0],
            "nombre": i[1],
            "apellidos": i[2],
            "dni": i[3],
            "email": i[4],
            "direccion": i[5],
            "telefono": i[6],
            "worker_id": i[7],
            "user_id": i[8]
            }
        res.append(user_n)

    return jsonify(res)



#Returns a worker by DNI
@app.route('/workers/<string:user_dni>')
def getWorkerByDNI(user_dni):
    cur = mysql.connection.cursor()
    cur.execute('select * from users join workers where id_persona = user_id')
    data = cur.fetchall()
    js = []

    for i in data:
        user_n = {
            "id": i[0],
            "nombre": i[1],
            "apellidos": i[2],
            "dni": i[3],
            "email": i[4],
            "direccion": i[5],
            "telefono": i[6],
            "worker_id": i[7],
            "pass": i[8],
            "user_id": i[9],
            "tipo": i[10]
            }
        js.append(user_n)

    for i in js:
        if i['dni'] == user_dni:
            return i
    return jsonify({'message': 'Usuario no encontrado'})




#Create Workers Routes
@app.route('/addWorkers', methods=['POST'])
def addWorkers():
    #mysql data
    passw = request.json['pass']
    dni = request.json['dni']
    tipo = request.json['tipo']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users")
    data = cur.fetchall()
    user_id = 0
    for i in data:
        if i[3] == dni:
            user_id = i[0]

    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('INSERT INTO workers (pass, user_id, tipo) VALUES (%s, %s, %s)', (passw, user_id, tipo))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Create External workers Routes
@app.route('/addExternalWorkers', methods=['POST'])
def addExternalWorkers():
    #mysql data
    dni = request.json['dni']
    ocupacion = request.json['ocupacion']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users")
    data = cur.fetchall()
    user_id = 0
    for i in data:
        if i[3] == dni:
            user_id = i[0]

    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('INSERT INTO externalworkers (user_id, ocupacion) VALUES (%s, %s)', (user_id, ocupacion))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador Externo insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Create Clients Routes
@app.route('/addClients', methods=['POST'])
def addClients():
    #mysql data
    dni = request.json['dni']
    clientePotencial = request.json['clientePotencial']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users")
    data = cur.fetchall()
    user_id = 0
    for i in data:
        if i[3] == dni:
            user_id = i[0]

    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('INSERT INTO clients (user_id, clientePotencial) VALUES (%s, %s)', (user_id, clientePotencial))
        mysql.connection.commit()
        return jsonify({'message': "Cliente insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Create Manager Routes
@app.route('/addManager', methods=['POST'])
def addManager():
    #mysql data
    dni = request.json['dni']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users")
    data = cur.fetchall()
    user_id = 0
    for i in data:
        if i[3] == dni:
            user_id = i[0]


    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('INSERT INTO gestor (user_id) VALUES (%s)', (user_id))
        mysql.connection.commit()
        return jsonify({'message': "Gestor insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Create Users Routes
@app.route('/addUsers', methods=['POST'])
def addUsers():
    #mysql data
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    dni = request.json['dni']
    email = request.json['email']
    direccion = request.json['direccion']
    telefono = request.json['telefono']

    if request.headers['Authorization'] == "0i234c6c89":
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (nombre, apellidos, dni, email, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellidos, dni, email, direccion, telefono))
        mysql.connection.commit()
        return jsonify({'message': "Usuario insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Edit Users Routes
@app.route('/editUser/<string:user_dni>', methods=['POST'])
def editUsers(user_dni):
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    email = request.json['email']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append(i)
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('UPDATE users SET nombre = %s, apellidos = %s, dni = %s, email = %s, direccion = %s, telefono = %s where id_persona = %s', (nombre, apellidos, user_dni, email, direccion, telefono, res[0][0]))
        mysql.connection.commit()
        return jsonify({'message': "Usuario editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})


#Edit Workers Routes
@app.route('/editWorker/<string:user_dni>', methods=['POST'])
def editWorkers(user_dni):
    passswd = request.json['pass']
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append(i)
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('UPDATE workers SET pass = %s where user_id = %s', (passswd, res[0][0]))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Edit External Worker Routes
@app.route('/editExternalWorker/<string:user_dni>', methods=['POST'])
def editExternalWorker(user_dni):
    ocupacion = request.json['ocupacion']
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append(i)
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('UPDATE externalworkers SET pass = %s where user_id = %s', (ocupacion, res[0][0]))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador Externo editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Edit Client Routes
@app.route('/editClient/<string:user_dni>', methods=['POST'])
def editClient(user_dni):
    clientePotencial = request.json['clientePotencial']
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append(i)
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('UPDATE clients SET pass = %s where user_id = %s', (clientePotencial, res[0][0]))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador Externo editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete user from de DB
@app.route('/deleteUser/<string:user_dni>', methods=['DELETE'])
def deleteUser(user_dni):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append(i)

    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('DELETE from workers where user_id = {}'.format(res[0][0]))
        mysql.connection.commit()
        cur.execute('DELETE from users where id_persona = {}'.format(res[0][0]))
        mysql.connection.commit()
        return jsonify({"message": "Usuario borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete worker from de DB
@app.route('/deleteWorker/<string:user_dni>', methods=['DELETE'])
def deleteWorker(user_dni):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN workers where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append()
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('DELETE from workers where id = {}'.format(res[0][0]))
        mysql.connection.commit()
        return jsonify({"message": "Trabajador borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete external worker from de DB
@app.route('/deleteExternalWorker/<string:user_dni>', methods=['DELETE'])
def deleteExternalWorker(user_dni):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN externalworkers where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append()
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('DELETE from externalworkers where id = {}'.format(res[0][0]))
        mysql.connection.commit()
        return jsonify({"message": "Trabajador Externo borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete Client from de DB
@app.route('/deleteClient/<string:user_dni>', methods=['DELETE'])
def deleteClient(user_dni):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN clients where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append()
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('DELETE from clients where id = {}'.format(res[0][0]))
        mysql.connection.commit()
        return jsonify({"message": "Cliente borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete manager from de DB
@app.route('/deleteManager/<string:user_dni>', methods=['DELETE'])
def deleteManager(user_dni):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from users JOIN gestor where id_persona = user_id')
    data = cur.fetchall()
    res = []
    for i in data:
        if i[3] == user_dni:
            res.append()
    
    if request.headers['Authorization'] == "0i234c6c89":
        cur.execute('DELETE from gestor where id = {}'.format(res[0][0]))
        mysql.connection.commit()
        return jsonify({"message": "Gestor borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Login as admin
@app.route('/login', methods=['POST'])
def login():
    mail = request.json['mail']
    password = request.json['password']
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `users` JOIN `workers` WHERE id_persona LIKE user_id AND email LIKE "{}"'.format(mail))
    data = cur.fetchall()
    if len(data) != 0:
        if data[0][10] == "Administrador" and data[0][8] == password:
            return jsonify({ "message": "Login accepted", "status": 200, "accepted": True })
        else:
            return jsonify({ "message": "User denied", "status": 200, "accepted": False })
    else:
        return jsonify({ "message": "User not found", "status": 404, "accepted": False })



if __name__ == '__main__':
    app.run(debug=True, port=8000)