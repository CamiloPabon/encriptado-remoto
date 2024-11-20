Proyecto de Servidor de Descifrado en Linux
## Descripción

Este proyecto es un servidor desarrollado en Python que permite recibir mensajes cifrados desde un cliente, descifrarlos utilizando diferentes algoritmos de descifrado, y devolver el mensaje original. El servidor está diseñado para funcionar en un entorno Linux y es capaz de manejar múltiples tipos de cifrado, incluyendo Blowfish, sustitución, transposición, y RSA.

## Características

- **Soporte para diferentes algoritmos de cifrado**: El servidor puede descifrar mensajes utilizando los siguientes métodos:
    - **Blowfish**: Utiliza una clave proporcionada por el usuario para descifrar el mensaje.
    - **Sustitución**: Realiza un descifrado mediante un valor numérico de desplazamiento.
    - **Transposición**: Inversa el orden de los caracteres en el mensaje.
    - **RSA**: Descifra mensajes cifrados mediante claves RSA públicas y privadas.
- **Servidor persistente**: El servidor puede permanecer en funcionamiento para recibir y procesar varias solicitudes de descifrado, permitiendo que el usuario decida si desea continuar tras cada descifrado.
- **Comunicación Cliente-Servidor**: Utiliza sockets TCP para la comunicación entre el cliente y el servidor, asegurando una conexión confiable para la transmisión de mensajes cifrados y respuestas.

## Requisitos

- Python 3.
- Librería PyCryptodome para el manejo de cifrado y descifrado.
- Entorno Linux para ejecutar el servidor.

## Cómo usar

1. Clonar el repositorio en tu entorno Linux.
2. Instalar las dependencias necesarias utilizando `pip install pycryptodome`.
3. Ejecutar el servidor con `python3 receptor.py`.
4. El servidor esperará conexiones desde un cliente que envíe mensajes cifrados.
5. Tras recibir y descifrar un mensaje, el servidor preguntará si deseas continuar o finalizar la aplicación.

## Ejemplos de Uso

El cliente envía un mensaje cifrado con Blowfish o RSA, y el servidor solicita la clave correspondiente para descifrarlo y luego muestra el mensaje original.

Además de RSA, el servidor soporta otros métodos sencillos de cifrado, lo que lo hace ideal para escenarios educativos o para probar conceptos de seguridad y criptografía.
Este proyecto es un servidor desarrollado en Python que permite recibir mensajes cifrados desde un cliente, descifrarlos utilizando diferentes algoritmos de descifrado, y devolver el mensaje original. El servidor está diseñado para funcionar en un entorno Linux y es capaz de manejar múltiples tipos de cifrado, incluyendo Blowfish, sustitución, transposición, y RSA.

