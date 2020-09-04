import os

from win32com.client import DispatchEx

name_lists = []
for name in os.listdir(os.path.join(os.getcwd(), "tmp")):
    if name.endswith(".xlsx"):
        name_lists.append(name)
xlApp = DispatchEx("Excel.Application")
xlApp.Visible = False
xlApp.DisplayAlerts = 0
for name_list in name_lists:
    filename = os.path.join(os.getcwd(), "tmp", name_list)
    exportfile = filename.split('.')[0] + '.pdf'
    books = xlApp.Workbooks.Open(filename, False)
    books.ExportAsFixedFormat(0, exportfile)
    books.Close(False)
    print('保存 PDF 文件：', exportfile)
xlApp.Quit()
