from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('model.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos enviados en el request
    data = request.get_json()
    app.logger.debug(f'Datos recibidos: {data}')
    
    # Convertir los datos a un DataFrame con nombres de columnas adecuados
    try:
        data_df = pd.DataFrame([data], columns=['abdomen', 'antena'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        predictions = model.predict(data_df)
        app.logger.debug(f'Predicciones: {predictions}')
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'categoria': predictions[0]})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

