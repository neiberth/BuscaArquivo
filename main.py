# Autor: Neiberth Lucena moreira
# Versão: 1.0.0.1 beta
# Data: 14/12/2021
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

def onClik():
    arq = edt_arquivo.text()
    dir = edt_dir.text()
    ltw_resultado.addItem(dir)

def onClear():
    edt_dir.clear()
    edt_arquivo.clear()
    ltw_resultado.clear()

# ****** INIT - APP ******
app = QApplication(sys.argv)

# ****** INIT - ICONS ******
ic_open_small = QIcon()
ic_open_small.addFile('img/openSmall.png')
# ****** END - ICONS ******


# ****** INIT - WINDOW ******
window = QMainWindow()
window.setGeometry(350, 200, 560, 410)
window.setMinimumSize(560, 410)
window.setMaximumSize(560, 410)
window.setWindowTitle("Programa de Busca de arquivos")
window.setWindowIcon(ic_open_small)
# ****** END - WINDOW ******

# ****** INIT - LABELS ******
lb_dir = QLabel(window)
lb_dir.setText('Digite o diretorio de busca: ')
lb_dir.setGeometry(20, 20, 190, 20)

lb_arquivo = QLabel(window)
lb_arquivo.setText('Digite nome do aquivo: ')
lb_arquivo.setGeometry(20, 60, 190, 20)
# ****** END - LABELS ******

# ****** INIT - EDIT TEXT ******
edt_dir = QLineEdit(window)
edt_dir.setGeometry(210, 20, 335, 20)
edt_dir.setObjectName('edt_dir')

edt_arquivo = QLineEdit(window)
edt_arquivo.setGeometry(210, 60, 335, 20)
edt_arquivo.setObjectName('edt_arquivo')
# ****** END - EDIT TEXT ******

# ****** INIT - BUTTONS ******
btn_busca = QPushButton(window)
btn_busca.setGeometry(160, 110, 120, 23)
btn_busca.setText('Fazer a Busca')
btn_busca.setObjectName('btn_busca')
btn_busca.clicked.connect(onClik)

btn_limpar = QPushButton(window)
btn_limpar.setGeometry(330, 110, 120, 23)
btn_limpar.setText('Limpar campos')
btn_limpar.setObjectName('btn_limpar')
btn_limpar.clicked.connect(onClear)
# ****** END - BUTTONS ******

# ****** INIT - GROUP BOX ******
gpb_resultado = QGroupBox(window)
gpb_resultado.setGeometry(20, 140, 525, 251)
gpb_resultado.setTitle('Resultado')

# ------ INIT - GROUP BOX ------
ltw_resultado = QListWidget(gpb_resultado)
ltw_resultado.setGeometry(23, 39, 471, 201)
# ------ END - GROUP BOX ------

window.show()
sys.exit(app.exec())
# ****** END - APP ******