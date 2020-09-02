from openpyxl import load_workbook
from openpyxl import workbook

#设置文件
file = "case.xlsx"
#打开文件
wb = workbook
#创建一张新表
ws = wb.create_sheet()
#第一行输入
ws.append(['需求', '模块', '一级模块', '二级模块', '用例名称', '优先级', '前置条件', '操作步骤', '期望结果', '测试结果', '备注', '测试人'])


wb.save("cases.xlsx")

