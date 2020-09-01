from xmindparser import xmind_to_dict
import json


#获得一个列表+字典的数据
data = xmind_to_dict("D:\登录注册.xmind")
print(data)

#获取列表中的字典
get_dict = data[0]
print(get_dict)

#获取需求名称
get_sheet = get_dict["topic"]["title"]
print("需求名称：",get_sheet)

#获取所属模块
get_case = get_dict["topic"]
get_model = get_case["topics"][0]["title"]
num = len(get_case["topics"])
print("所属大模块：",get_model)
print("需求的大模块数量：",num)

#获取所属的一级模块
get_model1 = get_case["topics"][0]["topics"][0]["title"]
num2 = len(get_case["topics"][0]["topics"])
print("一级模块：",get_model1)
print("一级模块数量",num2)

#获取所属的二级模块
get_model2 = get_case["topics"][0]["topics"][0]["topics"][0]["title"]
num3 = len(get_case["topics"][0]["topics"][0]["topics"])
print(get_model2)
print("二级模块数量",num3)

#显示在该二级模块下有多少条测试用例
get_num = len(get_case["topics"][0]["topics"][0]["topics"][0]["topics"])
print(get_num)

#获取在该二级模块下的所有测试用例
get_cases = get_case["topics"][0]["topics"][0]["topics"][0]["topics"][0]["topics"]

#获取用例名称
#get_cases[X]["title"]   用例名称变量
get_cases_title = get_cases[0]["title"]
print(get_cases_title)

#获取用例优先级
#get_cases[X]["makers"][0]   优先级变量
priority = ""
get_priority = get_cases[1]["makers"][0]
if get_priority == "priority-1":
    priority = "S"
elif get_priority == "priority-2":
    priority = "A"
elif get_priority == "priority-3":
    priority = "B"
elif get_priority == "priority-4":
    priority = "C"
print(priority)

#获取用例的前置步骤
#get_cases[X]["topics"][0]["title"]  前置步骤
get_first = get_cases[0]["topics"][0]["title"]
print(get_first)

#获取用例步骤
#get_cases[X]["topics"][1]["title"]   步骤
get_step = get_cases[0]["topics"][1]["title"]
print(get_step)

#获取期望结果
#get_cases[X]["topics"][1]["topics"][0]["title"]  期望结果
get_hoperesult = get_cases[0]["topics"][1]["topics"][0]["title"]
print(get_hoperesult)

print(get_cases)

#case_title = data[0]["topic"]["title"]
#print(case_title)