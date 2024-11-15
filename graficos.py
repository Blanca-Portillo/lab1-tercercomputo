import matplotlib.pyplot as plt
import pandas as pd

class AnalisisFinanciero:
    def __init__(self, bd):
        self.bd = bd

    def graficar_distribucion_gastos(self, usuario_id):
        # Obtener los gastos del usuario
        gastos = self.bd.obtener_gastos(usuario_id)
        if not gastos:
            print("No se encontraron gastos para este usuario.")
            return

        # Convertir los datos a un DataFrame
        df = pd.DataFrame(gastos, columns=["ID", "Fecha", "Cantidad"])

        # Verificar si la columna 'Fecha' es ya de tipo datetime
        if not pd.api.types.is_datetime64_any_dtype(df['Fecha']):
            df['Fecha'] = pd.to_datetime(df['Fecha'])

        # Ordenar los gastos por fecha
        df = df.sort_values(by="Fecha")

        # Graficar la distribución de gastos
        plt.figure(figsize=(10, 6))
        plt.bar(df['Fecha'], df['Cantidad'], color='teal')
        plt.title("Distribución de Gastos")
        plt.xlabel("Fecha")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def graficar_progreso_mensual(self, usuario_id):
        # Obtener los ingresos y gastos del usuario
        ingresos = self.bd.obtener_ingresos(usuario_id)
        gastos = self.bd.obtener_gastos(usuario_id)
        if not ingresos or not gastos:
            print("No se encontraron ingresos o gastos para este usuario.")
            return

        # Convertir los datos de ingresos y gastos a DataFrames
        df_ingresos = pd.DataFrame(ingresos, columns=["ID", "Fecha", "Cantidad"])
        df_gastos = pd.DataFrame(gastos, columns=["ID", "Fecha", "Cantidad"])

        # Convertir las columnas 'Fecha' a tipo datetime si es necesario
        if not pd.api.types.is_datetime64_any_dtype(df_ingresos['Fecha']):
            df_ingresos['Fecha'] = pd.to_datetime(df_ingresos['Fecha'])
        if not pd.api.types.is_datetime64_any_dtype(df_gastos['Fecha']):
            df_gastos['Fecha'] = pd.to_datetime(df_gastos['Fecha'])

        # Ordenar los ingresos y gastos por fecha
        df_ingresos = df_ingresos.sort_values(by="Fecha")
        df_gastos = df_gastos.sort_values(by="Fecha")

        # Graficar el progreso mensual de ingresos y gastos
        plt.figure(figsize=(10, 6))
        plt.plot(df_ingresos['Fecha'], df_ingresos['Cantidad'], label='Ingresos', color='green')
        plt.plot(df_gastos['Fecha'], df_gastos['Cantidad'], label='Gastos', color='red', linestyle='--')
        plt.title("Progreso Mensual de Ingresos y Gastos")
        plt.xlabel("Fecha")
        plt.ylabel("Cantidad")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
