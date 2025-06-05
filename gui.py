import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QProgressBar,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class PokemonBattleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokémon Kampf")
        self.setGeometry(100, 100, 1000, 600)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Kampfbereich (Sprites und HP)
        battle_layout = QHBoxLayout()

        self.left_sprite = QLabel("♀")
        self.left_sprite.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_sprite.setFont(QFont("Arial", 40))

        self.right_sprite = QLabel("♂")
        self.right_sprite.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_sprite.setFont(QFont("Arial", 40))

        # Lebensbalken ohne Prozentanzeige
        self.left_hp_bar = QProgressBar()
        self.left_hp_bar.setMaximum(50)
        self.left_hp_bar.setValue(10)
        self.left_hp_bar.setTextVisible(False)

        self.right_hp_bar = QProgressBar()
        self.right_hp_bar.setMaximum(50)
        self.right_hp_bar.setValue(10)
        self.right_hp_bar.setTextVisible(False)

        # HP-Labels daneben
        self.left_hp_label = QLabel("10 / 50")
        self.left_hp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_hp_label = QLabel("10 / 50")
        self.right_hp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Pokebälle
        pokeball_layout_left = QHBoxLayout()
        pokeball_layout_right = QHBoxLayout()
        for _ in range(6):
            pokeball_layout_left.addWidget(QLabel("🔴"))
            pokeball_layout_right.addWidget(QLabel("🔴"))

        # Linke Seite
        left_layout = QVBoxLayout()
        left_layout.addLayout(pokeball_layout_left)
        left_layout.addWidget(self.left_hp_bar)
        left_layout.addWidget(self.left_hp_label)
        left_layout.addWidget(self.left_sprite)

        # Rechte Seite
        right_layout = QVBoxLayout()
        right_layout.addLayout(pokeball_layout_right)
        right_layout.addWidget(self.right_hp_bar)
        right_layout.addWidget(self.right_hp_label)
        right_layout.addWidget(self.right_sprite)

        battle_layout.addLayout(left_layout)
        battle_layout.addStretch()
        battle_layout.addLayout(right_layout)

        # Unterer Bereich
        lower_layout = QGridLayout()

        for i in range(3):
            btn = QPushButton(f"Pok {i + 1}")
            btn.clicked.connect(self.test_action)
            lower_layout.addWidget(btn, i, 0)

        for i in range(3, 6):
            btn = QPushButton(f"Pok {i + 1}")
            btn.clicked.connect(self.test_action)
            lower_layout.addWidget(btn, i - 3, 1)

        for i in range(4):
            btn = QPushButton(f"Att {i + 1}")
            btn.clicked.connect(self.test_action)
            lower_layout.addWidget(btn, i // 2, 2 + (i % 2))

        main_layout.addLayout(battle_layout)
        main_layout.addStretch()
        main_layout.addLayout(lower_layout)
        self.setLayout(main_layout)

    def test_action(self):
        print("Testfunktion ausgeführt")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokemonBattleUI()
    window.show()
    sys.exit(app.exec())
