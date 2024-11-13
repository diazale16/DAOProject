# DAOProject: *Consecionario*

## Grupo 18 - Integrantes:
    - [ 86720 ] Diaz Crivelli, Alejandro  
    - [ 87464 ] Zavala, Francisco 
    - [ 90891 ] Mansilla, Benjamín Felipe
    - [ 86516 ] Molina, Daniela 
    - [ 88688 ] Paglia, Francisco 


## Dependencias necesarias
Las **dependencias** necesarias para el uso de la aplicación en sus distintos módulos son:

    - customtkinter (5.2.2)
    - matplotlib (3.9.2)
    - reportlab (3.6.8)
    - SQLAlchemy (2.0.36)
    - tkcalendar (1.6.1)

Para instalar las mismas ejecutar:
```bash
pip install -r requirements.txt
```

## Uso del programa
Para **cargar la base de datos** con informacion pre-generada de forma controlada pero aleatoria ejecutar el siguiente script:  
```bash
python3 DBLoader.py
```
Para **iniciar el programa** ingresando al Home ejecutar:
```bash
python3 main.py
```

## Información relevante:

### Reportes
Los reportes se guardan en la carpeta ```./resources/reports/``` en la raíz del proyecto.
Tambien se pueden encontrar las imágenes generadas para los reportes en la carpeta ```./resources/images/```. 
### Esquema de aplicación
El programa dentro de ```./app/``` se organiza en capas: ***interfaces, gestores, entidades y persistencia***. La particularidad es la **aplicación del ORM SQLAlchemy** para poder definir las entidades como tablas de una base de datos y poder interactuar con la misma a través de funciones genéricas aptas para todas las entidades. Por lo mismo, **los modelos con concentran comportamiento y el mismo se encuentra dentro del gestor de cada entidad** en ```./app/control/```. Por separado se definen los componentes referidos a los reportes dentro de ```./app/reports/```.
### Base de datos
La base de datos se aloja dentro de la carpeta ```./databases/```. La misma se crea de forma automática cada vez que se inicia la aplicación y crea las tablas definidas en ```./app/entities/``` de forma automática si es que no existen. El objeto que compone la **capa de persistencia** de la aplicación es ```./app/persistency/DBManager.py``` que concetra la aplicación del *Patrón Singleton* y funciones genéricas para interactuar con la base de datos.