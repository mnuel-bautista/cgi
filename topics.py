#!C:/Python/python.exe
# Librerias para conexion con MySQL y Servidor Apache
import mysql.connector
import os
import cgi
import cgitb

cgitb.enable()

# Toda pagina web inicia con el tipo de contenido y una linea en blanco
print("Content-type: text/html")
print()

# Se revisa el tipo de peticion http GET, POST, PUT, DELETE
metodo = os.environ["REQUEST_METHOD"]

# Se obtiene una lista de valores recibidos del formulario
valoresUrl = cgi.FieldStorage()

if metodo == 'GET':
    print("Metodo de consulta")
    print()
    query = ("SELECT * FROM topics")
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    for (id, topic, user_id, created_at, updated_at) in cursor:
        print("<h1>id:%s</h1>, <h1>topic:%s</h1>" % (id, topic))
    cursor.close()
    conexion.close()
elif metodo == 'POST':
    print("Metodo de agregar")
    print()
    topic = valoresUrl["topic"].value
    query = ("INSERT INTO topics(title, user_id) VALUES('{}', 1)".format(topic))
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    print("Se agrego %s registro" % cursor.rowcount)
    cursor.close()
    conexion.close()
elif metodo == 'PUT':
    print('Metodo de actualizar')
    title = valoresUrl['id'].value
    query = ('UPDATE topics SET topic="{}"', title)
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    cursor.close()
    conexion.close()
    print()
elif metodo == 'DELETE':
    print("Metodo de eliminar")
    id = valoresUrl['id_topic'].value
    query = ('DELETE FROM topics WHERE id="{}"'.format(id))
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    cursor.close()
    conexion.close()
else:
    print("Error")
    print()
