# EJEMPLO API REST CON DJANGO

## PROYECTO: API para gestión de libros 
---
Proyecto realizado con la finalidad de poner en práctica los conceptos de **Django** en el backend con los principales métodos CRUD, tomando como guía el curso de [Programador Web Valencia](https://programadorwebvalencia.com/cursos/django-rest-framework/introducci%C3%B3n/) y la documentación de [Django REST Framework](https://www.django-rest-framework.org/).

<br>

## ENDPOINTS
---
### **GET -** `/api/books/` 
Devuelve a todos los libros alojados en la `base de datos` o un mensaje si no hay ningún libro.
### **POST -** `/api/books/` 
Crea un libro, si no hay ningún problema o dato faltante lo alojará a la `base de datos`, caso contrario devolverá el error junto con su descripción.
### **GET -** `/api/books/<int:pk>/` 
Devuelve el libro indicado por parámetro, caso no exista en la `base de datos` retornará un mensaje de error.
### **PUT -** `/api/books/<int:pk>/` 
Busca el libro indicado por parámetro y lo actualiza con los datos que enviamos (pueden ser todos los campos o solo algunos), caso no exista en la `base de datos` retornará un mensaje de error.
### **DELETE -** `/api/books/<int:pk>/` 
Busca el libro indicado por parámetro y lo elimina, caso no exista de antemano en la `base de datos` retornará un mensaje de error.
### **GET -** `/api/test/` 
Endpoint de prueba para saber si el servidor está funcionando.