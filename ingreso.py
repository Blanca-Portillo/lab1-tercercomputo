import datetime

class IngresosGastos:
    def __init__(self, bd):
        self.bd = bd

    def agregar_ingreso(self, usuario_id, cantidad):
        fecha = datetime.date.today().isoformat()
        self.bd.conn.execute('INSERT INTO ingresos (usuario_id, cantidad, fecha) VALUES (?, ?, ?)', (usuario_id, cantidad, fecha))
        self.bd.conn.commit()

    def agregar_gasto(self, usuario_id, cantidad, categoria, es_gasto_pequeño=False):
        fecha = datetime.date.today().isoformat()
        self.bd.conn.execute('INSERT INTO gastos (usuario_id, cantidad, categoria, fecha, es_gasto_pequeño) VALUES (?, ?, ?, ?, ?)',
                             (usuario_id, cantidad, categoria, fecha, es_gasto_pequeño))
        self.bd.conn.commit()
