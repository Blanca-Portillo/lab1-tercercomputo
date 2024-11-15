import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_base='finanzas.db'):
        # Conexión a la base de datos
        self.conn = sqlite3.connect(nombre_base)
        self.crear_tablas()

    def crear_tablas(self):
        with self.conn:
            # Crear tabla de ingresos y gastos (ajustar según lo necesario)
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS ingresos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                cantidad REAL
            )
            """)
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                cantidad REAL
            )
            """)

    def obtener_ingresos(self, usuario_id):
        # Función para obtener los ingresos de un usuario (ID ejemplo)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ingresos WHERE id=?", (usuario_id,))
        return cursor.fetchall()

    def obtener_gastos(self, usuario_id):
        # Función para obtener los gastos de un usuario (ID ejemplo)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM gastos WHERE id=?", (usuario_id,))
        return cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()
