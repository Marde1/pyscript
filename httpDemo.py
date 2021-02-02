import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")

if __name__ == "__main__":
    # print(type(response))
    # # print("read():",response.read())
    # print(response.read().decode("utf-8"))
    # # print("readinto():", response.readinto())
    # print("getheader():", response.getheader("Content-Type"))
    # print("getheaders():", response.getheaders())
    # # print("fileno():", response.fileno())
    # print("status:",response.status)
    # print("msg:",response.msg)
    # print("version:",response.version)
    # print("reason:",response.reason)
    # print("debuglevel:",response.debuglevel)
    # print("closed:", response.closed)
    # print(response.readlines())

    for i in response.readlines():
        print(i)

