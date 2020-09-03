import xlwt

xls = xlwt.Workbook()

sheet = xls.add_sheet("sheet")
table_name = ['需求名称', '所属模块', '一级模块', '二级模块', '优先级', '前置步骤', '操作步骤', '期望结果', '测试结果', '备注', '测试人']
# 使用write的方法，写入，write(行，列，值)，下标从0开始，就是第一行开始
# 当前表示，第一行第一列中，写入：字段1
#写入第一行
for i in range (11):
    sheet.write(0, i, table_name[i])




#使用save保存
xls.save('./test.xls')


