import sys
import os
sys.path.append(os.getcwd() + "\\..\\AI")
from traffic_volume_classification import TrafficModel
import torch
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)

from boardUi import BoardUi

class MainController:
    def __init__(self):
        self.view = BoardUi()
        self.view.claimPackageButton.clicked.connect(self.claimPackage)
        self.model = TrafficModel()
        #self.view.addPackage.clicked.connect(self.addPackage)
        #self.view.viewPackageStatus.clicked.connect(self.viewPackage)

        self.view.show()
        
    def load_model(self, fname):
        # Loads model and prepares it for evaluation
        self.model.load_state_dict(torch.load(fname))
        self.model.eval()

    def claimPackage(self):
        dialog = QDialog(self.view)
        dialog.setWindowTitle("Claim Package")
        dialog_Layout = QFormLayout(dialog)

        name_input = QLineEdit(dialog)
        id_input = QLineEdit(dialog)


        dialog_Layout.addRow("Name:", name_input)
        dialog_Layout.addRow("ID:", id_input)

        buttons_layout = QHBoxLayout()

        claim_button = QPushButton("Claim", dialog)
        #When clicked claim, claim package
        claim_button.clicked.connect(dialog.accept)

        scan_button = QPushButton("Scan", dialog)
        #When clicked, open qr code scanner?

        buttons_layout.addWidget(claim_button)
        buttons_layout.addWidget(scan_button)
        dialog_Layout.addRow(buttons_layout)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(
                self.view, "Package Claimed", "The package was successfully claimed!"
            )

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, "bargeLogo.ico")))
    controller = MainController()
    controller.load_model("model-1000.pt") # needs args
    app.exec()