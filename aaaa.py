from xmindparser import xmind_to_dict


def get_case(self, title, dicts):
    case = dicts["topic"]
    priority = ""
    # 计算大模块数量
    get_num_module = len(case["topics"])

    # 计算一级模块数量
    get_module_first = len(case["topics"][0]["topics"])

    # 计算二级模块数量
    get_module_second = len(case["topics"][0]["topics"][0]["topics"])

    # 计算用例数
    get_case_num = len(case["topics"][0]["topics"][0]["topics"][0]["topics"])

    # 1.进入大模块的循环中
    for i in range(0, get_num_module):
        # 进来后计算一级模块数量
        num_module_first = len(case["topics"][i]["topics"])
        # 获取大模块名称
        get_module_big = case["topics"][i]["title"]
        print("所属模块：", get_module_big)
        # 2.进入一级模块
        for j in range(0, num_module_first):
            # 计算二级模块的数量
            num_module_second = len(case["topics"][i]["topics"][j]["topics"])
            # 获取一级模块的名称
            get_module_first = case["topics"][i]["topics"][j]["title"]
            print("一级模块：", get_module_first)
            # 3.进入二级模块
            for a in range(0, num_module_second):
                # 计算二级模块下的用例数
                num_case = len(case["topics"][i]["topics"][j]["topics"][a]["topics"])
                # 获取二级模块名称
                get_module_second = case["topics"][i]["topics"][j]["topics"][a]["title"]
                print("二级模块：", get_module_second)
                # 4.进入每一条用例中
                for b in range(0, num_case):
                    # 获取测试用例名字
                    case_name = case["topics"][i]["topics"][j]["topics"][a]["topics"][b]["title"]
                    print("用例名称：", case_name)
                    # 获取测试用例的优先级
                    get_priority = case[b]["makers"][0]
                    if get_priority == "priority-1":
                        priority = "S"
                    elif get_priority == "priority-2":
                        priority = "A"
                    elif get_priority == "priority-3":
                        priority = "B"
                    else:
                        priority = "C"
                    print("优先级：", priority)

                    # 获取前置步骤
                    step_first = case[b]["topics"][0]["title"]
                    print("前置步骤：", step_first)
                    # 获取操作步骤
                    step = case[b]["topics"][1]["title"]
                    print("操作步骤：", step)
                    # 获取期望结果
                    hole_result = case[b]["topics"][1]["topics"][0]["title"]
                    print("期望结果", hole_result)


if __name__ == "__main__":
    # 读取文件
    data = xmind_to_dict("D:\登录注册.xmind")
    # 获取列表中的字典
    get_dict = data[0]
    # 获取需求的名称
    title = get_dict["topic"]["title"]

    getcase(title, get_dict)
