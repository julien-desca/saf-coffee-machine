from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QHBoxLayout, QTextEdit

from drink_selection_panel import DrinkSelectionPanel
from money_panel import MoneyPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ratio 1:2 - PySide6")
        self.setGeometry(100, 100, 1600, 1200)

        # Conteneur central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout horizontal
        layout = QHBoxLayout()

        # Composants
        widget_gauche = DrinkSelectionPanel()
        widget_droite = MoneyPanel()

        # Ajout avec ratio 1:2
        layout.addWidget(widget_gauche, 2)
        layout.addWidget(widget_droite, 1)

        # Application du layout
        central_widget.setLayout(layout)