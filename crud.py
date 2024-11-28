# FILE: app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import pymysql.cursors
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    connection = pymysql.connect(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('NAME'),
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    return 'Welcome to the CRUD :)'

@app.route('/clientes', methods=['GET', 'POST'])
def manage_clientes():
    if request.method == 'POST':
        data = request.json
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO Clientes (Razon_Social, Nombre_Comercial, Correo_Electronico) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data['razon_social'], data['nombre_comercial'], data['correo_electronico']))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Cliente created successfully'}), 201
    else:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Clientes")
            result = cursor.fetchall()
        connection.close()
        return jsonify(result)

@app.route('/clientes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_cliente(id):
    connection = get_db_connection()
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Clientes WHERE id = %s", (id,))
            result = cursor.fetchone()
        connection.close()
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.json
        with connection.cursor() as cursor:
            sql = "UPDATE Clientes SET Razon_social = %s, Nombre_comercial = %s, Correo_electronico = %s WHERE id = %s"
            cursor.execute(sql, (data['razon_social'], data['nombre_comercial'], data['correo_electronico'], id))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Cliente updated successfully'})
    elif request.method == 'DELETE':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Clientes WHERE id = %s", (id,))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Cliente deleted successfully'})

# CRUD for Domicilios
@app.route('/domicilios', methods=['GET', 'POST'])
def manage_domicilios():
    if request.method == 'POST':
        data = request.json
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO Domicilios (Domicilio, Colonia, Municipio, Estado, Tipo_Direccion) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data['domicilio'], data['colonia'], data['municipio'], data['estado'], data['tipo_direccion']))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Domicilio created successfully'}), 201
    else:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Domicilios")
            result = cursor.fetchall()
        connection.close()
        return jsonify(result)

@app.route('/domicilios/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_domicilio(id):
    connection = get_db_connection()
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Domicilios WHERE id = %s", (id,))
            result = cursor.fetchone()
        connection.close()
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.json
        with connection.cursor() as cursor:
            sql = "UPDATE Domicilios SET Domicilio = %s, Colonia = %s, Municipio = %s, Estado = %s, Tipo_direccion = %s WHERE id = %s"
            cursor.execute(sql, (data['domicilio'], data['colonia'], data['municipio'], data['estado'], data['tipo_direccion'], id))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Domicilio updated successfully'})
    elif request.method == 'DELETE':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Domicilios WHERE id = %s", (id,))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Domicilio deleted successfully'})

# CRUD for Productos
@app.route('/productos', methods=['GET', 'POST'])
def manage_productos():
    if request.method == 'POST':
        data = request.json
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO productos (Nombre, Unidad_Medida, Precio_Base) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data['nombre'], data['unidad_medida'], data['precio_base']))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Producto created successfully'}), 201
    else:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Productos")
            result = cursor.fetchall()
        connection.close()
        return jsonify(result)

@app.route('/productos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_producto(id):
    connection = get_db_connection()
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Productos WHERE id = %s", (id,))
            result = cursor.fetchone()
        connection.close()
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.json
        with connection.cursor() as cursor:
            sql = "UPDATE Productos SET nombre = %s, Unidad_Medida = %s, Precio_Base = %s WHERE id = %s"
            cursor.execute(sql, (data['nombre'], data['unidad_medida'], data['precio_base'], id))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Producto updated successfully'})
    elif request.method == 'DELETE':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Productos WHERE id = %s", (id,))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Producto deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)