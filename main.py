################################################################################
#
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
################################################################################
# TODO Recursion in back thread
# TODO Button To Favorites
# TODO Login Form
# TODO Telegram
# TODO Update
# TODO Local Database
# TODO .exe
import datetime
import os
import sys
import time

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PyQt6.QtCore import pyqtSlot
from PySide6.QtCore import Slot

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
from datetime import date
from app_functions import *
from waitingspinnerwidget import QtWaitingSpinner
from one_pop_up import OnePopUp
from one_postpone import OnePostpone

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Step 2: Create a QThread object
        self.worker = Worker()
        # Step 3: Create a worker object
        self.thread = QThread(parent=None)

        self.search_worker = Worker()
        self.search_thread = QThread(parent=None)

        # Creating and setting up timer
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(10 * 1000)
        self.timer.timeout.connect(self.postpone_update)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        today = date.today()
        self.rw_list = []
        self.ui.label_date.setText(today.strftime("%B %d, %Y"))
        self.ui.label_acc_name.setText("Not Logged in")
        self.spinner = QtWaitingSpinner(self.ui.centralwidget)

        # TOGGLE/BURGER MENU
        ########################################################################
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggle_menu(self, 180, True))

        # PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(self.change_page)

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(self.change_page)

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(self.change_page)

        # PAGE 3 - Search button
        self.ui.btn_search.clicked.connect(self.train_search)

        # PAGE 4
        self.ui.btn_page_4.clicked.connect(self.change_page)

        self.ui.btn_notifications.clicked.connect(lambda: print('PyQt5 button click Notifications\n'))
        self.ui.btn_settings.clicked.connect(lambda: print('PyQt5 button click Settings\n'))

        self.ui.btn_page_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END

    def change_page(self):
        self.ui.btn_page_1.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.ui.btn_page_2.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.ui.btn_page_3.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ui.btn_page_4.setStyleSheet("background-color: rgb(120, 120, 120);")

        sender = self.sender()
        sender.setStyleSheet("background-color: white; border-radius: 30px;")

        if sender == self.ui.btn_page_1:
            print('PyQt5 button click 1\n')
            page = self.ui.page_1
        elif sender == self.ui.btn_page_2:
            print('PyQt5 button click 2\n')
            page = self.ui.page_2
            if not self.ui.list_transport.count():
                self.urban_search()
        elif sender == self.ui.btn_page_3:
            print('PyQt5 button click 3\n')
            page = self.ui.page_3
        else:
            print('PyQt5 button click 4\n')
            page = self.ui.page_4

        self.ui.Pages_Widget.setCurrentWidget(page)

    def urban_search(self):
        self.spinner.start()
        self.ui.Pages_Widget.setVisible(False)

        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run_urban)
        self.worker.finished.connect(self.thread.quit)
        # Step 6: Start the thread
        self.thread.start()
        self.worker.finished.connect(self.urban_loaded)

    def train_search(self):
        self.ui.list_railway.clear()
        departure = self.ui.line_departure.text()
        arrive = self.ui.line_arrival.text()
        calendar_date = self.ui.dateEdit.date()
        current_date_edit = QDateEdit()
        current_date_edit.setDisplayFormat("yyyy-MM-dd")
        current_date_edit.setDate(calendar_date)
        current_date = current_date_edit.text()
        generated_url = f'https://pass.rw.by/ru/route/?from={departure}&to={arrive}&date={current_date}'
        self.worker.rw_url[0] = generated_url
        self.spinner.start()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run_rw)
        self.worker.finished.connect(self.thread.quit)
        # Step 6: Start the thread
        self.thread.start()
        self.worker.finished.connect(self.rw_loaded)

    def urban_loaded(self, transport_list):
        self.ui.list_transport.addItems(transport_list)
        self.spinner.stop()
        self.ui.Pages_Widget.setVisible(True)
        self.thread.started.disconnect(self.worker.run_urban)
        self.worker.finished.disconnect(self.thread.quit)
        self.worker.finished.disconnect(self.urban_loaded)

    # after getting data
    def rw_loaded(self, rw_list):
        print('RW_LOADED\n')
        # saving list to postpone
        self.rw_list = rw_list
        for number, item in enumerate(rw_list):
            list_widget_item = QListWidgetItem(self.ui.list_railway)
            inst_pop_up = OnePopUp()
            inst_pop_up.ui.timeEdit.setTime(QTime.fromString(item['train_departure'], "hh:mm"))
            inst_pop_up.ui.timeEdit_2.setTime(QTime.fromString(item['train_arrive'], "hh:mm"))
            inst_pop_up.ui.line_duration.setText(item['train_duration'])
            inst_pop_up.setMinimumSize(0, 180 + item['str_count'] * 30)
            inst_pop_up.ui.tickets_text.setText(item['tickets'])
            list_widget_item.setSizeHint(inst_pop_up.frameSize())
            inst_pop_up.ui.label_header.setText(f"{item['number']}: {item['train_name']}")
            inst_pop_up.ui.pushButton_postpone.clicked.connect(self.postpone_search)
            list_widget_item.setData(41, number)
            list_widget_item.setData(42, inst_pop_up.ui.pushButton_postpone)
            # Finally adding the itemWidget to the list
            # ui->listWidget->setItemWidget(listWidgetItem, theWidgetItem);
            self.ui.list_railway.setItemWidget(list_widget_item, inst_pop_up)
        self.spinner.stop()
        self.thread.started.disconnect(self.worker.run_rw)
        self.worker.finished.disconnect(self.thread.quit)
        self.worker.finished.disconnect(self.rw_loaded)

    def postpone_search(self):
        print(f'Postpone request came from {self.sender()}\n')
        number = ''
        # finding selected train
        for train in range(self.ui.list_railway.count()):
            # print(f'{str(self.ui.list_railway.item(train).data(42))}')
            # 42 - button address, 41 - train number
            if str(self.sender()) == str(self.ui.list_railway.item(train).data(42)):
                number = self.ui.list_railway.item(train).data(41)
        print(f'Selected {number} postpone button\n')
        self.search_worker.postpone_id.append(number)
        self.postpone_add([self.rw_list[number]])
        if self.search_worker.postpone_status == 0:
            self.postpone_start()

    def postpone_start(self):
        print('POSTPONE_START\n')
        self.search_worker.postpone_status = 1
        self.search_worker.moveToThread(self.search_thread)
        # Step 5: Connect signals and slots
        self.search_thread.started.connect(self.search_worker.run_rw_postpone)
        self.search_worker.parsed.connect(self.postpone_wait)
        self.search_worker.parsed.connect(self.search_thread.quit)
        self.search_worker.toexit.connect(self.postpone_finished)
        # Step 6: Start the thread
        self.search_thread.start()

    def postpone_add(self, rw_list):
        print(f'Tread is running: {self.search_thread.isRunning()}\n')
        print('POSTPONE_ADD\n')
        # print(rw_list)
        self.ui.edit_log.append('--------------------------------------------------------------------------------------')
        current_datetime = datetime.datetime.now()
        self.ui.edit_log.append(f"{current_datetime}")
        for number, item in enumerate(rw_list):
            list_widget_item = QListWidgetItem(self.ui.list_postpone)
            inst_pop_up = OnePostpone()

            inst_pop_up.ui.timeEdit.setTime(QTime.fromString(item['train_departure'], "hh:mm"))
            inst_pop_up.ui.timeEdit_2.setTime(QTime.fromString(item['train_arrive'], "hh:mm"))
            inst_pop_up.ui.line_duration.setText(item['train_duration'])
            inst_pop_up.setMinimumSize(0, 180 + item['str_count'] * 30)
            inst_pop_up.ui.tickets_text.setText(item['tickets'])
            list_widget_item.setSizeHint(inst_pop_up.frameSize())
            inst_pop_up.ui.label_header.setText(f"{item['number']}: {item['train_name']}")

            inst_pop_up.ui.pushButton_delete.clicked.connect(self.postpone_delete)
            list_widget_item.setData(41, item['number'] - 1)
            print(item['number'])
            list_widget_item.setData(42, inst_pop_up.ui.pushButton_delete)

            # Finally adding the itemWidget to the list
            # ui->listWidget->setItemWidget(listWidgetItem, theWidgetItem);
            self.ui.list_postpone.setItemWidget(list_widget_item, inst_pop_up)
            print(f"{item['train_name']} added\n")
            self.ui.edit_log.append(f"{item['number']}: {item['train_name']}")
            self.ui.edit_log.append(f"{item['tickets']}")
            if number != len(rw_list) - 1:
                self.ui.edit_log.append('')
        self.ui.edit_log.append('--------------------------------------------------------------------------------------')
        # self.spinner.stop()

    def postpone_wait(self, postpone_rw_list):
        self.ui.list_postpone.clear()
        self.postpone_add(postpone_rw_list)
        print('postpone_update: START_TIMER\n')
        self.timer.start()

    def postpone_update(self):
        print('POSTPONE_UPDATE\n')
        self.search_thread.start()

    def postpone_delete(self):
        print(f'Postpone delete request came from {self.sender()}\n')
        number = ''
        # finding selected train
        for train in range(self.ui.list_postpone.count()):
            print(f'{str(self.ui.list_postpone.item(train).data(42))}')
            # 42 - button address, 41 - train number
            if str(self.sender()) == str(self.ui.list_postpone.item(train).data(42)):
                number = self.ui.list_postpone.item(train).data(41)
        print(f'Selected {number} postpone button\n')
        print(f'xqwe {self.search_worker.postpone_id}')
        self.search_worker.postpone_id.remove(number)

    def postpone_finished(self):
        print("POSTPONE_FINISHED\n")
        self.search_thread.started.disconnect(self.search_worker.run_rw_postpone)
        self.search_worker.parsed.disconnect(self.postpone_wait)
        self.search_worker.parsed.disconnect(self.search_thread.quit)
        self.search_worker.toexit.disconnect(self.postpone_finished)
        self.search_worker.postpone_status = 0
        self.search_thread.quit()


