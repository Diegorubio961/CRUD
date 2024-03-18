from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Configuración de la conexión a la base de datos
conn = pymysql.connect(
    host='sql10.freesqldatabase.com',
    user='sql10692197',
    password='Q5QUPZj2iF',
    database='sql10692197'
)

# Ruta para crear un cliente
@app.route('/crear_cliente', methods=['POST'])
def crear_cliente():
    data = request.json
    nombre = data['nombre']
    apellido = data['apellido']
    direccion = data['direccion']
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (Nombre, Apellido, direccion) VALUES (%s, %s, %s)", (nombre, apellido, direccion))
    conn.commit()
    cursor.close()
    
    return jsonify({'message': 'Cliente creado exitosamente'}), 201

# Ruta para obtener todos los clientes
@app.route('/leer_clientes', methods=['POST'])
def obtener_clientes():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    
    return jsonify(clientes), 200

# Ruta para actualizar un cliente por su ID
@app.route('/actualizar_cliente', methods=['POST'])
def actualizar_cliente():
    data = request.json
    id = data['id']
    nombre = data["nombre"]
    apellido = data['apellido']
    direccion = data['direccion']
    
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET Nombre=%s, Apellido=%s, direccion=%s WHERE id=%s", (nombre, apellido, direccion, id))
    conn.commit()
    cursor.close()
    
    return jsonify({'message': 'Cliente actualizado exitosamente'}), 200

# Ruta para eliminar un cliente por su ID
@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    data = request.json
    id = data['id']

    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=%s", id)
    conn.commit()
    cursor.close()
    
    return jsonify({'message': 'Cliente eliminado exitosamente'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

