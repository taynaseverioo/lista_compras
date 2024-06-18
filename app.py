from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

# Endpoint para processar o login
@app.route('/api/login', methods=['POST'])
def login():
    dados = request.get_json()

    username = dados['username']
    password = dados['password']

    # Aqui você faria a verificação da autenticação usando sua lógica existente
    if AssuntoAutenticacao.autenticar(username, password): # type: ignore
        # Login bem-sucedido
        return jsonify({'message': 'Login bem-sucedido'})
    else:
        # Login falhou
        return jsonify({'message': 'Nome de usuário ou senha incorretos'}), 401

if __name__ == '__main__':
    app.run(debug=True)
