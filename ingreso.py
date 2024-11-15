import datetime

class IngresosGastos:
    def __init__(self, bd):
        self.bd = bd

    def validar_fecha(self, fecha):
        """Verifica si la fecha ingresada tiene el formato correcto."""
        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            print("Fecha inválida. Usa el formato YYYY-MM-DD.")  # Mensaje claro si la fecha es inválida
            return False

    def agregar_ingreso(self, usuario_id, cantidad, fecha):
        """Agrega un ingreso a la base de datos."""
        if self.validar_fecha(fecha):
            try:
                self.bd.conn.execute('''
                    INSERT INTO ingresos (usuario_id, cantidad, fecha)
                    VALUES (?, ?, ?)
                ''', (usuario_id, cantidad, fecha))
                self.bd.conn.commit()
                print("Ingreso agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar el ingreso: {e}")

    def agregar_gasto(self, usuario_id, cantidad, categoria, fecha, es_gasto_pequeño):
        """Agrega un gasto a la base de datos."""
        if self.validar_fecha(fecha):
            try:
                self.bd.conn.execute('''
                    INSERT INTO gastos (usuario_id, cantidad, categoria, es_gasto_pequeño, fecha)
                    VALUES (?, ?, ?, ?, ?)
                ''', (usuario_id, cantidad, categoria, es_gasto_pequeño, fecha))
                self.bd.conn.commit()
                print("Gasto agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar el gasto: {e}")

    def agregar_meta_ahorro(self, usuario_id, meta, fecha_limite):
        """Agrega una meta de ahorro a la base de datos."""
        if self.validar_fecha(fecha_limite):
            try:
                self.bd.conn.execute('''
                    INSERT INTO metas_ahorro (usuario_id, meta, fecha_limite)
                    VALUES (?, ?, ?)
                ''', (usuario_id, meta, fecha_limite))
                self.bd.conn.commit()
                print("Meta de ahorro agregada correctamente.")
            except Exception as e:
                print(f"Error al agregar la meta de ahorro: {e}")
