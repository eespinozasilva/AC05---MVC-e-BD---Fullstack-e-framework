import sqlite3

var_ra = 2100645
var_name = 'Émerson'
var_sobrenome = 'Espinoza'
var_mensagem = 'Olá docinho'

banco = sqlite3.connect('correio_elegante.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE cartas (ra int, prime_nome text, ulti_nome text, mensagem text)")

cursor.execute("INSERT INTO cartas (ra, prime_nome, ulti_nome, mensagem) VALUES (?,?,?,?)", (var_ra, var_name, var_sobrenome, var_mensagem))

banco.commit()
cursor.execute("SELECT * FROM cartas")
print(cursor.fetchall())
