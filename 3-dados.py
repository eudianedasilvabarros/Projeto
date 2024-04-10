import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')

cursor = conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO musica(nome, ano, cantor)
        VALUES ('Escolha certa', 2023, 'Henry Freitas')
    """
)

conexao.commit()
conexao.close()