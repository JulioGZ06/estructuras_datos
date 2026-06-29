from PyQt5.QtWidgets import QApplication
import sys

from load.load_menu_principal import MenuPrincipal

app = QApplication(sys.argv)

ventana = MenuPrincipal()
ventana.show()

sys.exit(app.exec_())