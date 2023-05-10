from abc import ABC, abstractmethod
from datetime import date, timedelta
import calendar

class BankService(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass
    
    @abstractmethod
    def calculate_month_payment(self):
        pass

    @abstractmethod
    def calculate_amount_of_payment(self):
        pass

    @abstractmethod
    def calculate_overpayments(self):
        pass

    @abstractmethod
    def pay_month_payment(self):
        pass

    @abstractmethod
    def check_input(self):
        pass

    @abstractmethod
    def activate(self):
        pass

class Credit(BankService):
    def __init__(self, amount, interest, period):
        self.amount = amount
        self.interest = interest
        self.period = period
        self.debt = amount
        self.date = date.today()
        self.current_month = 0

    def calculate_interest(self):
        return round(self.debt * self.interest / 1200, 2)
    
    def calculate_month_payment(self):
        return self.amount * self.interest / \
                1200 * (1 + self.interest / 1200) ** self.period / \
                ((1 + self.interest / 1200) ** self.period - 1)
    
    def calculate_amount_of_payment(self):
        return self.calculate_month_payment() * self.period
    
    def calculate_overpayments(self):
        return self.calculate_amount_of_payment() - self.amount
    
    def calculate_main_debt(self):
        return self.calculate_month_payment() - self.calculate_interest()
    
    def get_date_of_payment(self):
        days = calendar.monthrange(self.date.year, self.date.month)[1]
        self.date += timedelta(days=days)
        month = calendar.month_abbr[self.date.month]
        return f'{month} {self.date.day}, {self.date.year}'

    def pay_month_payment(self):
        self.debt -= self.calculate_main_debt()
        self.current_month += 1

        if round(self.debt) == 0:
            self.debt = round(self.debt, 1)

    def check_input(self):
        try:
            self.amount = float(self.amount)
            self.interest = float(self.interest)
            self.period = int(self.period) 
            # self.amount <= 0 or self.interest <= 0 or self.period <= 0
        except:    
            return f'Вы ввели недопустимые данные: {self.amount}, {self.interest}, {self.period}. Кредит не может быть рассчитан.'
        return True

    def activate(self):
        if self.check_input() != True:
            return self.check_input()
        compute_list = [['Ежемесячный платёж', round(self.calculate_month_payment(), 2)],
                    ['Переплата по кредиту', round(self.calculate_overpayments(), 2)],
                    ['Сумма кредита', self.amount],
                    ['График платежей', self.period]]
        data_list = []
        while self.current_month < self.period:
            self.pay_month_payment()
            data_list.append([['№', str(self.current_month).zfill(2)],
                            ['Дата платежа', self.get_date_of_payment()],
                            ['Платёж в месяц', round(self.calculate_month_payment(), 2)],
                            ['Основной долг', round(self.calculate_main_debt(), 2)],
                            ['Проценты', round(self.calculate_interest(), 2)],
                            ['Остаток', round(self.debt, 2)]])     
        return data_list, compute_list
        
def create_credit(amount, interest, period):
    credit = Credit(amount, interest, period)
    return credit
