
#   API - Livros

# 1- Criação de um API de disponibilização a consulta, criação edição e exclusão
# 2- URL base - localhost
# 3- Endpoints - 
        # - localhost/livros(GET) - Consultar
        # - localhost/livros/id(POST) - Criar
        # - localhost/livros/id(GET) - Consultar um especifico
        # - localhost/livros/id(GET) - Modificar 
        # - localhost/livros(DELETE) - Deletar

# 4- Recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)                   # Criando um aplicação flask com o nome do aplicativo atual
                                        # Fonte de dados
livros = [                              # Lista de Dicionário
    {
        'id' : 1,
        'titulo' : 'A droga do amor',
        'autor' : 'Pedro Bandeira'
    },
    {
        'id' : 2,
        'titulo' : 'Pytho Data Science do Zero',
        'autor' : 'Joel Grus'
    },
    {
        'id' : 3,
        'titulo' : 'Fluent Python',
        'autor' : 'Luciano Ramalho'
    }
]

# Consultar todos

@app.route('/livros',methods=['GET'])            # methods=['GET'] - especica que apenas o GET vai rodar nessa aplicação
def obter_livros():
    return jsonify(livros)

# Consultar id
# Criando a rota
@app.route('/livros/<int:id>',methods=['GET'])   # methods=['GET'] - especica que apenas o GET vai rodar nessa aplicação
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:                # Consultando o id especifico
            return jsonify(livro)

# Editar
# Criando a rota
@app.route('/livros/<int:id>',methods=['PUT'])   # methods=['PUT'] - especica que apenas o PUT vai rodar nessa aplicação
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):      
        if livro.get('id') == id:                # Especificando o id que vai ser editado
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar
# Criando a rota
@app.route('/livros',methods=['POST'])           # methods=['POST'] - especica que apenas o POST vai rodar nessa aplicação
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)                    # Append adicionando o livro

    return jsonify(livros)

# Excluir
# Criando a rota
@app.route('/livros/<int:id>',methods=['DELETE'])# methods=['DELETE'] - especica que apenas o DELETE vai rodar nessa aplicação
def excluir_um_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:                # Especificando o que vai ser excluído
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True) # Inicializando a aplicação com o localhost