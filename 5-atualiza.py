import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2-Atualização
id = 1
cursor.execute(
    """
    UPDATE musica set nome = ?
    WHERE id = ?
    """,
    ("Escolha certa", id)

)
conexao.commit()