# HeroesApp
Esta es una aplicacion desarrollada con las siguientes tecnologias: HTML (Handlerbars), CSS, JavaScript, Node.js y Express.js. SQL SERVER (SEQUELIZE) 
para la consistencia de los datos.

Debe tener instalado Node.js y nodemon, Express.js y Handlebars. Debe tener SQL SERVER y crear una base de datos llamada HeroesAppWithLogin. 
En la carpeta util del proyecto está el archivoque realiza la conexión con la base de datos, ahí debe colocar sus credenciales en SQL SERVER en lugar de sa y password.

También debe tener instalado SEQUELIZE ORM para SQL SERVER, se puede hacer con el siguiente comando en la terminal: npm install --save tedious

# Funcionamiento
HeroesApp es una aplicacion que te sirve para crear superheroes, los cuales constan de un nombre, una raza y una descripcion. 
Las razas podrás crearlas tu mismo y así poder asignarle la raza que desee a su heroe.

Para disfrutar las funcionalidades de HeroesApp primero debes registrarte, para eso existe el botón de SignIn y Login en la esquina superior derecha. 
Registrate con la información que te solicita la aplicación y luego podrás acceder a las funcionalidades del sitio.

Sin embargo, también puedes ver el Home Page sin estar registrado, pero no podrás hacer nada más que ver el home.

Corre el servidor con el comando npm start si estas en VS code, luego en el navegador utiliza el puerto 9000. localHost:9000. Y así podrás acceder al sitio.
