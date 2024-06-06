from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos enviados en el request
    data = request.get_json()
    app.logger.debug(f'Datos recibidos: {data}')
    
    # Ignorar los datos recibidos y devolver un mensaje de éxito
    return jsonify({'mensaje': 'éxito'})

if __name__ == '__main__':
    app.run(debug=True)


