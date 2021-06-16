# TFG
En esta API hay varias llamadas para gestionar el control de datos de usuarios de una página web. Estas son:

### GETS
_/users_
>Devuelve una lista de todos los usuarios de la página

_/workers_
>Devuelve una lista de todos los trabajadores de la empresa

_/externalWorkers_
>Devuelve una lista de todos los trabajadores externos de la empresa

_/clients_
>Devuelve una lista de todos los clientes de la empresa

_/gestores_
>Devuelve una lista de todos los gestores de la empresa

_/workers/DNI_
>Cambiando DNI por el dni de una persona, devuelve los datos de ese trabajador si existiese

### POSTS
_/addWorkers_
>Con una cabecera que contenga: 
- passw
- dni
- tipo
>Asocia al usuario con ese dni el tipo de trabajador y una contraseña

_/addExternalWorkers_
>Con una cabecera que contenga: 
- dni
- ocupacion
>Asocia al usuario con ese dni la ocupacion del trabajador externo

_/addClients_
>Con una cabecera que contenga: 
    - dni
>Convierte el usuario en cliente

_/addManager_
>Con una cabecera que contenga: 
- dni
>Convierte el usuario en gestor

_/addUsers_
>Con una cabecera que contenga: 
- nombre
- apellidos
- dni
- email
- direccion
- telefono
>Crea un nuevo usuario en la base de datos

_/editUser/DNI_
>Cambiando DNI por el dni de una persona
>Con una cabecera que contenga: 
- nombre
- apellidos
- email
- direccion
- telefono
>Cambia los datos del usuario por estos nuevos

_/editWorker/DNI_
>Cambiando DNI por el dni de una persona
>Con una cabecera que contenga: 
- passswd
>Cambia la contraseña del trabajador

_/editExternalWorker/DNI_
>Cambiando DNI por el dni de una persona
>Con una cabecera que contenga: 
- ocupacion
>Cambia la ocupacion del trabajador externo

_/editClient/DNI_
>Cambiando DNI por el dni de una persona
>Con una cabecera que contenga: 
- clientePotencial
>Indica si es o no cliente potencial

### DELETES
_/deleteUser/DNI_
>Cambiando DNI por el dni de una persona
>Borra ese usuario

_/deleteWorker/DNI_
>Cambiando DNI por el dni de una persona
>>Borra ese trabajador

_/deleteExternalWorker/DNI_
>Cambiando DNI por el dni de una persona
>Borra ese trabajador externo

_/deleteClient/DNI_
>Cambiando DNI por el dni de una persona
>Borra ese cliente

_/deleteManager/DNI_
>Cambiando DNI por el dni de una persona
>Borra ese gestor
