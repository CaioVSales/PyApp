from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def exibir_mensagem():
    dado_lido = janela.lineEdit.text()
    print(dado_lido)
    janela.lineEdit.setText('')
    if dado_lido == "":
        QMessageBox.about(janela,"alerta","Nenhum nome inserido.")
    else:
        QMessageBox.about(janela,"alerta","Olá, " + dado_lido)



app = QtWidgets.QApplication([])
janela = uic.loadUi("verificar.ui")
janela.pushButton.clicked.connect(exibir_mensagem)

janela.show()
app.exec()