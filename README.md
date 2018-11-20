# Wordplease
Exercise 7 for the module Python and Django for the Keepcoding Web Development Bootcamp


/ Ultimos posts publicados

/blogs/<nombre_de_usuario>/  Ultimos posts de usuario


## RESTful API services

The following endpoints are available (end slash is mandatory):

### Users API

+ `POST /api/v1/users/<id>/` Any user can register using:

```json
{
	"first_name": "test",
	"last_name": "test",
	"username": "test",
	"email": "test@test.com",
	"password": "test"
}
```

+ `GET /api/v1/users/<id>/` Only admin and authenticated users will be able to display their own account's detail.
+ `PUT /api/v1/users/<id>/` Only admin and authenticated users will be able to update their own account.
+ `DELETE /api/v1/users/<id>/` Only admin and authenticated users will be able to delete their own account.

### Blogs API

+ `GET /api/v1/blogs/` Any user can display a list of urls from the blogs available in the platform. 
+ `GET /api/v1/blogs/?search=test&ordering=title&owner=1` Standard parameters are available for searching, ordering and filtering 


### Posts API
• Un endpoint para poder leer los artículos de un blog de manera que, si el usuario no está
autenticado, mostrará sólo los artículos publicados. Si el usuario está autenticado y es el
propietario del blog o un administrador, podrá ver todos los artículos (publicados o no). En este
endpoint se deberá mostrar únicamente el título del post, la imagen, el resumen y la fecha de
publicación. Este endpoint debe permitir buscar posts por título o contenido y ordenarlos por
título o fecha de publicación. Por defecto los posts deberán venir ordenados por fecha de
publicación descendente.
• Un endpoint para crear posts en el cual el usuario deberá estar autenticado. En este endpoint el
post quedará publicado automáticamente en el blog del usuario autenticado.
• Un endpoint de detalle de un post, en el cual se mostrará toda la información del POST. Si el
post no es público, sólo podrá acceder al mismo el dueño del post o un administrador.
• Un endpoint de actualización de un post. Sólo podrá acceder al mismo el dueño del post o un
administrador.
• Un endpoint de borrado de un post. Sólo podrá acceder al mismo el dueño del post o un
administrador.


