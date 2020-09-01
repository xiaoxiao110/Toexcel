import json
data = {
     'Chinese': 90,
     'Mathematics': 85,
     'English': 94
}

string = json.dumps(data)

print(string)

print("类型：{}".format(type(string)))