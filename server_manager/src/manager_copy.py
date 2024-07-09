import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from ui_main_window import Ui_MainWindow  # Importar el archivo generado por Qt Designer

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI
        self.load_ui()

    def load_ui(self):
        # Setup UI from converted file
        self.setWindowTitle('ROS Service Interface')
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # Load ui attributes from designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.centralwidget)
        self.verticalLayout.addWidget(self.ui.centralwidget)

        # Accessing elements from designer file
        self.float1SpinBox = self.ui.float1SpinBox
        self.float2SpinBox = self.ui.float2SpinBox
        self.robotComboBox = self.ui.robotComboBox
        self.sendButton = self.ui.sendButton

    def haversine(self, lat1, lon1, lat2, lon2):
        R = 6371.0
        
        # Convertir grados a radianes
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        
        # Diferencias de las coordenadas
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        distance = R * c
        return distance

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()