# from flask import Flask,jsonify,request
# import mysql.connector
# app= Flask(__name__)
# @app.route('/')
# def consulta(consultadb):
#     # Configura los parámetros de conexión
#     host = "192.168.100.20"
#     usuario = "root"
#     contrasena = "1qazxsw2.-"
#     base_datos = "SHYDOUX"

#     try:
#         # Intenta conectarte a la base de datos
#         conexion = mysql.connector.connect(
#             host=host,
#             user=usuario,
#             password=contrasena,
#             database=base_datos
#         )

#         # Verifica si la conexión fue exitosa
#         if conexion.is_connected():
#             print("Conexión exitosa a la base de datos")

#             # Crea un cursor para ejecutar consultas SQL
#             cursor = conexion.cursor()

#             # Ejecuta un SELECT en la tabla garticulos
#             cursor.execute(consultadb)

#             # Recupera todos los resultados
#             resultados = cursor.fetchall()
            
#             # Muestra los resultados
#             for row in resultados:
#                 print(row)

#     except mysql.connector.Error as e:
#         print(f"Error de conexión a la base de datos: {e}")

#     finally:
#         # Cierra el cursor y la conexión al salir
#         if 'conexion' in locals() and conexion.is_connected():
#             cursor.close()
#             conexion.close()
#             print("Conexión cerrada")
#             return resultados

# if __name__ == "__main__":
#     consulta("SELECT * FROM GARTICULOS")
#     app.run(debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sslify import SSLify
import mysql.connector
import json

app = Flask(__name__)
sslify=SSLify(app)
CORS(app) 
@app.route('/consulta/<string:consultadb>', methods=['GET'])
def consulta(consultadb):
    with open("conexion.json") as archivo:
        datos=json.load(archivo)
    # Configura los parámetros de conexión
    print(datos)
    host = datos["host"]
    usuario = datos["user"]
    contrasena = datos["password"]
    base_datos = datos["bd"]

    try:
        # Intenta conectarte a la base de datos
        conexion = mysql.connector.connect(
            host=host,
            user=usuario,
            password=contrasena,
            database=base_datos
        )

        # Verifica si la conexión fue exitosa
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")

            # Crea un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()

            # Ejecuta un SELECT en la tabla garticulos
            cursor.execute(consultadb)

            # Recupera todos los resultados
            resultados = cursor.fetchall()

            # Muestra los resultados
            for row in resultados:
                print(row)

    except mysql.connector.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

    finally:
        # Cierra el cursor y la conexión al salir
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")
            return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True,ssl_context=('cert.pem','key.pem'))
