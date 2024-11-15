import datetime

class IngresosGastos:
    def __init__(self, bd):
        self.bd = bd

    def validar_fecha(self, fecha):
        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def agregar_ingreso(self, usuario_id, cantidad, fecha):
        if self.validar_fecha(fecha):
            self.bd.conn.execute('''
                INSERT INTO ingresos (usuario_id, cantidad, fecha)
                VALUES (?, ?, ?)
            ''', (usuario_id, cantidad, fecha))
            self.bd.conn.commit()
            print("Ingreso agregado correctamente.")
        else:
            print("Fecha inválida. Usa el formato YYYY-MM-DD.")

    def agregar_gasto(self, usuario_id, cantidad, categoria, fecha, es_gasto_pequeño):
        if self.validar_fecha(fecha):
            self.bd.conn.execute('''
                INSERT INTO gastos (usuario_id, cantidad, categoria, es_gasto_pequeño, fecha)
                VALUES (?, ?, ?, ?, ?)
            ''', (usuario_id, cantidad, categoria, es_gasto_pequeño, fecha))
            self.bd.conn.commit()
            print("Gasto agregado correctamente.")
        else:
            print("Fecha inválida. Usa el formato YYYY-MM-DD.")

    def agregar_meta_ahorro(self, usuario_id, meta, fecha_limite):
        if self.validar_fecha(fecha_limite):
            self.bd.conn.execute('''
                INSERT INTO metas_ahorro (usuario_id, meta, fecha_limite)
                VALUES (?, ?, ?)
            ''', (usuario_id, meta, fecha_limite))
            self.bd.conn.commit()
            print("Meta de ahorro agregada correctamente.")
        else:
            print("Fecha inválida. Usa el formato YYYY-MM-DD.")
