# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd

def extractMath(obj):
    return obj["math"]

scores = [
	{"name":"john", "kor":90, "math":90, "eng":95 },
	{"name":"peter", "kor":90, "math":90, "eng":95 },
	{"name":"sue", "kor":90, "math":90, "eng":95 },
	{"name":"susan", "kor":90, "math":90, "eng":95 },
]

a = "Hello World"

if __name__ == "__main__":
    dataframe = pd.DataFrame(scores)
    print(dataframe.loc[0])
    print(dataframe["kor"])
    print(dataframe)
    result = map(extractMath, scores)
    print(list(result))
    for item in scores:
        for key, value in item.items():
            print(key, value)
    keys = scores[0].keys()
    values = scores[0].values()
    items = scores[0].items()
    print(keys,values,items)
    print(scores[0].keys())
    print(scores[0]["kor"])
    for score in scores:
        print(score)
    print(a)
