from xmindparser import xmind_to_dict
import tkinter as tk
from tkinter import filedialog
import logging
import xlwt

def getcase(title, get_dict, count):
    try:
        xls = xlwt.Workbook()
        logging.info('创建Excel')
        # 设置单元格对齐方式
        alignment = xlwt.Alignment()
        # 自动换行
        alignment.wrap = 1
        # 设置样式
        style = xlwt.XFStyle()
        style.alignment = alignment
        logging.info('已设置Excel为自动换行')
        # 创建一个Sheet
        sheet = xls.add_sheet("sheet")
        # 设置行列的高宽
        tall_style = xlwt.easyxf('font:height 450')
        orther_style = xlwt.easyxf('font:height 1000')
        # 设置第一行的宽度
        first_row = sheet.row(0)
        first_row.set_style(tall_style)
        logging.info('已将第一行的宽度设置为450')
    except Exception as ex:
        logging.info("出现错误，如下：")
        logging.error(ex)

    try:
        table_name = \
            ['需求名称', '所属模块', '一级模块', '二级模块', '用例名称', '优先级', '前置步骤', '操作步骤', '期望结果', '测试结果', '备注', '测试人']
        # 设置列
        for i in range(11):
            sheet.write(0, i, table_name[i])
            if i == 4 or i == 6:
                sheet.col(i).width = 8888
                logging.info('第五行或第七行设置为8888')
            elif i == 7 or i == 8:
                sheet.col(i).width = 12888
                logging.info('第七行或第八行设置为12888')
            else:
                sheet.col(i).width = 4000
        logging.info('已写入第一行数据')
    except Exception as ex:
        logging.info("出现错误，如下：")
        logging.error(ex)

    try:
        print("需求名称：", title)
        get_case = get_dict["topic"]
        # 计算大模块数量
        get_num_module = len(get_case["topics"])
        logging.info('计算最大模块数量')
        # 1.进入大模块的循环中
        for i in range(0, get_num_module):
            # 进来后计算一级模块数量
            num_module_first = len(get_case["topics"][i]["topics"])
            logging.info('计算一级模块数量')
            # 获取大模块名称
            get_module_big = get_case["topics"][i]["title"]
            print("所属模块：", get_module_big)
            logging.info('获取大模块名称')
            # 2.进入一级模块
            for j in range(0, num_module_first):
                # 计算二级模块的数量
                num_module_second = len(get_case["topics"][i]["topics"][j]["topics"])
                logging.info('计算二级模块数量')
                # 获取一级模块的名称
                get_module_first = get_case["topics"][i]["topics"][j]["title"]
                print("一级模块：", get_module_first)
                logging.info('获取一级模块名称')
                # 3.进入二级模块
                for a in range(0, num_module_second):
                    # 计算二级模块下的用例数
                    num_case = len(get_case["topics"][i]["topics"][j]["topics"][a]["topics"])
                    logging.info('计算用例数')
                    # 获取二级模块名称
                    get_module_second = get_case["topics"][i]["topics"][j]["topics"][a]["title"]
                    print("二级模块：", get_module_second)
                    logging.info('获取二级模块名称')
                    # 4.进入每一条用例中
                    for b in range(0, num_case):
                        # 获取测试用例名字
                        case_name = get_case["topics"][i]["topics"][j]["topics"][a]["topics"][b]["title"]
                        print("用例名称：", case_name)
                        logging.info('获取用例名称')
                        # 获取测试用例的优先级
                        get_priority = get_case["topics"][i]["topics"][j]["topics"][a]["topics"][b]["makers"][0]
                        if get_priority == "priority-1":
                            priority = "S"
                        elif get_priority == "priority-2":
                            priority = "A"
                        elif get_priority == "priority-3":
                            priority = "B"
                        elif get_priority == "priority-4":
                            priority = "C"
                        else:
                            priority = "D"
                        print("优先级：", priority)
                        logging.info('获取用例优先级')
                        # 获取前置步骤
                        step_first = get_case["topics"][i]["topics"][j]["topics"][a]["topics"][b]["topics"][0]["title"]
                        print("前置步骤：", step_first)
                        logging.info('获取前置步骤')
                        # 获取操作步骤
                        step = get_case["topics"][i]["topics"][j]["topics"][a]["topics"][b]["topics"][1]["title"]
                        print("操作步骤：", step)
                        logging.info('获取操作步骤')
                        # 获取期望结果
                        hope_result = \
                            get_case["topics"][i]["topics"][j]["topics"][a]["topics"][b]["topics"][1]["topics"][0][
                                "title"]
                        print("期望结果", hope_result)
                        logging.info('获取期望结果')
                        # 收集用例信息
                        case_info = [title, get_module_big, get_module_first, get_module_second, case_name,
                                     priority, step_first, step, hope_result]
                        # 写入Excel
                        for s in range(9):
                            sheet.write(count, s, case_info[s], style)
                            orther_row = sheet.row(count)
                            orther_row.set_style(orther_style)
                        count += 1
                        logging.info('本条用例写入Excel成功')
        xls.save('./case.xls')
    except Exception as ex:
        logging.info("出现错误，如下：")
        logging.error(ex)

    logging.info('用例已保存')
    return 1


if __name__ == "__main__":
        #设置日志日式
        logging.basicConfig(level=logging.INFO,
                            filename='log.log',
                            filemode='w',
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        count = 1
        #读取文件
        try:
            root = tk.Tk()
            root.withdraw()
            f_path = filedialog.askopenfilename()
            data = xmind_to_dict(f_path)
            logging.info("开始读取文件")
            # 获取列表中的字典
            get_dict = data[0]
            logging.info("文件读取成功")
            # 获取需求的名称
            title = get_dict["topic"]["title"]
            logging.info("获取需求名称")
            sheets = getcase(title, get_dict, count)
            logging.info("完成")
        except Exception as ex:
            logging.info("出现错误，如下：")
            logging.error(ex)

