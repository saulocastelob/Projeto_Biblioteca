# Cadastrar
# Editar
# Remover
# Buscar por código
# Buscar todos
# Emprestar
# Devolver

'''
{
- codigo
- titulo
- autor
- categoria
- emprestado
}

'''



banco = [
    {
        'codigo': 1,
        'titulo': 'Código limpo',
        'autor': 'Roberth',
        'categoria': 'Programação',
        'alugado': True,
        'preco': 15.90 
    }
]
codigoAtual = 1 # variável global

def addLivro(titulo: str, autor: str, categoria: str, preco: float):
    global codigoAtual
    codigoAtual += 1
    livro = {
        'codigo': codigoAtual,
        'titulo': titulo,
        'autor': autor,
        'categoria': categoria,
        'alugado': False,
        'preco': preco
    }
    banco.append(livro)
    print('Livro cadastrado com sucesso!')


def inputAddLivro():
    titulo = input('Digite o titulo do livro: ')
    autor = input('Digite o autor do livro: ')
    categoria = input('Digite a categoria do livro: ')
    preco = float(input('Digite o preço do livro: '))
    addLivro(titulo, autor, categoria, preco)


def buscarPorCodigo(codigo: int):
    for livro in banco:
        if livro['codigo'] == codigo:
            return livro
    return None # Nulo


def editLivro(codigo: int, titulo: str, 
              autor: str, categoria: str, preco: float):
    livro = buscarPorCodigo(codigo)
    livro['titulo'] = titulo
    livro['autor'] = autor
    livro['categoria'] = categoria
    livro['preco'] = preco
    print('Dados alterados com sucesso!!')


def inputEditLivro():
    codigo = int(input('Digite o código do livro: '))
    if buscarPorCodigo(codigo):
        titulo = input('Digite o titulo do livro: ')
        autor = input('Digite o autor do livro: ')
        categoria = input('Digite a categoria do livro: ')
        preco = float(input('Digite o preço do livro: '))
        editLivro(codigo, titulo, autor, categoria, preco)
    else:
        print('Livro não encontrado!!!')


def inputBuscarPorCodigo():
    codigo = int(input('Digite o código do livro: '))
    livro = buscarPorCodigo(codigo)
    if livro:
        print('--- DADOS DO LIVRO ---')
        print(f"Código: {livro['codigo']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Categoria: {livro['categoria']}")
        print(f"Preço: {livro['preco']}")
        print(f"Alugado: {livro['alugado']}")
        return
    print('Livro não encontrado!!')


def deleteLivro(codigo: int):
    livro = buscarPorCodigo(codigo)
    banco.remove(livro)
    print('Livro removido com sucesso!')


def inputDeleteLivro():
    codigo = int(input('Digite o código do livro: '))
    livro = buscarPorCodigo(codigo)
    if livro:
        deleteLivro(codigo)
    else:
        print('Livro não encontrado!')


def listarTodos():
    for livro in banco:
        print('--- DADOS DO LIVRO ---')
        print(f"Código: {livro['codigo']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Categoria: {livro['categoria']}")
        print(f"Preço: {livro['preco']}")
        print(f"Alugado: {livro['alugado']}")
        print('-'*50)

def menu():
    while True:
        print('--- BEM VINDO AO MENU ---')
        print('1 - Cadastrar livro')
        print('2 - Editar livro')
        print('3 - Buscar livro')
        print('4 - Remover livro')
        print('5 - Listar todos')
        print('6 - Alugar livro')
        print('7 - Devolver livro')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            inputAddLivro()
        elif opcao == '2':
            inputEditLivro()
        elif opcao == '3':
            inputBuscarPorCodigo()
        elif opcao == '4':
            inputDeleteLivro()
        elif opcao == '5':
            listarTodos()
        else: 
            break

menu()
