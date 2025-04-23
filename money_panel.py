from PySide6.QtWidgets import QWidget, QLCDNumber, QVBoxLayout


class MoneyPanel(QWidget):
    def __init__(self):
        super().__init__()

        feedback = QLCDNumber(1)

        layout = QVBoxLayout()
        layout.addWidget(feedback)

        self.setLayout(layout)