import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from base import BaseDeDatos
from ingreso import IngresosGastos
from graficos import AnalisisCategoria
from alertas import Notificaciones

class FinanceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicializar base de datos
        self.bd = BaseDeDatos()

        # Inicializar componentes
        self.ingresos_gastos = IngresosGastos(self.bd)
        self.analisis = AnalisisCategoria(self.bd)
        self.notifications = Notificaciones(self.bd, self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sistema de Administración y Ahorro de Dinero")
        layout = QVBoxLayout()

        # Botones
        self.income_button = QPushButton("Registrar Ingreso")
        self.expense_button = QPushButton("Registrar Gasto")
        self.analysis_button = QPushButton("Análisis de Gastos")

        # Conectar botones a funciones
        self.income_button.clicked.connect(self.register_income)
        self.expense_button.clicked.connect(self.register_expense)
        self.analysis_button.clicked.connect(self.show_analysis)

        # Agregar botones al layout
        layout.addWidget(self.income_button)
        layout.addWidget(self.expense_button)
        layout.addWidget(self.analysis_button)

        # Configurar el contenedor principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Iniciar las notificaciones
        self.notifications.iniciar_notificaciones(usuario_id=1)  # reemplazar con el ID real

    def register_income(self):
        # Registrar un ingreso
        self.ingresos_gastos.agregar_ingreso(usuario_id=1, cantidad=500)  # Ejemplo de ingreso
        print("Ingreso registrado.")

    def register_expense(self):
        # Registrar un gasto
        self.ingresos_gastos.agregar_gasto(usuario_id=1, cantidad=10, categoria="Café", es_gasto_pequeño=True)  # Ejemplo de gasto
        print("Gasto registrado.")

    def show_analysis(self):
        # Mostrar análisis de gastos
        self.analisis.graficar_distribucion_gastos(usuario_id=1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = FinanceApp()
    mainWindow.show()
    sys.exit(app.exec_())
