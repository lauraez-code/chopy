import sqlite3 as sql

conn = sql.connect("chopy_db")


    
conn.execute ('''CREATE TABLE cliente (
        cpf TEXT NOT NULL PRIMARY KEY,
        email TEXT NOT NULL,
        rua_cliente TEXT NOT NULL,
        bairro_cliente TEXT NOT NULL,
        cidade_cliente TEXT NOT NULL,
        estado_cliente TEXT NOT NULL)''')



conn.execute ('''CREATE TABLE pedido (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        data_pedido DATE NOT NULL,
        valor_total NUMERIC (10,2) NOT NULL,
        status TEXT NOT NULL,
        forma_pagamento TEXT NOT NULL,
        id_cliente INTEGER REFERENCES cliente (cpf))''')  



conn.execute ('''CREATE TABLE loja (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cnpj_cpf TEXT NOT NULL,
        data_cadastro DATE NOT NULL,
        cidade_origem TEXT NOT NULL)''')    


    
conn.execute ('''CREATE TABLE produto (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        preco NUMERIC (10,2) NOT NULL,
        estoque INTEGER NOT NULL,
        id_loja INTEGER REFERENCES loja(id))''')


    
conn.execute ('''CREATE TABLE cupom (
        codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        valor_min_gasto NUMERIC (10,2),
        valor_desconto NUMERIC (10,2),
        data_expiracao DATE NOT NULL)''')
    
    

conn.execute ('''CREATE TABLE pedido_produto (
        id_pedido INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        PRIMARY KEY (id_pedido, id_produto),
        FOREIGN KEY (id_pedido) REFERENCES pedido (id),
        FOREIGN KEY (id_produto) REFERENCES produto (id))''')



conn.execute ('''CREATE TABLE pedido_cupom (
        id_pedido INTEGER NOT NULL,
        codigo_cupom INTEGER NOT NULL,
        PRIMARY KEY (id_pedido, codigo_cupom),
        FOREIGN KEY (id_pedido) REFERENCES pedido (id),
        FOREIGN KEY (codigo_cupom) REFERENCES cupom (codigo))''')

conn.close() 

     
    
