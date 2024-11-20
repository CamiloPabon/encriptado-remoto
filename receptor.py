# Servidor en Linux (receptor.py)

from Crypto.Cipher import Blowfish, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
import socket
import sys

# Función de descifrado Blowfish
def descifrar_blowfish(mensaje_cifrado, clave):
    cipher = Blowfish.new(clave, Blowfish.MODE_ECB)
    mensaje_padded = cipher.decrypt(mensaje_cifrado)
    return unpad(mensaje_padded, Blowfish.block_size).decode()

# Función de descifrado de Sustitución
def descifrar_sustitucion(mensaje_cifrado, clave):
    return ''.join(chr((ord(char) - clave) % 256) for char in mensaje_cifrado)

# Función de descifrado de Transposición
def descifrar_transposicion(mensaje_cifrado):
    return mensaje_cifrado[::-1]

# Función de descifrado RSA
def descifrar_rsa(mensaje_cifrado, clave_privada_pem):
    clave_privada = RSA.import_key(clave_privada_pem)
    cipher = PKCS1_OAEP.new(clave_privada)
    return cipher.decrypt(mensaje_cifrado).decode()

# Función principal del servidor para aceptar conexiones
def servidor():
    host = '0.0.0.0'  # Acepta conexiones desde cualquier IP
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Configuración para reutilizar la dirección y el puerto
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print("Esperando conexión...")
        while True:
            conn, addr = s.accept()
            with conn:
                try:
                    print(f"Conexión establecida desde {addr}")
                    data = conn.recv(4096)  # Aumentar el tamaño para recibir la información completa
                    metodo_descifrado, mensaje_cifrado = data.split(b'|', 1)

                    metodo_descifrado = metodo_descifrado.decode().strip()
                    print(f"Método de descifrado recibido: {metodo_descifrado}")

                    if metodo_descifrado == "1":
                        clave = input("Introduce la clave para el descifrado (debe ser la misma utilizada para cifrar): ").encode()
                        mensaje_descifrado = descifrar_blowfish(mensaje_cifrado, clave)
                    elif metodo_descifrado == "2":
                        clave = int(input("Introduce la clave numérica para el descifrado de sustitución: "))
                        mensaje_descifrado = descifrar_sustitucion(mensaje_cifrado.decode(), clave)
                    elif metodo_descifrado == "3":
                        mensaje_descifrado = descifrar_transposicion(mensaje_cifrado.decode())
                    elif metodo_descifrado == "4":
                        clave_privada_pem, mensaje_cifrado_rsa = mensaje_cifrado.split(b'|', 1)
                        print("La clave RSA es:")
                        print(clave_privada_pem.decode())
                        mensaje_descifrado = descifrar_rsa(mensaje_cifrado_rsa, clave_privada_pem)
                    else:
                        raise ValueError("Método de descifrado no soportado")

                    print(f'Mensaje descifrado: {mensaje_descifrado}')
                    conn.sendall(mensaje_descifrado.encode())
                except Exception as e:
                    print(f"Error al procesar el mensaje: {e}")
                finally:
                    # Cerrar la conexión con el cliente
                    print("Cerrando la conexión con el cliente...")
                    conn.close()
                print("Cerrando el servidor...")
                s.close()
                sys.exit()

# Función de manejo de cifrados
def cifrados():
    servidor()

if __name__ == "__main__":
    servidor()
