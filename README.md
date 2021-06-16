# TFG
En esta API hay varias llamadas para gestionar el control de datos de usuarios de una página web. Estas son:

### GETS
/users
Devuelve una lista de todos los usuarios de la página

/workers
Devuelve una lista de todos los trabajadores de la empresa

/externalWorkers
Devuelve una lista de todos los trabajadores externos de la empresa

/clients
Devuelve una lista de todos los clientes de la empresa

/gestores
Devuelve una lista de todos los gestores de la empresa

/workers/DNI
Cambiando DNI por el dni de una persona, devuelve los datos de ese trabajador si existiese

### POSTS
/addWorkers
Con una cabecera que contenga: 
    - passw
    - dni
    - tipo
Asocia al usuario con ese dni el tipo de trabajador y una contraseña

/addExternalWorkers
Con una cabecera que contenga: 
    - dni
    - ocupacion
Asocia al usuario con ese dni la ocupacion del trabajador externo

/addClients
Con una cabecera que contenga: 
    - dni
Convierte el usuario en cliente

/addManager
Con una cabecera que contenga: 
    - dni
Convierte el usuario en gestor

/addUsers
Con una cabecera que contenga: 
    - nombre
    - apellidos
    - dni
    - email
    - direccion
    - telefono
Crea un nuevo usuario en la base de datos

/editUser/DNI
Cambiando DNI por el dni de una persona
Con una cabecera que contenga: 
    - nombre
    - apellidos
    - email
    - direccion
    - telefono
Cambia los datos del usuario por estos nuevos

/editWorker/DNI
Cambiando DNI por el dni de una persona
Con una cabecera que contenga: 
    - passswd
Cambia la contraseña del trabajador

/editExternalWorker/DNI
Cambiando DNI por el dni de una persona
Con una cabecera que contenga: 
    - ocupacion
Cambia la ocupacion del trabajador externo

/editClient/DNI
Cambiando DNI por el dni de una persona
Con una cabecera que contenga: 
    - clientePotencial
Indica si es o no cliente potencial

### DELETES
/deleteUser/DNI
Cambiando DNI por el dni de una persona
Borra ese usuario

/deleteWorker/DNI
Cambiando DNI por el dni de una persona
Borra ese trabajador

/deleteExternalWorker/DNI
Cambiando DNI por el dni de una persona
Borra ese trabajador externo

/deleteClient/DNI
Cambiando DNI por el dni de una persona
Borra ese cliente

/deleteManager/DNI
Cambiando DNI por el dni de una persona
Borra ese gestor
