from datetime import datetime
from distutils.log import debug
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
from flask_cors.core import try_match
from users import users
from flask_mysqldb import MySQL
from encriptacion import *
from token_generator import *
import os
import sys

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

os.environ['TOKEN'] = token_generator() + ""

try:
    app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
    app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
    app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
    app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
except:
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'tfg'


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
            "telefono": i[6],
            "tabla": "usuario"
            }
        res.append(user_n)

    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado" })



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
            "pass": "",
            "user_id": i[9],
            "tipo": i[10],
            "tabla": "trabajador"
            }
        res.append(user_n)

    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})



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
            "ocupacion": i[9],
            "tabla": "trabajador externo"
            }
        res.append(user_n)

    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})



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
            "clientePotencial": i[9],
            "tabla": "cliente"
            }
        res.append(user_n)

    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})



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
            "user_id": i[8],
            "tabla": "gestor"
            }
        res.append(user_n)

    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})



#Returns a worker by DNI
@app.route('/workers/<string:word>')
def searchWorkers(word):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users JOIN workers WHERE (nombre LIKE '%{words}%' OR apellidos LIKE '%{words}%' OR dni LIKE '%{words}%' ) AND user_id LIKE id_persona".format(words = word))
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
            "pass": "",
            "user_id": i[9],
            "tipo": i[10],
            "tabla": "trabajador"
            }
        res.append(user_n)

    print("\n\n" + str(res) + "\n\n")
    if request.headers['Authorization'] == os.environ['TOKEN']:
        if len(res) > 0:
            return jsonify(res)

        return jsonify({'message': 'Ningún usuario encontrado'})
    else:
        return jsonify({'message': "Acceso denegado"})
    


#Returns a worker by DNI
@app.route('/users/<string:word>')
def searchUsers(word):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE nombre LIKE '%{words}%' OR apellidos LIKE '%{words}%' OR dni LIKE '%{words}%'".format(words = word))
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
            "tabla": "usuario"
            }
        res.append(user_n)

    if request.headers['Authorization'] == os.environ['TOKEN']:
        if len(res) > 0:
            return jsonify(res)

        return jsonify({'message': 'Ningún usuario encontrado'})
    else:
        return jsonify({'message': "Acceso denegado"})
    


#Returns a worker by DNI
@app.route('/user/<string:user_id>', methods=['GET'])
def searchUserid(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id_persona LIKE " + user_id)
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
            "tabla": "usuario"
            }
        res.append(user_n)

    if request.headers['Authorization'] == os.environ['TOKEN']:
        if len(res) > 0:
            return jsonify(res)

        return jsonify({'message': 'Ningún usuario encontrado'})
    else:
        return jsonify({'message': "Acceso denegado"})
    


