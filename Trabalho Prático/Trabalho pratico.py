import csv
import os

PERMISSOES = {
    'gerente': ['criar', 'ler', 'atualizar', 'deletar'],
    'funcionario': ['ler', 'atualizar'],
    'estagiario': ['ler']
}

CAMINHO_ARQUIVO = 'usuarios.csv'

def criar_arquivo_csv():
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nome', 'Email', 'Senha', 'Permissao'])


def criar_usuario(id, nome, email, senha, permissao):
    if permissao not in PERMISSOES:
        raise ValueError("Permissão inválida")
    
    with open(CAMINHO_ARQUIVO, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nome, email, senha, permissao])
    print(f'Usuário {nome} criado com sucesso.')

def ler_usuarios():
    with open(CAMINHO_ARQUIVO, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Pular cabeçalho
        for row in reader:
            print(f'ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}, Permissão: {row[4]}')

def atualizar_usuario(id, nome=None, email=None, senha=None, permissao=None):
    usuarios = []
    atualizado = False

    with open(CAMINHO_ARQUIVO, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        usuarios.append(header)
        
        for row in reader:
            if row[0] == id:
                if nome:
                    row[1] = nome
                if email:
                    row[2] = email
                if senha:
                    row[3] = senha
                if permissao:
                    if permissao not in PERMISSOES:
                        raise ValueError("Permissão inválida")
                    row[4] = permissao
                atualizado = True
            usuarios.append(row)
    
    if atualizado:
        with open(CAMINHO_ARQUIVO, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(usuarios)
        print(f'Usuário com ID {id} atualizado com sucesso.')
    else:
        print(f'Usuário com ID {id} não encontrado.')


def atualizar_usuario(id, nome=None, email=None, senha=None, permissao=None):
    usuarios = []
    atualizado = False

    with open(CAMINHO_ARQUIVO, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        usuarios.append(header)
        
        for row in reader:
            if row[0] == id:
                if nome:
                    row[1] = nome
                if email:
                    row[2] = email
                if senha:
                    row[3] = senha
                if permissao:
                    if permissao not in PERMISSOES:
                        raise ValueError("Permissão inválida")
                    row[4] = permissao
                atualizado = True
            usuarios.append(row)
    
    if atualizado:
        with open(CAMINHO_ARQUIVO, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(usuarios)
        print(f'Usuário com ID {id} atualizado com sucesso.')
    else:
        print(f'Usuário com ID {id} não encontrado.')

def deletar_usuario(id):
    usuarios = []
    encontrado = False

    with open(CAMINHO_ARQUIVO, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        usuarios.append(header)
        
        for row in reader:
            if row[0] == id:
                encontrado = True
            else:
                usuarios.append(row)
    
    if encontrado:
        with open(CAMINHO_ARQUIVO, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(usuarios)
        print(f'Usuário com ID {id} deletado com sucesso.')
    else:
        print(f'Usuário com ID {id} não encontrado.')


def main():
    criar_arquivo_csv()
    criar_usuario('1', 'João Silva', 'joao@empresa.com', 'senha123', 'gerente')
    criar_usuario('2', 'Maria Oliveira', 'maria@empresa.com', 'senha456', 'funcionario')
    ler_usuarios()
    atualizar_usuario('2', nome='Maria Souza')
    deletar_usuario('1')
    ler_usuarios()

if __name__ == "__main__":
    main()
