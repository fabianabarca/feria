# Modelo de la base de datos

A continuación se presenta la base de datos utilizando el modelo Entidad-Relación. Esta forma de representar la base de datos ayuda a que se tenga una mejor idea de las relaciones entre las entidades y que atributos que se tienen. [Más información].

## Tabla de contenidos

1. [Nomenclatura](#nomenclatura)
2. [Modelo](#modelo)

<a name="nomenclatura"></a>
## Nomenclatura

1. Rectangulo: Representa una  **entidad** (Feria, Horario, Producto, etc.), es decir lo que queremos almacenar en la base de datos dado nuestro minimundo (en nuestro caso nuestro minimundo seria todo lo relacionado con las Ferias).<br />
![Entidad](https://github.com/fabianabarca/ferias/blob/main/static/img/readmes/model/Entidad.png)

2. Rombo: Representa una  **relación** entre dos o más entidades. Existen las siguientes relaciones.<br />
![Relacion](https://github.com/fabianabarca/ferias/blob/main/static/img/readmes/model/Relacion.png)
 
    - **Uno a Uno (1-1)**: Una entidad X solo se puede a una entidad Y.

     ```Ejemplo:  Una entidad Persona y una entidad Licencia de Conducir, una Persona solo puede tener una licencia de conducir, y una licencia de conducir solo puede pertenecer a una persona.```
    - **Uno a muchos (1-N)**: Una entidad X se puede relacionar a muchas entidades Y, pero las entidades Y solo se pueden relacionar a una entidad X. 

     ```Ejemplo: Una entidad Alumno y una entidad Nota, un Alumno puede tener muchas Notas pero las Notas solo estan asociadas a un alumno unico. ```
    - **Muchos a muchos (N-M o N-N)**: Una entidad X se puede relacionar con varias entidades Y, y una entidad Y se puede relacionar con varias entidades X. 

    ```Ejemplo: Una entidad Profesor, y una entidad Alumno, un profesor puede tener varios alumnos y un alumno puede tener varios profesores.```
    
3. Círculo/Óvalo: Representa un **atributo** de la entidad (ID, Nombre, Edad, etc.). Cuando esta subrayado significa que ese atributo es la llave primaria o identificador único de esa entidad.<br />
![Atributo](https://github.com/fabianabarca/ferias/blob/main/static/img/readmes/model/Atributo.png)

<a name="modelo"></a>
## Modelo

![Modelo ER](https://github.com/fabianabarca/ferias/blob/main/static/img/readmes/model/Modelo%20ER%20-%20Ferias.png)


[Más información]: https://www.lucidchart.com/pages/es/que-es-un-diagrama-entidad-relacion