# Step 1: Create a worker class
class Worker(QObject):
    finished = Signal(list)
    parsed = Signal(list)
    toexit = Signal()
    rw_url = ['https://pass.rw.by/ru/route/?from=Орша&to=Минск&date=2021-10-14']
    postpone_id = []
    postpone_status = 0

    def __init__(self):
        super().__init__()

    def run_urban(self):
        """Long-running task (Minsktrans)."""
        transport = MinskTransport()
        transport_list = transport.parse()
        print('Finished\n')
        self.finished.emit(transport_list)

    def run_rw(self):
        """Long-running task (RW.BY)."""
        print(f'Started with {self.rw_url[0]}\n')
        railway = Railway(self.rw_url[0])
        rw_list = railway.parse()
        print('Finished\n')
        self.finished.emit(rw_list)

    def run_rw_postpone(self):
        """Long-running task (RW.BY) PART 2."""
        print(f'run_rw_postpone: Started with {self.rw_url[0]}\n')

        railway = Railway(self.rw_url[0])
        rw_list = railway.parse()
        print('run_rw_postpone: PARSE_FINISHED\n')
        out_list = []
        for iter_id in self.postpone_id:
            print(f'{rw_list[iter_id]}\n')
            out_list.append(rw_list[iter_id])
        if len(self.postpone_id) == 0:
            self.toexit.emit()
        self.parsed.emit(out_list)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec())
