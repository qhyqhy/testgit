import xlrd,sys
from xlutils.copy import copy
import aotuddd.checkout as ccc
class Cases():
    def checklogin(self):
        datasrc='D:/testcase.xls'
        # 打开EXCEL文档
        datas=xlrd.open_workbook('D:/testcase.xls')
        # 获得EXCEL文档的第一张表
        sheet=datas.sheets()[1]
        # sheet1=datas.get_sheet(1)
        # sheet.nrows：sheet表的行数，sheet.ncols表示sheet表的列数
        for i in range(3,sheet.nrows):
            # 取第i行的值存入list中
            list=sheet.row_values(i)
            #list[0]第i行的第一列,是模块名
            module=list[0]
            # print(module)
            # 将woniuboss包下的WoniuBoss.py模块下的list[0]模块动态加载到内存中
            __import__('aotuddd.'+module)
            m=sys.modules['aotuddd.'+module]
            o=getattr(m,'Woniuboss')
            mtd=getattr(o(),list[1])

            msg=mtd(list[2],list[3],list[4],list[5],list[6])
            print(i)
            q=ccc.checkout()
            q.check(msg,list[7],i)

if __name__=="__main__":
    c=Cases()
    c.checklogin()




