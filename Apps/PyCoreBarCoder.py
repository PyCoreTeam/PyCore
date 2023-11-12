import os.path
import shutil
import sys
import time
from datetime import datetime

import barcode
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QMessageBox
from barcode.writer import SVGWriter, ImageWriter
from qfluentwidgets import ComboBox, BodyLabel, TextEdit, PushButton, InfoBar, InfoBarPosition, CheckBox, MessageBox


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
        self.text()

    def clear(self):

        reply = QMessageBox.question(self, 'Clear barcodes', 'Are you sure you want to clear barcodes?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:

            for filename in os.listdir("./barcodes"):
                file_path = os.path.join("./barcodes", filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    InfoBar.success(
                        title="OK",
                        content=f"成功清除",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.BOTTOM_LEFT,
                        duration=6000,
                        parent=self,

                    )
                except Exception as e:
                    InfoBar.error(
                        title="Failed",
                        content=f"清除失败，错误信息{e}",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.BOTTOM_LEFT,
                        duration=6000,
                        parent=self,

                    )

    def init(self):
        # fonts
        self.bodyfont = QFont()
        self.bodyfont.setFamily("Arial")
        self.barcodeCXT = BodyLabel(self)
        self.barcodeCXT.setGeometry(20, 80, 110, 40)
        self.bodyfont.setPointSize(15)
        self.barcodeCXT.setFont(self.bodyfont)

        self.messageCXT = BodyLabel(self)
        self.messageCXT.setGeometry(185, 80, 110, 40)
        self.bodyfont.setPointSize(15)
        self.messageCXT.setFont(self.bodyfont)

        self.message = TextEdit(self)
        self.message.setGeometry(185, 120, 130, 40)
        self.setGeometry(300, 300, 900, 760)
        self.setWindowTitle('PyCore Bar Coder 1.0')
        self.barcodeComboBox = ComboBox(self)
        self.barcodeComboBox.addItems(barcode.PROVIDED_BARCODES)
        self.barcodeComboBox.setGeometry(20, 120, 110, 40)
        self.barcodeComboBox.setVisible(True)
        self.summonBtn = PushButton(self)
        self.summonBtn.setGeometry(370, 120, 130, 40)
        self.summonBtn.setFont(self.bodyfont)
        self.summonBtn.clicked.connect(self.gen)

        self.clearBtn = PushButton(self)
        self.clearBtn.setGeometry(560, 120, 90, 40)
        self.clearBtn.setFont(self.bodyfont)
        self.clearBtn.clicked.connect(self.clear)

        self.viewc = CheckBox(self)
        self.viewc.setGeometry(20, 0, 50, 50)
        self.viewl = BodyLabel(self)
        self.bodyfont.setPointSize(12)
        self.viewl.setGeometry(20, 40, 50, 50)
        self.viewl.setFont(self.bodyfont)
        self.show()

    def text(self):
        self.barcodeCXT.setText("Barcode")
        self.messageCXT.setText("Message")
        self.summonBtn.setText("Generate")
        self.viewl.setText("View")
        self.clearBtn.setText("Clear")

    def gen(self):
        try:
            barcode_ = barcode.get_barcode(self.barcodeComboBox.text())
            barcode_ = barcode_(self.message.toPlainText(), writer=ImageWriter())
            date = datetime.now().date()
            _date = datetime.now()
            c = f'{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}_{_date.hour}-{_date.minute}-{_date.second}'
            date.strftime('%m')
            if not os.path.exists("./barcodes"):
                os.mkdir("./barcodes")
            barcode_.save(f"./barcodes/barcode_{c}")
            InfoBar.success(
                title="Success",
                content=f"成功生成",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_LEFT,
                duration=6000,
                parent=self,
            )

            from PIL import Image
            if self.viewc.isChecked():
                Image.open(f"./barcodes/barcode_{c}.png").show()
        except Exception as e:
            InfoBar.error(
                title="Failed",
                content=f"生成失败，错误信息{e}",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_LEFT,
                duration=6000,
                parent=self,
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UI = UI()
    sys.exit(app.exec_())