#Create Workers Routes
@app.route('/addWorkers', methods=['POST'])
def addWorkers():
    #mysql data
    password = request.json['pass']
    dni = request.json['dni']
    tipo = request.json['tipo']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users WHERE dni LIKE '" + dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('INSERT INTO workers (pass, user_id, tipo) VALUES (%s, %s, %s)', (encrypt_password(password), user_id, tipo))
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
    cur.execute("Select * from users WHERE dni LIKE '" + dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]

    if request.headers['Authorization'] == os.environ['TOKEN']:
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
    cur.execute("Select * from users WHERE dni LIKE '" + dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]

    if request.headers['Authorization'] == os.environ['TOKEN']:
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
    cur.execute("Select * from users WHERE dni LIKE '" + dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    print(user_id)


    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('INSERT INTO gestor (user_id) VALUES (' + str(user_id) + ')')
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

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (nombre, apellidos, dni, email, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellidos, dni, email, direccion, telefono))
        mysql.connection.commit()
        return jsonify({'message': "Usuario insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})



@app.route('/editUser/<string:user_dni>', methods=['PUT'])
def editUsers(user_dni):
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    email = request.json['email']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    password = request.json['pass']
    tipo = request.json['tipo']
    ocupacion = request.json['ocupacion'] 
    clientePotencial = request.json['clientePotencial']
    new_dni = request.json['dni']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users WHERE dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('UPDATE users SET nombre = %s, apellidos = %s, dni = %s, email = %s, direccion = %s, telefono = %s where id_persona = %s', (nombre, apellidos, new_dni, email, direccion, telefono, user_id))
        mysql.connection.commit()
        try:
            if password != "":
                cur.execute('UPDATE workers SET pass = %s, tipo = %s where user_id = %s', (encrypt_password(password), tipo, user_id))
            else:
                cur.execute('UPDATE workers SET tipo = %s where user_id = %s', (tipo, user_id))
            mysql.connection.commit()
        except:
            try:
                cur.execute('UPDATE externalworkers SET ocupacion = %s where user_id = %s', (ocupacion, user_id))
                mysql.connection.commit()
            except:
                try:
                    cur.execute('UPDATE clients SET clientePotencial = %s where user_id = %s', (clientePotencial, user_id))
                    mysql.connection.commit()
                except:
                    pass
        return jsonify({'message': "Usuario editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})


#Edit Workers Routes
@app.route('/editWorker/<string:user_dni>', methods=['PUT'])
def editWorkers(user_dni):
    password = request.json['pass']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users WHERE dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        if password != "":
            cur.execute('UPDATE workers SET pass = %s where user_id = %s', (encrypt_password(password), user_id))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Edit External Worker Routes
@app.route('/editExternalWorker/<string:user_dni>', methods=['PUT'])
def editExternalWorker(user_dni):
    ocupacion = request.json['ocupacion']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users WHERE dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('UPDATE externalworkers SET pass = %s where user_id = %s', (ocupacion, user_id))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador Externo editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Edit Client Routes
@app.route('/editClient/<string:user_dni>', methods=['PUT'])
def editClient(user_dni):
    clientePotencial = request.json['clientePotencial']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users WHERE dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('UPDATE clients SET pass = %s where user_id = %s', (clientePotencial, user_id))
        mysql.connection.commit()
        return jsonify({'message': "Trabajador Externo editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete user from de DB
@app.route('/deleteUser/<string:user_dni>', methods=['DELETE'])
def deleteUser(user_dni):
    cur = mysql.connection.cursor()
    cur.execute("Select * from users WHERE dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from clients where user_id = {}'.format(user_id))
        mysql.connection.commit()
        cur.execute('DELETE from gestor where user_id = {}'.format(user_id))
        mysql.connection.commit()
        cur.execute('DELETE from externalworkers where user_id = {}'.format(user_id))
        mysql.connection.commit()
        cur.execute('DELETE from workers where user_id = {}'.format(user_id))
        mysql.connection.commit()
        cur.execute('DELETE from users where id_persona = {}'.format(user_id))
        mysql.connection.commit()
        return jsonify({"message": "Usuario borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete worker from de DB
@app.route('/deleteWorker/<string:user_dni>', methods=['DELETE'])
def deleteWorker(user_dni):
    cur = mysql.connection.cursor()
    cur.execute("Select * from users JOIN workers WHERE id_persona = user_id and dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from workers where user_id = {}'.format(user_id))
        mysql.connection.commit()
        return jsonify({"message": "Trabajador borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete external worker from de DB
@app.route('/deleteExternalWorker/<string:user_dni>', methods=['DELETE'])
def deleteExternalWorker(user_dni):
    cur = mysql.connection.cursor()
    cur.execute("Select * from users JOIN externalworkers WHERE id_persona = user_id and dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from externalworkers where user_id = {}'.format(user_id))
        mysql.connection.commit()
        return jsonify({"message": "Trabajador Externo borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete Client from de DB
@app.route('/deleteClient/<string:user_dni>', methods=['DELETE'])
def deleteClient(user_dni):
    cur = mysql.connection.cursor()
    cur.execute("Select * from users JOIN clients WHERE id_persona = user_id and dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from clients where user_id = {}'.format(user_id))
        mysql.connection.commit()
        return jsonify({"message": "Cliente borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Delete manager from de DB
@app.route('/deleteManager/<string:user_dni>', methods=['DELETE'])
def deleteManager(user_dni):
    cur = mysql.connection.cursor()
    cur.execute("Select * from users JOIN gestor WHERE id_persona = user_id and dni LIKE '" + user_dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from gestor where user_id = {}'.format(user_id))
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
        if data[0][8] == encrypt_password(password):
            os.environ['TOKEN'] = token_generator() + ""
            return jsonify({ "message": "Login accepted", "status": 200, "accepted": True, "user": data[0], "token": os.environ['TOKEN'] })
        else:
            return jsonify({ "message": "User denied", "status": 200, "accepted": False })
    else:
        return jsonify({ "message": "User not found", "status": 404, "accepted": False })





















#Get all materials
@app.route('/materials', methods=['GET'])
def getMaterials():
    cur = mysql.connection.cursor()
    cur.execute("Select * from materials")
    data = cur.fetchall()
    res = []
    for i in data:
        material = {
            "nombre": i[0],
            "cantidad": i[1],
            "stockSeguridad": i[2]
        }
        
        res.append(material)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})



#Create a new material
@app.route('/addMaterials', methods=['POST'])
def addMaterial():
    #mysql data
    nombre = request.json['nombre']
    cantidad = request.json['cantidad']
    stockSeguridad = request.json['stockSeguridad']

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur = mysql.connection.cursor()
        
        cur.execute("Select * from materials WHERE nombre='" + nombre + "'")
        data = cur.fetchall()
        if len(data) > 0:
            return jsonify({'message': "Este material ya existe en la base de datos"})
        else:
            cur.execute('INSERT INTO materials (nombre, cantidad, stockSeguridad) VALUES (%s, %s, %s)', (nombre, cantidad, stockSeguridad))
        mysql.connection.commit()
        return jsonify({'message': "Material insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})


#Create a new material
@app.route('/editMaterial', methods=['PUT'])
def updateMaterial():
    #mysql data
    antiguo_nombre = request.json['antiguo_nombre']
    nombre = request.json['nombre']
    cantidad = request.json['cantidad']
    stockSeguridad = request.json['stockSeguridad']

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur = mysql.connection.cursor()
        cur.execute('UPDATE materials SET nombre=%s, cantidad=%s, stockSeguridad=%s WHERE nombre=%s', (nombre, cantidad, stockSeguridad, antiguo_nombre))
        mysql.connection.commit()
        return jsonify({'message': "Material editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})

#Delete job from de DB
@app.route('/deleteMaterial', methods=['DELETE'])
def deleteMaterial():
    nombre = request.json['nombre']
    cur = mysql.connection.cursor()
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from materials where nombre="' + nombre + '"')
        mysql.connection.commit()
        return jsonify({"message": "Material borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})






















#Get all Jobs
@app.route('/trabajos', methods=['GET'])
def getJobs():
    cur = mysql.connection.cursor()
    cur.execute("Select * from trabajo")
    data = cur.fetchall()
    res = []
    for i in data:
        trabajo = {
            "id": i[0],
            "tipo": i[1],
            "descripcion": i[2],
            "direccion": i[3],
            "id_cliente": i[4],
            "certificado": i[5],
            "presupuesto": i[6]
        }
        
        res.append(trabajo)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})


#Get a Job by its ID
@app.route('/trabajo/<string:job_id>', methods=['GET'])
def getJobByID(job_id):
    cur = mysql.connection.cursor()
    cur.execute("Select * from trabajo where id LIKE "+job_id)
    data = cur.fetchall()
    res = []
    for i in data:
        trabajo = {
            "id": i[0],
            "tipo": i[1],
            "descripcion": i[2],
            "direccion": i[3],
            "id_cliente": i[4],
            "certificado": i[5],
            "presupuesto": i[6]
        }
        
        res.append(trabajo)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})



#Get a Job by its client id
@app.route('/trabajos/<string:id_cliente>', methods=['GET'])
def getJobById_cliente(id_cliente):
    cur = mysql.connection.cursor()
    cur.execute("Select * from trabajo where id_cliente LIKE "+id_cliente)
    data = cur.fetchall()
    res = []
    for i in data:
        trabajo = {
            "id": i[0],
            "tipo": i[1],
            "descripcion": i[2],
            "direccion": i[3],
            "id_cliente": i[4],
            "certificado": i[5],
            "presupuesto": i[6]
        }
        
        res.append(trabajo)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})


#Create Jobs Routes
@app.route('/addJobs', methods=['POST'])
def addJobs():
    #mysql data
    dni = request.json['dni']
    tipo = request.json['tipo']
    descripcion = request.json['descripcion']
    direccion = request.json['direccion']
    
    cur = mysql.connection.cursor()
    cur.execute("Select * from users WHERE dni LIKE '" + dni + "'")
    data = cur.fetchall()
    user_id = data[0][0]

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('INSERT INTO trabajo (tipo, descripcion, direccion, id_cliente, certificado, presupuesto) VALUES (%s, %s, %s, %s, %s, %s)', (tipo, descripcion, direccion, user_id, None, None))
        mysql.connection.commit()
        return jsonify({'message': "Trabajo insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})


#Edit Jobs Routes
@app.route('/editJobs/<string:work_id>', methods=['PUT'])
def editJobs(work_id):
    tipo = request.json['tipo']
    descripcion = request.json['descripcion']
    direccion = request.json['direccion']
    certificado = request.json['certificado']
    presupuesto = request.json['presupuesto']
    
    cur = mysql.connection.cursor()
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('UPDATE trabajo SET tipo=%s, descripcion=%s, direccion=%s, id_cliente=id_cliente, certificado=%s, presupuesto=%s WHERE id=%s', (tipo, descripcion, direccion, certificado, presupuesto, work_id))
        mysql.connection.commit()
        return jsonify({'message': "Trabajo editado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})


#Delete job from de DB
@app.route('/deleteJob/<string:job_id>', methods=['DELETE'])
def deleteJob(job_id):
    cur = mysql.connection.cursor()
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from trabajo where id = {}'.format(job_id))
        mysql.connection.commit()
        return jsonify({"message": "Trabajo borrado correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})





#Get all appointments
@app.route('/citas', methods=['GET'])
def getAgenda():
    cur = mysql.connection.cursor()
    cur.execute("Select * from cita")
    data = cur.fetchall()
    res = []
    for i in data:
        cita = {
            "id": i[0],
            "id_trabajo": i[1],
            "fecha": i[2],
            "certificado": i[3],
            "id_tecnico": i[4],
            "id_perito": i[5],
            "id_administrador": i[6],
            "descripcion": i[7],
            "direccion": i[8]
        }
        
        res.append(cita)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})

@app.route('/citasSinAsociar', methods=['GET'])
def getAgendaSinTrabajo():
    cur = mysql.connection.cursor()
    cur.execute("Select * from cita where id_trabajo IS null")
    data = cur.fetchall()
    res = []
    for i in data:
        cita = {
            "id": i[0],
            "id_trabajo": i[1],
            "fecha": i[2],
            "certificado": i[3],
            "id_tecnico": i[4],
            "id_perito": i[5],
            "id_administrador": i[6],
            "descripcion": i[7],
            "direccion": i[8]
        }
        
        res.append(cita)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})



#Get a Job by its client id
@app.route('/citas/<string:id_trabajo>', methods=['GET'])
def getMeetingById_trabajo(id_trabajo):
    cur = mysql.connection.cursor()
    cur.execute("Select * from cita where id_trabajo LIKE "+id_trabajo)
    data = cur.fetchall()
    res = []
    for i in data:
        cita = {
            "id": i[0],
            "id_trabajo": i[1],
            "fecha": i[2],
            "certificado": i[3],
            "id_tecnico": i[4],
            "id_perito": i[5],
            "id_administrador": i[6],
            "descripcion": i[7],
            "direccion": i[8]
        }
        
        res.append(cita)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})


#Create Meetings Routes
@app.route('/addMeetings', methods=['POST'])
def addMeetings():
    #mysql data
    id_trabajo = request.json['id_trabajo']
    fecha = request.json['fecha']
    id_tecnico = request.json['id_tecnico']
    id_perito = request.json['id_perito']
    id_administrador = request.json['id_administrador']
    descripcion = request.json['descripcion']
    direccion = request.json['direccion']
    
    
    cur = mysql.connection.cursor()

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('INSERT INTO cita (id_trabajo, fecha, certificado, id_tecnico, id_perito, id_administrador, descripcion, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (id_trabajo, fecha, None, id_tecnico, id_perito, id_administrador, descripcion, direccion))
        mysql.connection.commit()
        return jsonify({'message': "Cita insertada en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})



#Edit Meetings Routes
@app.route('/editMeetings/<string:meeting_id>', methods=['PUT'])
def editMeetings(meeting_id):
    fecha = request.json['fecha']
    descripcion = request.json['descripcion']
    direccion = request.json['direccion']
    id_trabajo = request.json['id_trabajo']
    id_tecnico = request.json['id_tecnico']
    id_perito = request.json['id_perito']
    id_administrador = request.json['id_administrador']
    certificado = request.json['certificado']  
    
    cur = mysql.connection.cursor()
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('UPDATE cita SET fecha=%s, descripcion=%s, direccion=%s, id_trabajo=%s, id_tecnico=%s, id_perito=%s, id_administrador=%s, certificado=%s where id=%s', (fecha, descripcion, direccion, id_trabajo, id_tecnico, id_perito, id_administrador, certificado, meeting_id))
        mysql.connection.commit()
        return jsonify({'message': "Cita editada correctamente"})
    
    return jsonify({'message': "Acceso denegado"})
    
    
#Delete meeting from de DB
@app.route('/deleteMeeting/<string:meeting_id>', methods=['DELETE'])
def deleteMeeting(meeting_id):
    cur = mysql.connection.cursor()
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from cita where id = {}'.format(meeting_id))
        mysql.connection.commit()
        return jsonify({"message": "Cita borrada correctamente"})
    else:
        return jsonify({'message': "Acceso denegado"})








@app.route('/certificados/<string:job_id>', methods=['GET'])
def getCertificados(job_id):
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return send_from_directory("./certificados/", "certificado-trabajo" + str(job_id) + ".pdf", as_attachment=True)
    return jsonify({'message': "Acceso denegado"})



@app.route('/certificados/<string:job_id>', methods=['POST'])
def sendCertificados(job_id):
    uploaded_file = request.files['file']
    
    cur = mysql.connection.cursor()

    if request.headers['Authorization'] == os.environ['TOKEN']:
        if uploaded_file.filename != '':
            uploaded_file.filename = "certificado-trabajo" + str(job_id) + ".pdf"
            uploaded_file.save("./certificados/"+uploaded_file.filename)
            
            cur.execute('UPDATE trabajo SET certificado=%s WHERE id=%s', ("certificado-trabajo" + str(job_id) + ".pdf", job_id))
            mysql.connection.commit()
            return jsonify({'message': "Certificado subido correctamente"})
        return jsonify({'message': "Hubo un error en el archivo"})
    else:
        return jsonify({'message': "Acceso denegado"})
        



@app.route('/certificados/<string:job_id>', methods=['DELETE'])
def deleteCertificados(job_id):
    cur = mysql.connection.cursor()
    if request.headers['Authorization'] == os.environ['TOKEN']:
        os.remove("./certificados/certificado-trabajo" + str(job_id) + ".pdf")
        cur.execute('UPDATE trabajo SET certificado=%s WHERE id=%s', (None, job_id))
        mysql.connection.commit()
        return jsonify({'message': "Certificado borrado correctamente"})
    return jsonify({'message': "Acceso denegado"})







@app.route('/presupuestos/<string:job_id>', methods=['GET'])
def getPresupuestos(job_id):
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return send_from_directory("./presupuestos/", "presupuesto-trabajo" + str(job_id) + ".pdf", as_attachment=True)
    return jsonify({'message': "Acceso denegado"})



@app.route('/presupuestos/<string:job_id>', methods=['POST'])
def sendPresupuestos(job_id):
    uploaded_file = request.files['file']
    
    cur = mysql.connection.cursor()

    if request.headers['Authorization'] == os.environ['TOKEN']:
        if uploaded_file.filename != '':
            uploaded_file.filename = "presupuesto-trabajo" + str(job_id) + ".pdf"
            uploaded_file.save("./presupuestos/"+uploaded_file.filename)
            
            cur.execute('UPDATE trabajo SET presupuesto=%s WHERE id=%s', ("presupuesto-trabajo" + str(job_id) + ".pdf", job_id))
            mysql.connection.commit()
            return jsonify({'message': "Presupuesto subido correctamente"})
        return jsonify({'message': "Hubo un error en el archivo"})
    else:
        return jsonify({'message': "Acceso denegado"})
        



@app.route('/presupuestos/<string:job_id>', methods=['DELETE'])
def deletePresupuestos(job_id):
    cur = mysql.connection.cursor()
    if request.headers['Authorization'] == os.environ['TOKEN']:
        os.remove("./presupuestos/presupuesto-trabajo" + str(job_id) + ".pdf")
        cur.execute('UPDATE trabajo SET presupuesto=%s WHERE id=%s', (None, job_id))
        mysql.connection.commit()
        return jsonify({'message': "Presupuesto borrado correctamente"})
    return jsonify({'message': "Acceso denegado"})





@app.route('/alertas', methods=['GET'])
def getAlerts():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alertas')
    data = cur.fetchall()
    res = []
    for i in data:
        alerta = {
            "id": i[0],
            "descripcion": i[1],
            "fecha": i[2],
            "tipoAlerta": i[3],
            "activa": i[4],
            "id_access": i[5]
        }
        
        res.append(alerta)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})

    
@app.route('/alertas', methods=['POST'])
def createAlerts():#mysql data
    descripcion = request.json['descripcion']
    fecha = request.json['fecha']
    tipoAlerta = request.json['tipoAlerta']
    activa = request.json['activa']
    id_access = request.json['id_access']
    
    cur = mysql.connection.cursor()

    if request.headers['Authorization'] == os.environ['TOKEN'] or tipoAlerta == "Contacto":
        cur.execute('INSERT INTO alertas (descripcion, fecha, tipoAlerta, activa, id_access) VALUES (%s, %s, %s, %s, %s)', (descripcion, fecha, tipoAlerta, activa, id_access))
        mysql.connection.commit()
        return jsonify({'message': "Alerta insertada en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})


@app.route('/editAlert/<string:alert_id>', methods=['PUT'])
def editAlerts(alert_id):
    activa = request.json['activa']
    fecha = request.json['fecha']
    
    cur = mysql.connection.cursor()
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('UPDATE alertas SET activa=%s, fecha=%s where id=%s', (activa, fecha, alert_id))
        mysql.connection.commit()
        return jsonify({'message': "Alerta editada correctamente"})
    
    return jsonify({'message': "Acceso denegado"})




@app.route('/consultas', methods=['POST'])
def createConsultas():#mysql data
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    correo = request.json['correo']
    
    cur = mysql.connection.cursor()

    cur.execute('INSERT INTO consultas (nombre, descripcion, correo) VALUES (%s, %s, %s)', (nombre, descripcion, correo))
    mysql.connection.commit()
    return jsonify({'message': "Consulta insertada en la base de datos"})


@app.route('/consultas', methods=['GET'])
def getConsultas():#mysql data
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM consultas')
    data = cur.fetchall()
    res = []
    for i in data:
        consulta = {
            "id": i[0],
            "nombre": i[1],
            "correo": i[2],
            "descripcion": i[3]
        }
        
        res.append(consulta)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})




@app.route('/proveedores', methods=['GET'])
def getProveedores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proveedores')
    data = cur.fetchall()
    res = []
    for i in data:
        proveedor = {
            "nombre": i[0],
            "email": i[1],
            "direccion": i[2],
            "telefono": i[3],
            "id": i[4]
        }
        
        res.append(proveedor)

    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        return jsonify(res)
    else:
        return jsonify({'message': "Acceso denegado"})


@app.route('/proveedores', methods=['POST'])
def createProveedores():#mysql data
    nombre = request.json['nombre']
    email = request.json['email']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    
    cur = mysql.connection.cursor()

    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('INSERT INTO proveedores (nombre, email, direccion, telefono) VALUES (%s, %s, %s, %s)', (nombre, email, direccion, telefono))
        mysql.connection.commit()
        return jsonify({'message': "Proveedor insertado en la base de datos"})
    else:
        return jsonify({'message': "Acceso denegado"})


@app.route('/editProveedor/<string:proveedor_id>', methods=['PUT'])
def editProveedores(proveedor_id):
    nombre = request.json['nombre']
    email = request.json['email']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    
    cur = mysql.connection.cursor()
    
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('UPDATE proveedores SET nombre=%s, email=%s, direccion=%s, telefono=%s where id=%s', (nombre, email, direccion, telefono, proveedor_id))
        mysql.connection.commit()
        return jsonify({'message': "Proveedor editada correctamente"})
    
    return jsonify({'message': "Acceso denegado"})

@app.route('/proveedores/<string:proveedor_id>', methods=['DELETE'])
def deleteProveedores(proveedor_id):
    cur = mysql.connection.cursor()
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('DELETE from proveedores where id = {}'.format(proveedor_id))
        mysql.connection.commit()
        return jsonify({'message': "Proveedor borrado correctamente"})
    return jsonify({'message': "Acceso denegado"})


@app.route('/citasCumplidas', methods=['GET'])
def getCitasMayor5Anyos():
    cur = mysql.connection.cursor()
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('SELECT * FROM trabajo JOIN cita WHERE trabajo.tipo LIKE "Instalacion de gas" and cita.id_trabajo LIKE trabajo.id AND timestampdiff(day, sysdate(), cita.fecha)*-1 > 1800')
        data = cur.fetchall()
        return jsonify({"Result":data})
    return jsonify({'message': "Acceso denegado"})


@app.route('/citasCumplidas', methods=['POST'])
def postCitasMayor5Anyos():
    cur = mysql.connection.cursor()
    if request.headers['Authorization'] == os.environ['TOKEN']:
        cur.execute('SELECT * FROM trabajo JOIN cita WHERE trabajo.tipo LIKE "Instalacion de gas" and cita.id_trabajo LIKE trabajo.id AND timestampdiff(day, sysdate(), cita.fecha)*-1 > 1800')
        data = cur.fetchall()
        cur.execute('SELECT id_access FROM alertas')
        data2 = cur.fetchall()
        for i in data:
            if i[0] not in data2:
                cur.execute('INSERT INTO alertas (descripcion, fecha, tipoAlerta, activa, id_access) VALUES (%s, %s, %s, %s, %s)', ("El trabajo nºX se realizó hace más de 5 años y necesita revisión periódica", datetime.now(), "Revisión", 1, i[0]))
                mysql.connection.commit()
        
        return jsonify({"Result":data})
    return jsonify({'message': "Acceso denegado"})


if __name__ == '__main__':
    app.run(debug=True)