from Crypto.Cipher import Blowfish, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
import os
import socket

# Función de cifrado Blowfish
def cifrar_blowfish(mensaje):
    clave = os.urandom(16)  # Genera una clave aleatoria de 16 bytes (entre 4 y 56 bytes es permitido)
    cipher = Blowfish.new(clave, Blowfish.MODE_ECB)
    mensaje_padded = pad(mensaje.encode(), Blowfish.block_size)
    return clave + cipher.encrypt(mensaje_padded)  # Incluye la clave con el mensaje cifrado

# Función de cifrado de Sustitución
def cifrar_sustitucion(mensaje, clave):
    return ''.join(chr((ord(char) + clave) % 256) for char in mensaje)

# Función de cifrado de Transposición
def cifrar_transposicion(mensaje):
    return mensaje[::-1]

# Función de cifrado RSA
def cifrar_rsa(mensaje, clave_publica):
    cipher = PKCS1_OAEP.new(clave_publica)
    return cipher.encrypt(mensaje.encode())

# Enviar el mensaje cifrado al servidor
def enviar_mensaje(mensaje_cifrado, metodo_cifrado):
    host = "192.168.18.57"  # Cambia por la dirección IP de la máquina Linux
    port = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(f"{metodo_cifrado}|".encode() + mensaje_cifrado)
            data = s.recv(4096)  # Aumentar tamaño para recibir la respuesta completa
            print(f'Respuesta descifrada desde el servidor: {data.decode()}')
    except Exception as e:
        print(f"Error en la comunicación con el servidor: {e}")

# Elegir el cifrado a utilizar
def main():
    mensaje = input("Introduce el mensaje que deseas cifrar: ")
    metodo_cifrado = input("Introduce el método de cifrado \n1. Blowfish \n2. Sustitucion\n3. Transposicion\n4. RSA: ").strip()

    if metodo_cifrado == "1":
        mensaje_cifrado = cifrar_blowfish(mensaje)
    elif metodo_cifrado == "2":
        clave = int(input("Introduce la clave numérica para el cifrado de sustitución: "))
        mensaje_cifrado = cifrar_sustitucion(mensaje, clave).encode()
    elif metodo_cifrado == "3":
        mensaje_cifrado = cifrar_transposicion(mensaje).encode()
    elif metodo_cifrado == "4":
        # Generar par de claves RSA automáticamente
        key = RSA.generate(2048)
        clave_privada = key.export_key()
        clave_publica = key.publickey()
        mensaje_cifrado = cifrar_rsa(mensaje, clave_publica)
        # Enviar la clave privada junto con el mensaje cifrado
        mensaje_cifrado = clave_privada + b'|' + mensaje_cifrado
    else:
        raise ValueError("Método de cifrado no soportado")

    enviar_mensaje(mensaje_cifrado, metodo_cifrado)

if __name__ == "__main__":
    main()

