import pdfplumber
from openpyxl import Workbook
# with pdfplumber.open("ANSI HI 14.6 -2016.pdf") as pdf:
#     for page in pdf.pages:
#         text = page.extract_text()
#         print(text)
workbook = Workbook()
sheet = workbook.active
with pdfplumber.open("ANSI HI 14.6 -2016.pdf") as pdf:
    for page in pdf.pages[20:21]:
        table = page.extract_table(table_settings={
            "vertical_strategy": "text",
            "horizontal_strategy": "text",
        })
        print(table)
        for row in table:
            # if not "".join([str(item) for item in row]) == "":
            print(row)
            sheet.append(row)
workbook.save(filename="1.xlsx")
