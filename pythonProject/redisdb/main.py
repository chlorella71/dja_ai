# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import redis
import time

HOST="43.201.147.73"
PORT=6379
PASSWORD=111


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def redis_connections():
    try:
        red = redis.Redis(
            host=HOST,
            port=PORT,
            password=PASSWORD,
            db=0,
            decode_responses=True
        )
        red.ping()
        print("AWS REDIS에 성공적으로 연결되었음")
        return red
    except Exception as error:
        print(error)

def redis_set(red, key, value):
    result=red.set(key, value)
    return result

def redis_rpush(red,list_name, arrs):
    if red.rpush(list_name, *arrs): #*은 javascript의 ...과 같음
        print("list insert successful")

def redis_hash_set(red, object_name, dictionary):
    if red.hset(object_name, mapping=dictionary):
        print("object insert successful")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    red = redis_connections()

    # post_id=101
    # key=f"post:{post_id}:views"
    # key=f"{post_id}"
    # views=red.incr(key)
    # print(views)
    # print(key)

    # red.delete("post:{post_id}:views")
    # value = (red.get("post:{post_id}:views"))
    # print(value)

    # key="myKey"
    # value="Hello"
    # result = red.set(key, value)
    # print(result)
    # print(red.get(key))

    # objects = {"이름": "John", "국어": 90, "수학": 99, "영어": 100}
    # for key, value in objects.items():
    #     if redis_set(red, key, value):
    #         print("insert successfully")
    # print(red.get("국어"))

    # keys = red.keys("*")
    # print(keys)
    # for key in keys:
    #     print(red.get(key))

    # fruits = [ "apple" , "grape", "strawberry", "banana"]
    # redis_rpush(red, 'myList', fruits)

    # result = red.lpop('myList')
    # print(result)

    # print(red.lrange('myList', 0, -1))

    # data = {"이름": "John", "국어": 90, "수학":99}
    # redis_hash_set(red, "user:1", data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
