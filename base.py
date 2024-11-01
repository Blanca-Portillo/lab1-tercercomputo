import sqlite3

class BaseDeDatos:
    def __init__(self):
        self.conn = sqlite3.connect('finanzas.db')
        self.crear_tablas()

    def crear_tablas(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre_usuario TEXT,
                contraseña TEXT
            );
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS ingresos (
                id INTEGER PRIMARY KEY,
                usuario_id INTEGER,
                cantidad REAL,
                fecha TEXT,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
            );
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY,
                usuario_id INTEGER,
                cantidad REAL,
                categoria TEXT,
                fecha TEXT,
                es_gasto_pequeño BOOLEAN,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
            );
        ''')
        self.conn.commit()
