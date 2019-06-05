# coding=utf-8
"""This is a tool to crop paper pdf to the kindle size
author: FindHao(find@findspace.name)"""
from PyPDF2 import PdfFileWriter, PdfFileReader
from copy import copy
# todo: 暴力裁剪会切断行
import sys

file_name = sys.argv[1]
margin = int(sys.argv[2])

output = PdfFileWriter()
input1 = PdfFileReader(open(file_name, "rb"))
# 阅读顺序应该是
# 1 3
# 2 4
for page in input1.pages:
    # 由于PyPDF2的一些原因，无法做成循环形式，所以只能写成这么丑陋的。。
    upperleft_x = page.mediaBox.getUpperLeft_x()
    upperleft_y = page.mediaBox.getUpperLeft_y()
    upperright_x = page.mediaBox.getUpperRight_x()
    upperright_y = page.mediaBox.getUpperRight_y()
    lowerleft_x = page.mediaBox.getLowerLeft_x()
    lowerleft_y = page.mediaBox.getLowerLeft_y()
    lowerright_x = page.mediaBox.getLowerRight_x()
    lowerright_y = page.mediaBox.getLowerRight_y()

    new_page = copy(page)
    new_page.cropBox.lowerLeft = (lowerleft_x + margin, lowerleft_y)
    new_page.cropBox.upperLeft = (upperleft_x + margin, upperleft_y)
    new_page.cropBox.lowerRight = (lowerright_x - margin, lowerright_y)
    new_page.cropBox.upperRight = (upperright_x - margin, upperright_y)
    output.addPage(new_page)


outputStream = open(file_name[:-4]+"_croped.pdf", "wb")
output.write(outputStream)
