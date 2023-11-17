from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit
)

class BoardUi(QMainWindow):
    def __init__(self):
        super(BoardUi, self).__init__()

        self.setWindowTitle("Package Tracker")
        self.setGeometry(100, 100, 800, 400)

        widget = QWidget()
        self.layout = QHBoxLayout(widget)
        self.setCentralWidget(widget)

        self.setUp_ui()

        #self.sync = Syncing("test Board", "token")

    def setUp_ui(self):
        self.claimPackageButton = QPushButton("Claim Package")
        self.addPackage = QPushButton("Add Package")
        self.viewPackageStatus = QPushButton("View Package Status")


        button_layout = QVBoxLayout()
        button_layout.addWidget(self.claimPackageButton)
        button_layout.addWidget(self.addPackage)
        button_layout.addWidget(self.viewPackageStatus)

        self.layout.addLayout(button_layout)

    def column_ui(self, title, list_widget):
        column_layout = QVBoxLayout()
        column_label = QLabel(title)
        column_label.setStyleSheet("font-weight: bold;")

        column_layout.addWidget(column_label)
        column_layout.addWidget(list_widget)

        group_container = QWidget()
        group_container.setLayout(column_layout)

        return group_container