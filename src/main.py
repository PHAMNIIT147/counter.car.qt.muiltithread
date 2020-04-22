import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    win = MainWindow()

    # Setup style
    app.setStyleSheet("QLineEdit { background-color: black }")

    # Show main window
    win.show()

    # Start event loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
