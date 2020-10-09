"""
@Author: your name
@Date: 2020-01-12 15:32:35
@LastEditTime: 2020-07-05 18:28:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Other\MergePDF.py
"""
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

from PyPDF4 import PdfFileReader, PdfFileWriter
from xlrd import open_workbook

root = tk.Tk()
# root.title("MergePDF")
root.withdraw()


def getFileName(filepath):
    try:
        excel_file = filedialog.askopenfilename(
            title="选择编辑好的Excel", filetypes=[("Excel", "*.xlsx"), ("All files", "*")]
        )
        wb = open_workbook(excel_file)
        tb = wb.sheets()[0]
        File_list = []
        for r in range(tb.nrows):
            val = []
            for c in range(tb.ncols):
                val.append(filepath + tb.cell_value(r, c))
            File_list.append((val))
        return File_list
    except Exception as err:
        print("Somthing went wrong")
        print(err)
        sys.exit()


def MergePDF(filepath):
    try:
        in_file_path = filepath + r"\input\\"
        pdf_fileName = getFileName(in_file_path)
        for pdfnames in pdf_fileName:
            output = PdfFileWriter()
            for pdfname in pdfnames:
                input = PdfFileReader(open(pdfname, "rb"))
                pageCount = input.getNumPages()
                for iPage in range(0, pageCount):
                    output.addPage(input.getPage(iPage))
            pdfoutname = str(pdfnames[0]).replace("input", "output")
            outputStream = open(pdfoutname, "wb")
            output.write(outputStream)
            outputStream.close()
        messagebox.showinfo("Complete!", "Complete!")
    except Exception as err:
        print("Something went wrong")
        print(err)
        sys.exit()


if __name__ == "__main__":
    file_dir = os.getcwd()
    if not os.path.exists(file_dir + "\\input"):
        os.mkdir(file_dir + "\\input")
    if not os.path.exists(file_dir + "\\output"):
        os.mkdir(file_dir + "\\output")
    messagebox.showinfo(
        "Important Message", "请将PDF文件放入input文件夹中，合并完成后的PDF文件在output文件夹中"
    )
    MergePDF(file_dir)
