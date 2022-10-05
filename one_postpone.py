from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

# GUI FILE
from ui_one_postpone import Ui_Form


class OnePostpone(QWidget):
    def __init__(self):
        super(OnePostpone, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.timeEdit.setTime(QTime.currentTime().addSecs(-15 * 60))
        self.ui.timeEdit_2.setTime(QTime.currentTime())

        self.ui.pushButton_delete.clicked.connect(self.postpone_event)
        self.ui.pushButton_close.clicked.connect(self.close_event)
        self.ui.pushButton_add.clicked.connect(self.add_record_event)

    def postpone_event(self):
        print('in postpone_event at onePopUp')
        print(self.sender())
        print('_________out postpone_event at onePopUp')
        return self.sender()

    def close_event(self):
        print('onePopUp : close event')
        print('end_________onePopUp : close event')
        return self.sender()

    def add_record_event(self):
        print('in add_recordEvent at onePopUp')
        print(self.sender())
        print('_________out add_recordEvent at onePopUp')
        return self.sender()


# class PopupMain(QDialog):
#     def __init__(self, main_window=None):
#         super(PopupMain, self).__init__(parent=None)
#         self.address_of_main_window = main_window
#         self.list_of_tuples_item_widget = list()
#         self.ui.pushButton_show_main_window.clicked.connect(self.slot_show_main_window)
#         self.ui.pushButton_postpone_all.clicked.connect(self.slot_postpone_all)
#         self.ui.pushButton_add_extra_record.clicked.connect(self.slot_add_new)
#         self.ui.pushButton_close_all.clicked.connect(self.slot_close_all)
#
#     def slot_show_main_window(self):
#         self.hide()
#
#     def slot_postpone_all(self):
#         j = 0
#         while j < self.listWidget.count():
#             item_to_unhide = self.listWidget.item(j)
#             print(item_to_unhide)
#             item_to_unhide.setHidden(True)
#             j += 1
#
#     def slot_close_all(self):
#         j = 0
#         while j < self.listWidget.count():
#             print(j, self.listWidget.count())
#             item_to_unhide = self.listWidget.item(j)
#             print(item_to_unhide)
#             # if not item_to_unhide.isHidden:
#             i = self.listWidget.takeItem(j)
#             print('i={}'.format(i))
#             # j += 1
#
#     def slot_add_new(self):
#         self.hide()
#         j = 0
#         while j < self.listWidget.count():
#
#             item_to_unhide = self.listWidget.item(j)
#             print(item_to_unhide)
#             if item_to_unhide.isHidden:
#                 item_to_unhide.setHidden(False)
#             j += 1
#         # Creating  a new list widget item whose parent is the listwidget itself
#         # QListWidgetItem * listWidgetItem = new QListWidgetItem(ui->listWidget);
#         list_widget_item = QListWidgetItem(self.listWidget)
#         list_widget_item.setFlags(list_widget_item.flags() & ~Qt.ItemIsSelectable)
#         # list_widget_item.setFlags(list_widget_item.flags() & ~Qt.ItemIsSelectable)
#         # Adding the item to the listwidget
#         # ui->listWidget->addItem(listWidgetItem);
#         self.listWidget.addItem(list_widget_item)
#         # Creating an object of the designed widget which is to be added to the listwidget
#         # TheWidgetItem * theWidgetItem = new TheWidgetItem;
#         inst_pop_up = OnePopUp()
#         # inst_pop_up.timeEdit.setTime(QTime.currentTime().addSecs(-15 * 60))
#         # inst_pop_up.timeEdit_2.setTime(QTime.currentTime())
#         inst_pop_up.pushButton_postpone.pressed.connect(self.button_postpone_pressed_slot)
#         inst_pop_up.pushButton_close.clicked.connect(self.button_close_pressed_slot)
#         inst_pop_up.pushButton_add.pressed.connect(self.button_add_pressed_slot)
#         # Making sure that  the listWidgetItem has the same size as the TheWidgetItem
#         # listWidgetItem->setSizeHint(theWidgetItem->sizeHint());
#         list_widget_item.setSizeHint(inst_pop_up.frameSize())
#         # print(inst_pop_up.dockWidget.testAttribute())
#         inst_pop_up.label_header.setText('test')
#         # Finally adding the itemWidget to  the list
#         # ui->listWidget->setItemWidget(listWidgetItem, theWidgetItem);
#         self.listWidget.setItemWidget(list_widget_item, inst_pop_up)
#         self.list_of_tuples_item_widget.append((list_widget_item, inst_pop_up))
#         print('list_widget_item, inst_pop_up = {}, {}'.format(list_widget_item, inst_pop_up))
#         self.show()
#
#     def button_postpone_pressed_slot(self):
#         print('in button_postpone_pressed_slot at popupMain')
#         item = None
#         # print(self.sender())
#         pointer_to_widget = self.sender().parent().parent()
#         print(pointer_to_widget)
#         for list_item in self.list_of_tuples_item_widget:
#             if list_item[1] == pointer_to_widget:
#                 item = list_item[0]
#         print('item is {}'.format(item))
#         item.setHidden(True)
#         print('_________out of button_postpone_pressed_slot at popupMain')
#
#     def button_close_pressed_slot(self):
#         print('in button_close_pressed_slot at popupMain')
#         item = None
#         # print(self.sender())
#         pointer_to_widget = self.sender().parent().parent()
#         print(pointer_to_widget)
#         for list_item in self.list_of_tuples_item_widget:
#             if list_item[1] == pointer_to_widget:
#                 item = list_item[0]
#         print('item is {}'.format(item))
#         row = self.listWidget.row(item)
#         print('row={}'.format(row))
#         i = self.listWidget.takeItem(row)
#         print('i={}'.format(i))
#         print('__________out of button_close_pressed_slot at popupMain')
#
#     def button_add_pressed_slot(self):
#         print('in button_add_pressed_slot at popupMain')
#         onePopUp_instance = self.sender().parent().parent()
#         print(onePopUp_instance)
#         time_range_arg = dict(time_start=onePopUp_instance.timeEdit.time(),
#                               time_end=onePopUp_instance.timeEdit_2.time())
#         self.address_of_main_window.add_item_records(time_range=time_range_arg)
#         print('_______out of button_add_pressed_slot at popupMain')
