'''
Module main.py provides terminal user interface and interaction between modules.
'''


import sys
import npyscreen
from calc.operations import plus, minus, multi, divis, power
from calc.history import log_create, log_del, log_read


class FormObject(npyscreen.ActionForm, npyscreen.FormWithMenus):  # pylint: disable=too-many-ancestors
    '''Class of main page with menu. Here we have main functions of app.'''

    def create(self):
        self.show_atx = 1
        self.show_aty = 1

        self.oper_1 = self.add(npyscreen.TitleText, name='Operand #1:',	value='100',
                               begin_entry_at=15)
        self.nextrely += 1								

        self.oper_2 = self.add(npyscreen.TitleText, name='Operand #2:', value='2.2',
                               begin_entry_at=15)
        self.nextrely += 1								

        self.options = self.add(npyscreen.TitleSelectOne, max_height=5, name='Operation',
                                values=['+', '-', '*', '/', '**'], scroll_exit=True)
        self.nextrely += 1								

        self.result = self.add(npyscreen.TitleText,
                               name='Result: ', begin_entry_at=15)
        self.nextrely += 1								

        self.menu = self.new_menu('Main Menu')
        self.menu.addItem('About this app', self.about_app, 'a')
        self.menu.addItem('History', self.history, 'h')
        self.menu.addItem('Delete History', self.delete_history, 'd')
        self.menu.addItem('Exit', self.exit_app, 'q')

    def about_app(self):
        '''Give an 'About-App notification.'''
        npyscreen.notify_confirm('This is a simple TUI calculator. I\'ve made it.',
                                 'About this app')

    def history(self):
        '''Opens form of history page.'''
        self.parentApp.switchForm('HISTORY')

    def delete_history(self):
        '''Delete file .json from directory.'''
        npyscreen.notify_confirm(log_del())

    def exit_app(self):
        '''Close application with 3 sec notification delay.'''
        npyscreen.notify_wait('The app will be closed in 3 sec', 'Closing')
        sys.exit(0)

    def on_ok(self):

        try:
            a_num = float(self.oper_1.value)
            b_num = float(self.oper_2.value)

            if self.options.value == [0]:
                self.result.value = str(plus(a_num, b_num))
                oper = '+'

            if self.options.value == [1]:
                self.result.value = str(minus(a_num, b_num))
                oper = '-'

            if self.options.value == [2]:
                self.result.value = str('%.3f' % multi(a_num, b_num))
                oper = '*'

            if self.options.value == [3]:
                self.result.value = str('%.3f' % divis(a_num, b_num))
                oper = '/'

            if self.options.value == [4]:
                self.result.value = str('%.3f' % power(a_num, b_num))
                oper = '**'

            log_create(a_num, b_num, oper, self.result.value)

        except (ArithmeticError, ValueError) as error:
            self.result.value = str(error)
           
    def on_cancel(self):
        self.result.value, self.oper_1.value, self.oper_2.value = ' ', ' ', ' '


class HistoryPage(npyscreen.ActionForm):    # pylint: disable=too-many-ancestors
    '''History page class contans data stored in .json log file.'''

    def create(self):
        self.show_atx = 1
        self.show_aty = 1

        self.info = self.add(npyscreen.TitleText,
                             name='OK - refresh. CANCEL - exit.')
        self.nextrely += 1								

        self.show_history = self.add(npyscreen.MultiLineEdit)

    def on_ok(self):
        if log_read() is None:
            self.show_history.value = 'Log file is empty.'
        else:
            self.show_history.value = log_read()

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')


class App(npyscreen.NPSAppManaged):		
    '''Class of application manager which registers main form and history page.'''

    def onStart(self):
        self.addForm('MAIN', FormObject, name='TUI-Calculator',
                     lines=16, columns=50)  
        self.addForm('HISTORY', HistoryPage, name='History Page',
                     lines=16, columns=50)  


if __name__ == '__main__':
    APPLICATION = App().run()
