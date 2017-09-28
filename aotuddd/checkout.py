import xlrd
from xlutils.copy import copy
class checkout():
    def check(self,msg,exp,i):
        if msg==exp:
            date1=xlrd.open_workbook('D:\\testcase.xls')
            wb=copy(date1)
            ws=wb.get_sheet(1)
            ws.write(i,9,'通过')
            wb.save('D:\\testcase.xls')
        else:
            date1=xlrd.open_workbook('D:\\testcase.xls')
            wb=copy(date1)
            ws=wb.get_sheet(1)
            ws.write(i,9,'失败')
            wb.save('D:\\testcase.xls')
