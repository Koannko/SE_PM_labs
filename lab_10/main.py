# Банковские услуги
# Кредит
# Рассрочка
# Вклад
# Расчёт процентов, графика платежей.
from pathlib import Path
import PySimpleGUI as sg
import paket.credit as cred
import paket.deposit as dep
import paket.installment as ins


def settings_window(settings):
    # ------ GUI Definition ------ #
    layout = [[sg.T("SETTINGS")],
              [sg.T("Separator"), sg.I(settings["CSV"]["separator"], s=1, key="-SEPARATOR-"),
               sg.T("Decimal"), sg.Combo(settings["CSV"]["decimal"].split("|"),
                                   default_value=settings["CSV"]["decimal_default"],
                                   s=1, key="-DECIMAL-"),
               sg.T("Sheet Name:"), sg.I(settings["EXCEL"]["sheet_name"], s=20, key="-SHEET_NAME-")],
              [sg.B("Save Current Settings", s=20)]]

    window = sg.Window("Банковские услуги", layout, modal=True, use_custom_titlebar=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Save Current Settings":
            # Write to ini file
            settings["CSV"]["separator"] = values["-SEPARATOR-"]
            settings["CSV"]["decimal_default"] = values["-DECIMAL-"]
            settings["EXCEL"]["sheet_name"] = values["-SHEET_NAME-"]

            # Display success message & close window
            sg.popup_no_titlebar("Settings saved!")
            break
    window.close()


def main_window():
    # ------ Menu Definition ------ #
    menu_def = [["Услуги", ["Кредит", "Рассрочка", "Вклад"]],
                ["Помощь", ["Настройки", "О нас", "Выход"]]]


    # ------ GUI Definition ------ #
    layout = [[sg.MenubarCustom(menu_def, tearoff=False)],[sg.T("Калькулятор кредита", s=55, justification="c")],
              [sg.T("Сумма кредита (в рублях): ", s=45, justification="r"), sg.I(key="summa")],
              [sg.T("Срок кредита (в годах): ", s=45, justification="r"), sg.I(key="years")], 
              [sg.T("Годовая ставка (в процентах): ", s=45, justification="r"), sg.I(key="percent")], 
              [sg.B('Рассчитать месячный платеж', s=45), sg.B('Рассчитать переплату по кредиту', s=45)],
              [sg.B("Сохранить отчёт по кредиту", s=45)],
              [sg.T("")],
              [sg.T("Калькулятор рассрочки", s=55, justification="c")],
              [sg.T("Сумма покупки (в рублях): ", s=45, justification="r"), sg.I(key="summa2")],
              [sg.T("Срок рассрочки (в месяцах): ", s=45, justification="r"), sg.I(key="month2")], 
              [sg.T("Процентная ставка: ", s=45, justification="r"), sg.I(key="percent2")], 
              [sg.B('Рассчитать месячный платеж по рассрочке', s=45), sg.B('Рассчитать переплату по рассрочке', s=45)],
              [sg.B("Сохранить отчёт по рассрочке", s=45)],
              [sg.T("")],
              [sg.T("Калькулятор вклада", s=55, justification="c")],
              [sg.T("Сумма вклада (в рублях): ", s=45, justification="r"), sg.I(key="summa3")],
              [sg.T("Срок вклада (в месяцах): ", s=45, justification="r"), sg.I(key="month3")], 
              [sg.T("Процентная ставка: ", s=45, justification="r"), sg.I(key="percent3")], 
              [sg.B('Рассчитать доход по вкладу за весь период', s=45), sg.B('Рассчитать размер вклада на конец периода', s=45)],
              [sg.B("Сохранить отчёт по вкладу", s=45)],
              [],[],
              [sg.Exit(s=16, button_color="tomato"),sg.B("Настройки", s=16)],]

    window_title = settings["GUI"]["title"]
    window = sg.Window(window_title, layout, use_custom_titlebar=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "О нас":
            window.disappear()
            sg.popup(window_title, "Версия 1.0", "Калькулятор кредита", grab_anywhere=True)
            window.reappear()
        if event in ("Кредит", "Рассрочка", "Вклад"):
            sg.popup_error("Not yet implemented")
        if event in ('Рассчитать месячный платеж'):
            A = cred.month_pay(int(values["summa"]),int(values["years"]),int(values["percent"]))
            window.disappear()
            sg.popup(window_title, f'Ежемесячный платеж составит: {A} рублей', grab_anywhere=True)
            window.reappear()
        if event in ('Рассчитать переплату по кредиту'):
            E = cred.overpayment(int(values["summa"]),int(values["years"]),int(values["percent"]))
            window.disappear()
            sg.popup(window_title, f'Переплата по кредиту составит: {E} рублей', grab_anywhere=True)
            window.reappear()
        if event == "Сохранить отчёт по кредиту":
            cred.save_cred(int(values["summa"]),int(values["years"]),int(values["percent"]))


        if event in ('Рассчитать месячный платеж по рассрочке'):
            A = ins.month_pay(int(values["summa2"]),int(values["month2"]),int(values["percent2"]))
            window.disappear()
            sg.popup(window_title, f'Ежемесячный платеж составит: {A} рублей', grab_anywhere=True)
            window.reappear()
        if event in ('Рассчитать переплату по рассрочке'):
            E = ins.overpayment(int(values["summa2"]),int(values["month2"]),int(values["percent2"]))
            window.disappear()
            sg.popup(window_title, f'Переплата по рассрочке составит: {E} рублей', grab_anywhere=True)
            window.reappear()
        if event == "Сохранить отчёт по рассрочке":
            ins.save_ins(int(values["summa2"]),int(values["month2"]),int(values["percent2"]))


        if event in ('Рассчитать доход по вкладу за весь период'):
            A = dep.count_revenue(int(values["summa3"]),int(values["month3"]),int(values["percent3"]))
            window.disappear()
            sg.popup(window_title, f'Доход по вкладу за весь период: {A} рублей', grab_anywhere=True)
            window.reappear()
        if event in ('Рассчитать размер вклада на конец периода'):
            E = dep.count_dep(int(values["summa3"]),int(values["month3"]),int(values["percent3"]))
            window.disappear()
            sg.popup(window_title, f'Размер вклада на конец периода: {E} рублей', grab_anywhere=True)
            window.reappear()
        if event == "Сохранить отчёт по вкладу":
            dep.save_dep(int(values["summa3"]),int(values["month3"]),int(values["percent3"]))
                
    window.close()


if __name__ == "__main__":
    SETTINGS_PATH = Path.cwd()
    # create the settings object and use ini format
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="config.ini", use_config_file=True, convert_bools_and_none=True
    )
    # theme = settings["GUI"]["theme"]
    # font_family = settings["GUI"]["font_family"]
    # font_size = int(settings["GUI"]["font_size"])
    # sg.theme(theme)
    # sg.set_options(font=(font_family, font_size))
    main_window()