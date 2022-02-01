# TFG
En esta API hay varias llamadas para gestionar el control de datos de usuarios de una página web. Estas son:

### GETS
**_/users_**
>Devuelve una lista de todos los usuarios de la página

**_/workers_**
>Devuelve una lista de todos los trabajadores de la empresa

**_/externalWorkers_**
>Devuelve una lista de todos los trabajadores externos de la empresa

**_/clients_**
>Devuelve una lista de todos los clientes de la empresa

**_/gestores_**
>Devuelve una lista de todos los gestores de la empresa

**_/workers/word_**
>Cambiando word por una palabra busca entre el nombre, apellidos o dni del trabajador y devuelve todos aquellos que lo contengan

**_/users/word_**
>Cambiando word por una palabra busca entre el nombre, apellidos o dni del usuario y devuelve todos aquellos que lo contengan

**_/materials_**
>Devuelve una lista de todos los materiales de la empresa

**_/trabajos_**
>Devuelve una lista de todos los trabajos realizados por la empresa

**_/trabajo/IDs_**
>Cambiando ID por el ID de un trabajo, devuelve todos los datos de este

**_/citas_**
>Devuelve una lista de todas las citas concertadas

### POSTS
**_/addWorkers_**
>Con un cuerpo que contenga: 
- passw
- dni
- tipo
>Asocia al usuario con ese dni el tipo de trabajador y una contraseña

**_/addExternalWorkers_**
>Con un cuerpo que contenga: 
- dni
- ocupacion
>Asocia al usuario con ese dni la ocupacion del trabajador externo

**_/addClients_**
>Con un cuerpo que contenga: 
- dni
>Convierte el usuario en cliente

**_/addManager_**
>Con un cuerpo que contenga: 
- dni
>Convierte el usuario en gestor

**_/addUsers_**
>Con un cuerpo que contenga: 
- nombre
- apellidos
- dni
- email
- direccion
- telefono
>Crea un nuevo usuario en la base de datos

**_/addMaterials_**
>Con un cuerpo que contenga: 
- pass
- dni
- tipo
>Asocia al usuario con ese dni el tipo de trabajador y una contraseña

**_/addJobs_**
>Con un cuerpo que contenga: 
- dni (el del cliente)
- tipo
- descripcion
- direccion
>Crea un trabajo en la base de datos

**_/addMeetings_**
>Con un cuerpo que contenga: 
- id_trabajo
- fecha
- id_tecnico
- id_perito
- id_administrador
- descripcion
- direccion
>Crea una cita en la base de datos

### PUTS
**_/editUser/DNI_**
>Cambiando DNI por el dni de una persona
>Con un cuerpo que contenga: 
- nombre
- apellidos
- email
- direccion
- telefono
- pass
- tipo
- ocupacion
- clientePotencial
>Cambia los datos del usuario por estos nuevos

**_/editWorker/DNI_**
>Cambiando DNI por el dni de una persona
>Con un cuerpo que contenga: 
- tipo
- pass
>Cambia la contraseña del trabajador

**_/editExternalWorker/DNI_**
>Cambiando DNI por el dni de una persona
>Con un cuerpo que contenga: 
- ocupacion
>Cambia la ocupacion del trabajador externo

**_/editClient/DNI_**
>Cambiando DNI por el dni de una persona
>Con un cuerpo que contenga: 
- clientePotencial
>Indica si es o no cliente potencial


**_/editJobs/ID_**
>Cambiando el ID por el id de un trabajo
>Con un cuerpo que contenga: 
- tipo
- descripcion
- direccion
- id_cita
- id_certificado
>Edita un trabajo con los nuevos datos

**_/editMeetings/ID_**
>Cambiando el ID por el id de una cita
>Con un cuerpo que contenga: 
- id_trabajo
- fecha
- id_tecnico
- id_perito
- id_administrador
- descripcion
- direccion
- id_certificado
>Edita una cita con los nuevos datos

### DELETES
**_/deleteUser/DNI_**
>Cambiando DNI por el dni de una persona
>Borra ese usuario

**_/deleteWorker/DNI_**
>Cambiando DNI por el dni de una persona
>Borra ese trabajador

**_/deleteExternalWorker/DNI_**
>Cambiando DNI por el dni de una persona
>Borra ese trabajador externo

**_/deleteClient/DNI_**
>Cambiando DNI por el dni de una persona
>Borra ese cliente

**_/deleteManager/DNI_**
>Cambiando DNI por el dni de una persona
>Borra ese gestor

**_/deleteJob/ID_**
>Cambiando el ID por el id de un trabajo
>Borra ese trabajo

**_/deleteMeeting/ID_**
>Cambiando el ID por el id de una cita
>Borra esa cita