from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos enviados en el request
    data = request.get_json()
    
    # Convertir los datos a un DataFrame con nombres de columnas adecuados
    data_df = pd.DataFrame([data], columns=['abdomen', 'antena'])
    
    # Realizar predicciones
    predictions = model.predict(data_df)
    
    # Devolver las predicciones como respuesta JSON
    return jsonify({'categoria': predictions[0]})

if __name__ == '__main__':
    app.run(debug=True)
