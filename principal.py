import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QLineEdit, QDialog, QLabel, QFormLayout, QMessageBox)
from base import BaseDeDatos
from ingreso import IngresosGastos
from graficos import AnalisisCategoria
from alertas import Notificaciones

class IngresoGastoDialog(QDialog):
    def __init__(self, tipo, parent=None):
        super().__init__(parent)
        self.tipo = tipo
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"Registrar {self.tipo}")
        layout = QFormLayout()

        self.cantidad_input = QLineEdit()
        self.fecha_input = QLineEdit()  # O usar QDateEdit para seleccionar fecha

        layout.addRow(QLabel("Cantidad:"), self.cantidad_input)
        layout.addRow(QLabel("Fecha:"), self.fecha_input)

        if self.tipo == "Gasto":
            self.categoria_input = QLineEdit()
            self.es_gasto_pequeño_input = QLineEdit()  # Usar QCheckBox si prefieres
            layout.addRow(QLabel("Categoría:"), self.categoria_input)
            layout.addRow(QLabel("¿Es gasto pequeño? (1=Sí, 0=No):"), self.es_gasto_pequeño_input)

        self.submit_button = QPushButton("Registrar")
        self.submit_button.clicked.connect(self.submit_data)
        layout.addRow(self.submit_button)

        self.setLayout(layout)

    def submit_data(self):
        try:
            cantidad = float(self.cantidad_input.text())
            fecha = self.fecha_input.text()  # Aquí puedes agregar validación de fecha
            if self.tipo == "Ingreso":
                self.parent().ingresos_gastos.agregar_ingreso(usuario_id=1, cantidad=cantidad, fecha=fecha)
                QMessageBox.information(self, "Éxito", "Ingreso registrado.")
            else:  # Gasto
                categoria = self.categoria_input.text()
                es_gasto_pequeño = bool(int(self.es_gasto_pequeño_input.text()))  # Convierte a booleano
                self.parent().ingresos_gastos.agregar_gasto(usuario_id=1, cantidad=cantidad, 
                                                             categoria=categoria, es_gasto_pequeño=es_gasto_pequeño)
                QMessageBox.information(self, "Éxito", "Gasto registrado.")
            self.close()
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingrese valores válidos.")

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
        self.income_button.clicked.connect(self.open_income_dialog)
        self.expense_button.clicked.connect(self.open_expense_dialog)
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

    def open_income_dialog(self):
        dialog = IngresoGastoDialog("Ingreso", self)
        dialog.exec_()

    def open_expense_dialog(self):
        dialog = IngresoGastoDialog("Gasto", self)
        dialog.exec_()

    def show_analysis(self):
        # Mostrar análisis de gastos
        self.analisis.graficar_distribucion_gastos(usuario_id=1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = FinanceApp()
    mainWindow.show()
    sys.exit(app.exec_())
