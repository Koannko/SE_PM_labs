import pyforms
from classes import *
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlTextArea

class GUI(BaseWidget):

    def __init__(self):
        super(GUI,self).__init__('Банковский сервис')

        #Definition of the forms fields
        self._amount_cr  = ControlText('Сумма кредита')
        self._interest_cr = ControlText('Процентная ставка')
        self._period_cr = ControlText('Срок кредитования')
        self._overpay_cr = ControlText('Сумма переплат')
        self._table_cr = ControlTextArea('График платежей')
        self._button_cr = ControlButton('Рассчитать')

        self._amount_rs  = ControlText('Сумма кредита')
        self._interest_rs = ControlText('Процентная ставка')
        self._period_rs = ControlText('Срок кредитования')
        self._overpay_rs = ControlText('Сумма переплат')
        self._table_rs = ControlTextArea('График платежей')
        self._button_rs = ControlButton('Рассчитать')

        #Define the button action
        self._button_cr.value = self.__buttonAction_credit
        self._button_rs.value = self.__buttonAction_rs
        self.formset = [ {
        'Кредит':['_amount_cr', '=', '_interest_cr', '=', '_period_cr', '=', '_overpay_cr', '=', '_table_cr', '=','_button_cr', '='],
        'Рассрочка':['_amount_rs', '=', '_interest_rs', '=', '_period_rs', '=', '_overpay_rs', '=', '_table_rs', '=', '_button_rs', '=']
            },
        ]
        
    def __buttonAction_credit(self):
        """Button action event"""
        amount_str = float(self._amount_cr.value)
        interest_str = self._interest_cr.value
        period_str = self._period_cr.value

        credit = Credit(amount_str, interest_str, period_str)
        
        if not amount_str or not interest_str or not period_str or not credit.check_input():
            self._table_cr.value = 'Error: Please enter all values'
            return

        data = credit.activate()
        data_str = ''
        for i in range(0, len(data[0])):
            for j in range(0, len(data[0][i])):
                for k in range(0, len(data[0][i][j])):
                    data_str += "".join(str(data[0][i][j][k])) + '    '
            self._table_cr += data_str + '\n'
            data_str = ''

        self._overpay_cr.value = str(data[1][1][1])


    def __buttonAction_rs(self):
        """Button action event"""
        amount_str = float(self._amount_rs.value)
        interest_str = self._interest_rs.value
        period_str = self._period_rs.value

        credit = Credit(amount_str, interest_str, period_str)
        
        if not amount_str or not interest_str or not period_str or not credit.check_input():
            self._table_cr.value = 'Error: Please enter all values'
            return

        data = credit.activate()
        data_str = ''
        for i in range(0, len(data[0])):
            for j in range(0, len(data[0][i])):
                for k in range(0, len(data[0][i][j])):
                    data_str += "".join(str(data[0][i][j][k])) + '    '
            self._table_rs += data_str + '\n'
            data_str = ''

        self._overpay_rs.value = str(data[1][1][1])

if __name__ == "__main__": pyforms.start_app( GUI )