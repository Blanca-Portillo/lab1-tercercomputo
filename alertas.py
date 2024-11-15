class Notificaciones:
    def __init__(self, bd, ventana):
        self.bd = bd
        self.ventana = ventana

    def iniciar_notificaciones(self, usuario_id):
        gastos = self.bd.obtener_gastos(usuario_id)
        total_gastos = sum(gasto[2] for gasto in gastos)

        if total_gastos > 500:  # Ejemplo: alertar si los gastos superan los 500
            print("¡Alerta! Has superado tu límite de gastos.")
        else:
            print("Tus gastos están dentro del límite.")
