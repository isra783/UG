from PySide6.QtWidgets import QMainWindow

from Ui.untitled import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    '''
    class que genera la logica de los objetos personas
    '''
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)










