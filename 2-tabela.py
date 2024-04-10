import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')

cursor = conexao.cursor()

# 2-Criação da Tabela
cursor.execute(
    """
        CREATE TABLE musica(
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
          nome TEXT NOT NULL,
          ano INTEGER NOT NULL,
          cantor TEXT NOT NULL
        );
    """
)
# 3- Fecha conexão
conexao.close()
print("Tabela foi criada")