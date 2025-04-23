from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QFrame, QHBoxLayout


class DrinkSelectionPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("DrinkSelectionPanel")
        self.setStyleSheet("""
            #DrinkSelectionPanel{
                border: 2px solid black;
            }
        """)

        layout = QGridLayout()
        layout.addWidget(DrinkSelectionButton("Espresso", "1.5", self),0,0)
        layout.addWidget(DrinkSelectionButton("Double espresso", "1.5", self),0,1)
        layout.addWidget(DrinkSelectionButton("Cappucino", "1.5", self),0,2)
        layout.addWidget(DrinkSelectionButton("Hot chocolate", "1.5", self),1,0)
        layout.addWidget(DrinkSelectionButton("Mint Tea", "1.5", self),1,1)
        layout.addWidget(DrinkSelectionButton("Hot Milk", "1.5", self),1,2)
        self.setLayout(layout)


class DrinkSelectionButton(QFrame):
    def __init__(self, title, price, parent=None):
        super().__init__(parent)

        # Taille fixe du carré
        self.setFixedSize(150, 150)
        self.setObjectName("DrinkButton")
        # Style général du carré
        self.setStyleSheet("""
                  #DrinkButton {
                    background-color: rgb(255, 255, 255);
                    border-radius: 5px;
                    border: 1px solid black;
                }
              """)

        # Layout vertical
        layout = QVBoxLayout()
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(4)

        # Labels avec alignements spécifiques
        label_title = QLabel(title)
        label_title.setAlignment(Qt.AlignLeft)

        label_price = QLabel(price)
        label_price.setAlignment(Qt.AlignRight)

        # Ajout au layout
        layout.addWidget(label_title)
        layout.addWidget(label_price)

        self.setLayout(layout)
