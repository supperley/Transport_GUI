################################################################################
#
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
################################################################################

# ==> GUI FILE
from main import *


class UIFunctions(MainWindow):

    def __init__(self):
        super().__init__()

    def toggle_menu(self, max_width, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            max_extend = max_width
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
