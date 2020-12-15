from openpyxl import Workbook,load_workbook
from datetime import date
def create_excel_sheet(data):
    today = date.today()
    filename = today.strftime("%b-%d-%Y")
    filename = filename + '.xlsx'
    try:
        workbook = load_workbook(filename)
        sheet=workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active
        sheet['A1'] = "REGISTRATION NO"
        sheet['B1'] = "TIME"

    sheet.append(data)
    workbook.save(filename=filename)