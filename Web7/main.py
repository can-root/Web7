import os
import sys
import subprocess
import shutil
from PyQt5 import QtWidgets, QtGui, QtCore

class ProjeOlusturucu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Proje Olusturucu")
        self.setGeometry(100, 100, 400, 600)

        self.etiket = QtWidgets.QLabel("Proje Adini Girin:", self)
        self.etiket.setGeometry(50, 30, 300, 30)

        self.proje_adi_girdisi = QtWidgets.QLineEdit(self)
        self.proje_adi_girdisi.setGeometry(50, 70, 300, 30)

        self.sunucu_etiket = QtWidgets.QLabel("Sunucu Bilesenleri:", self)
        self.sunucu_etiket.setGeometry(50, 110, 300, 30)

        self.php_kutucuk = QtWidgets.QCheckBox("PHP (Sunucu)", self)
        self.php_kutucuk.setGeometry(50, 150, 150, 30)

        self.python_kutucuk = QtWidgets.QCheckBox("Python (Sunucu)", self)
        self.python_kutucuk.setGeometry(50, 180, 150, 30)

        self.sablon_etiket = QtWidgets.QLabel("Sablon Bilesenleri:", self)
        self.sablon_etiket.setGeometry(50, 220, 300, 30)

        self.html_kutucuk = QtWidgets.QCheckBox("HTML", self)
        self.html_kutucuk.setGeometry(50, 250, 100, 30)

        self.css_kutucuk = QtWidgets.QCheckBox("CSS", self)
        self.css_kutucuk.setGeometry(50, 280, 100, 30)

        self.js_kutucuk = QtWidgets.QCheckBox("JavaScript", self)
        self.js_kutucuk.setGeometry(50, 310, 100, 30)

        self.veri_etiket = QtWidgets.QLabel("Veri Bilesenleri:", self)
        self.veri_etiket.setGeometry(50, 340, 300, 30)

        self.sql_kutucuk = QtWidgets.QCheckBox("SQL", self)
        self.sql_kutucuk.setGeometry(50, 370, 100, 30)

        self.nosql_kutucuk = QtWidgets.QCheckBox("NoSQL", self)
        self.nosql_kutucuk.setGeometry(50, 400, 100, 30)

        self.olustur_buton = QtWidgets.QPushButton("Proje Olustur", self)
        self.olustur_buton.setGeometry(150, 440, 100, 30)
        self.olustur_buton.clicked.connect(self.proje_olustur)

        self.proje_listesi = QtWidgets.QListWidget(self)
        self.proje_listesi.setGeometry(50, 480, 300, 60)

        self.ac_buton = QtWidgets.QPushButton("Projeye Git", self)
        self.ac_buton.setGeometry(50, 550, 140, 30)
        self.ac_buton.clicked.connect(self.projeye_git)

        self.sil_buton = QtWidgets.QPushButton("Projeyi Sil", self)
        self.sil_buton.setGeometry(210, 550, 140, 30)
        self.sil_buton.clicked.connect(self.projeyi_sil)

        self.projeleri_yukle()

    def projeleri_yukle(self):
        self.proje_listesi.clear()
        web_dizini = os.path.join(os.getcwd(), 'web')
        if os.path.exists(web_dizini):
            projeler = os.listdir(web_dizini)
            self.proje_listesi.addItems(projeler)

    def projeye_git(self):
        mevcut_ogesi = self.proje_listesi.currentItem()
        if mevcut_ogesi:
            proje_adi = mevcut_ogesi.text()
            proje_yolu = os.path.join(os.getcwd(), 'web', proje_adi)
            if os.path.exists(proje_yolu):
                if sys.platform.startswith('win'):
                    os.startfile(proje_yolu)
                elif sys.platform == 'darwin':
                    subprocess.call(['open', proje_yolu])
                else:
                    subprocess.call(['xdg-open', proje_yolu])

    def projeyi_sil(self):
        mevcut_ogesi = self.proje_listesi.currentItem()
        if mevcut_ogesi:
            proje_adi = mevcut_ogesi.text()
            proje_yolu = os.path.join(os.getcwd(), 'web', proje_adi)
            cevap = QtWidgets.QMessageBox.question(self, 'Proje Sil',
                                                   f"{proje_adi} adli projeyi silmek istediginize emin misiniz?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if cevap == QtWidgets.QMessageBox.Yes:
                try:
                    if os.path.exists(proje_yolu):
                        shutil.rmtree(proje_yolu)
                        self.projeleri_yukle()
                        QtWidgets.QMessageBox.information(self, "Basarili", "Proje basariyla silindi!")
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self, "Hata", f"Projeyi silerken bir hata olustu: {str(e)}")

    def proje_olustur(self):
        proje_adi = self.proje_adi_girdisi.text().strip()
        if not proje_adi:
            QtWidgets.QMessageBox.warning(self, "Hata", "Proje adi bos olamaz!")
            return

        web_dizini = os.path.join(os.getcwd(), 'web')
        if not os.path.exists(web_dizini):
            os.makedirs(web_dizini)

        proje_yolu = os.path.join(web_dizini, proje_adi)
        if os.path.exists(proje_yolu):
            QtWidgets.QMessageBox.warning(self, "Hata", "Bu proje adi zaten mevcut!")
            return

        os.makedirs(proje_yolu)

        if self.php_kutucuk.isChecked():
            with open(os.path.join(proje_yolu, 'server.php'), 'w') as f:
                f.write("<?php\n// PHP Sunucu\n?>\n")

        if self.python_kutucuk.isChecked():
            with open(os.path.join(proje_yolu, 'server.py'), 'w') as f:
                f.write("# Python Sunucu\n")

        template_yolu = os.path.join(proje_yolu, 'sablon')
        os.makedirs(template_yolu)

        veri_yolu = os.path.join(proje_yolu, 'veri')
        os.makedirs(veri_yolu)

        if self.html_kutucuk.isChecked():
            with open(os.path.join(template_yolu, 'index.html'), 'w') as f:
                f.write("<!-- HTML Dosyasi -->\n")

        if self.css_kutucuk.isChecked():
            with open(os.path.join(template_yolu, 'style.css'), 'w') as f:
                f.write("/* CSS Dosyasi */\n")

        if self.js_kutucuk.isChecked():
            with open(os.path.join(template_yolu, 'script.js'), 'w') as f:
                f.write("// JavaScript Dosyasi\n")

        if self.sql_kutucuk.isChecked():
            with open(os.path.join(veri_yolu, 'veri.sql'), 'w') as f:
                f.write("-- SQL Dosyasi\n")

        if self.nosql_kutucuk.isChecked():
            with open(os.path.join(veri_yolu, 'veri.json'), 'w') as f:
                f.write("{}")

        QtWidgets.QMessageBox.information(self, "Basarili", "Proje basariyla olusturuldu!")
        self.projeleri_yukle()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pencere = ProjeOlusturucu()
    pencere.show()
    sys.exit(app.exec_())
