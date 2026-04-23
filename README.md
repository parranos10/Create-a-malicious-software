# Create-a-malicious-software
Implementar en un entorno controlado un keylogger para comprender su uso en entornos inseguros, la práctica es educacional y  no debe ser usada con intenciones no éticas e ilegales. El log de las letras presionadas en un archivo .txt.

# Libreria
Usamos la libreria keyboard para registar el teclado del usuario
esta se instala con el comando "pip install keyboard"

# Contexto
se crea una funcion en donde lo que va a hacer es registrar lo que teclea el usuario y crear un archivo de texto en donde se guarden todos los caracteres incluyendo el espacio ingresado por el usuario

luego fuera de la funcion esta la linea de codigo que detecta toda tecla presionada por el usuario y esto vuelve a la funcion anterior repitiendose asi cada vez que se aplasta una tecla, y no se crea un nuevo archivo cada vez debido a que en la funcion tenemos "a" que es append y esto hace que si ya existe el archivo simplemente se agrega al final

y por ultimo una tecla de salida que en este caso es "esc" que es para terminar el programa
