from flask import Flask, jsonify, request
from flask_caching import Cache

# Configuração do Flask
app = Flask(__name__)

# Configuração do Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Exemplo de dados que queremos armazenar em cache
sample_data = {
    1: {'name': 'John', 'age': 30},
    2: {'name': 'Jane', 'age': 25}
}

# Rota para consultar dados (com cache)
@app.route('/data/<int:id>', methods=['GET'])
@cache.cached(timeout=60)  # O resultado será armazenado em cache por 60 segundos
def get_data(id):
    if id in sample_data:
        return jsonify(sample_data[id])
    else:
        return jsonify({'error': 'Data not found'}), 404

# Rota para adicionar dados
@app.route('/data/<int:id>', methods=['POST'])
def update_data(id):
    if request.json:
        sample_data[id] = request.json
        return jsonify({'message': 'Data updated successfully'})
    else:
        return jsonify({'error': 'Invalid data provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)