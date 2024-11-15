from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from base import BaseDeDatos
from ingreso import IngresosGastos  # Asegúrate de que este archivo esté correctamente implementado
from graficos import AnalisisFinanciero  # Asegúrate de que el nombre de la clase sea 'AnalisisFinanciero'
from alertas import Notificaciones

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión Financiera Personal")
        self.setGeometry(100, 100, 800, 600)
        self.bd = BaseDeDatos()  # Conectar con la base de datos
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        btn_graficos = QPushButton("Analizar Gastos")
        btn_graficos.clicked.connect(self.mostrar_graficos)
        layout.addWidget(btn_graficos)

        btn_alertas = QPushButton("Configurar Alertas")
        btn_alertas.clicked.connect(self.mostrar_alertas)
        layout.addWidget(btn_alertas)

        btn_progreso = QPushButton("Ver Progreso Mensual")
        btn_progreso.clicked.connect(self.ver_progreso)
        layout.addWidget(btn_progreso)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mostrar_graficos(self):
        analisis = AnalisisFinanciero(self.bd)
        analisis.graficar_distribucion_gastos(1)  # Usuario ejemplo con ID = 1

    def mostrar_alertas(self):
        alertas = Notificaciones(self.bd, self)
        alertas.iniciar_notificaciones(1)  # Usuario ejemplo con ID = 1

    def ver_progreso(self):
        analisis = AnalisisFinanciero(self.bd)
        analisis.graficar_progreso_mensual(1)  # Usuario ejemplo con ID = 1

if __name__ == "__main__":
    app = QApplication([])
    ventana = UI()
    ventana.show()
    app.exec_()
