import sys
from funções import limpar_arquivos
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout



class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton("limpar arquivos")
        self.btn.setStyleSheet("font-size: 40px")
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.limpar)

        self.setCentralWidget(self.cw)
    
    def limpar(self):
        limpar_arquivos()

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()
