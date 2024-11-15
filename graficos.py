import matplotlib.pyplot as plt
import pandas as pd

class AnalisisFinanciero:
    def __init__(self, bd):
        self.bd = bd

    def graficar_distribucion_gastos(self, usuario_id):
        gastos = self.bd.obtener_gastos(usuario_id)
        if not gastos:
            print("No se encontraron gastos para este usuario.")
            return

        df = pd.DataFrame(gastos, columns=["ID", "Fecha", "Cantidad"])
        df['Fecha'] = pd.to_datetime(df['Fecha'])

        plt.figure(figsize=(10, 6))
        plt.bar(df['Fecha'], df['Cantidad'])
        plt.title("Distribución de Gastos")
        plt.xlabel("Fecha")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def graficar_progreso_mensual(self, usuario_id):
        ingresos = self.bd.obtener_ingresos(usuario_id)
        gastos = self.bd.obtener_gastos(usuario_id)
        if not ingresos or not gastos:
            print("No se encontraron ingresos o gastos para este usuario.")
            return

        df_ingresos = pd.DataFrame(ingresos, columns=["ID", "Fecha", "Cantidad"])
        df_gastos = pd.DataFrame(gastos, columns=["ID", "Fecha", "Cantidad"])
        
        df_ingresos['Fecha'] = pd.to_datetime(df_ingresos['Fecha'])
        df_gastos['Fecha'] = pd.to_datetime(df_gastos['Fecha'])

        plt.figure(figsize=(10, 6))
        plt.plot(df_ingresos['Fecha'], df_ingresos['Cantidad'], label='Ingresos')
        plt.plot(df_gastos['Fecha'], df_gastos['Cantidad'], label='Gastos', linestyle='--')
        plt.title("Progreso Mensual de Ingresos y Gastos")
        plt.xlabel("Fecha")
        plt.ylabel("Cantidad")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()



