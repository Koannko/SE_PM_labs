import pyforms
from classes import *
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlTextArea
from   pyforms.controls import ControlCombo
from   pyforms.controls import ControlCheckBox

class GUI(BaseWidget):

    def __init__(self):
        super(GUI,self).__init__('Банковский сервис')

        #Definition of the forms fields
        self._amount_cr  = ControlText('Сумма кредита')
        self._interest_cr = ControlText('Процентная ставка')
        self._period_cr = ControlText('Срок кредитования')
        self._overpay_cr = ControlText('Сумма переплат')
        self._payment_cr = ControlText('Ежемесячный платеж')
        self._table_cr = ControlTextArea('График платежей')
        self._button_cr = ControlButton('Рассчитать')
        self._button_save_cr = ControlButton('Сохранить отчёт')
        self._button_cr.value = self.__buttonAction_cr
        self._button_save_cr.value = self.__buttonSave_cr

        self._amount_ins  = ControlText('Сумма кредита')
        self._interest_ins = ControlText('Процентная ставка')
        self._period_ins = ControlText('Срок кредитования')
        self._overpay_ins = ControlText('Сумма переплат')
        self._payment_ins = ControlText('Средний платеж в месяц')
        self._table_ins = ControlTextArea('График платежей')
        self._button_ins = ControlButton('Рассчитать')
        self._button_save_ins = ControlButton('Сохранить отчёт')
        self._button_ins.value = self.__buttonAction_ins
        self._button_save_ins.value = self.__buttonSave_ins

        self._amount_dep  = ControlText('Сумма вклада')
        self._period_dep = ControlText('Срок размещения')
        self._interest_dep = ControlText('Процентная ставка')
        self._additions_dep = ControlCombo('Пополнение вклада')
        self._overpay_dep = ControlText('Доход')
        self._payment_dep = ControlText('Сумма в конце срока')
        self._table_dep = ControlTextArea('График начислений')
        self._additions_dep.add_item('Не предусмотрено')
        self._additions_dep.add_item('Каждый месяц')
        self._additions_dep.add_item('Каждый квартал')
        self._additions_dep.add_item('Каждый год')
        self._interest_type_dep = ControlCheckBox('Добавлять начисления ко вкладу')
        self._amount_of_additions = ControlText('Сумма пополнений вклада')
        self._button_dep = ControlButton('Рассчитать')
        self._button_save_dep = ControlButton('Сохранить отчёт')
        self._button_dep.value = self.__buttonAction_dep
        self._button_save_dep.value = self.__buttonSave_dep


        self.formset = [ {
        'Кредит':['_amount_cr', '||', '_interest_cr', '||', '_period_cr', '=', ' ', '_overpay_cr', '=', '_payment_cr', '=', '_table_cr', '=','_button_cr', '=', '_button_save_cr', '='],
        'Рассрочка':['_amount_ins', '||', '_interest_ins', '||', '_period_ins', '=', ' ', '_overpay_ins', '=', '_payment_ins', '=', '_table_ins', '=', '_button_ins', '=', '_button_save_ins', '='],
        'Вклад':['_amount_dep', '||', '_period_dep', '||', '_interest_dep', '=', '_additions_dep', '=', '_interest_type_dep', '||', '_amount_of_additions', '=', '_overpay_dep', '||', '_payment_dep', '=', '_table_dep', '=', '_button_dep', '=', '_button_save_dep']    
            },
        ]

        self.copy_num_cr = 0
        self.copy_num_ins = 0
        self.copy_num_dep = 0



    def __buttonAction_dep(self):
        interest_type = self._interest_type_dep.value
        amount_of_additions = self._amount_of_additions.value
        additions = self._additions_dep.value
        amount_str = self._amount_dep.value
        interest_str = self._interest_dep.value
        period_str = self._period_dep.value
        
        if amount_str == '' or not interest_str or not period_str:
            self._table_dep.value = 'Error: Please enter all values'
            return
        elif self._additions_dep.value != 'Не предусмотрено':
            if self._amount_of_additions.value == '':
                self._table_dep.value = 'Error: Please enter all values'
                return

        deposit = Deposit(float(amount_str), interest_str, period_str, interest_type, additions, amount_of_additions)
        data = deposit.activate()
        data_str = '№         Дата платежа                Начислено процентов               Пополнение вклада               Остаток вклада\n'
        self._table_dep.value = ''
        for i in range(0, len(data[0])):
            for j in range(0, len(data[0][i])):
                data_str += ''.join(str(data[0][i][j][1])) + \
                            ''.join(map(lambda _: ' ', range(25 + int(len(str(data[0][i][j][1])) * 1.2))))
            self._table_dep += data_str + '\n'
            data_str = ''

        self._overpay_dep.value = str(data[1][1][1])
        self._payment_dep.value = str(data[1][0][1])

    def __buttonSave_dep(self):
        amount_str = float(self._amount_dep.value)
        interest_str = self._interest_dep.value
        period_str = self._period_dep.value

        if amount_str == '' or not interest_str or not period_str:
            self._table_dep.value = 'Error: Please enter all values'
            return
        elif self._additions_dep.value != 'Не предусмотрено':
            if self._amount_of_additions.value == '':
                self._table_dep.value = 'Error: Please enter all values'
                return
        
        deposit = Deposit(float(amount_str), interest_str, period_str, self._interest_type_dep.value, self._additions_dep.value, self._amount_of_additions.value)
        data_lst, compute_list = deposit.activate()
        deposit.save_docx(data_lst, compute_list, self.copy_num_dep)
        self.copy_num_dep += 1
        

















    def __buttonAction_cr(self):
        amount_str = float(self._amount_cr.value)
        interest_str = self._interest_cr.value
        period_str = self._period_cr.value

        credit = Credit(amount_str, interest_str, period_str)
        
        if not amount_str or not interest_str or not period_str or not credit.check_input():
            self._table_cr.value = 'Error: Please enter all values'
            return

        data = credit.activate()
        data_str = '№                   Дата платежа                Платёж в месяц              Основной долг              Проценты                 Остаток\n'
        self._table_cr.value = ''
        for i in range(0, len(data[0])):
            for j in range(0, len(data[0][i])):
                data_str += ''.join(str(data[0][i][j][1])) + \
                            ''.join(map(lambda _: ' ', range(15 + int(len(str(data[0][i][j][1])) * 1.2))))
            self._table_cr += data_str + '\n'
            data_str = ''

        self._overpay_cr.value = str(data[1][1][1])
        self._payment_cr.value = str(data[1][0][1])

    def __buttonSave_cr(self):
        amount_str = float(self._amount_cr.value)
        interest_str = self._interest_cr.value
        period_str = self._period_cr.value

        credit = Credit(amount_str, interest_str, period_str)

        if not amount_str or not interest_str or not period_str or not credit.check_input():
            self._table_cr.value = 'Error: Please enter all values'
            return
        
        data_lst = credit.activate()[0]
        credit.save_docx(data_lst, self.copy_num_cr)
        self.copy_num_cr += 1




    def __buttonAction_ins(self):
        amount_str = float(self._amount_ins.value)
        interest_str = self._interest_ins.value
        period_str = self._period_ins.value

        installment = Installment(amount_str, interest_str, period_str)
        
        if not amount_str or not interest_str or not period_str or not installment.check_input():
            self._table_ins.value = 'Error: Please enter all values'
            return

        data = installment.activate()
        data_str = '№       Дата платежа    Платёж в месяц      Основной долг     Проценты       Остаток\n'
        self._table_ins.value = ''
        for i in range(0, len(data[0])):
            for j in range(0, len(data[0][i])):
                data_str += ''.join(str(data[0][i][j][1])) + \
                            ''.join(map(lambda _: ' ', range(15 + int(len(str(data[0][i][j][1])) * 1.2))))
            self._table_ins += data_str + '\n'
            data_str = ''

        self._overpay_ins.value = str(data[1][1][1])
        self._payment_ins.value = str(data[1][0][1])


    def __buttonSave_ins(self):
        amount_str = float(self._amount_ins.value)
        interest_str = self._interest_ins.value
        period_str = self._period_ins.value

        installment = Installment(amount_str, interest_str, period_str)

        if not amount_str or not interest_str or not period_str or not installment.check_input():
            self._table_ins.value = 'Error: Please enter all values'
            return
        
        data_lst = installment.activate()[0]
        installment.save_docx(data_lst, self.copy_num_ins)
        self.copy_num_ins += 1





if __name__ == "__main__": pyforms.start_app( GUI )