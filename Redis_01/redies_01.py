import  redis

if __name__ == '__main__':
    # 创建 redis 对象
    # 连接外部资源时，一定要使用try
    try:
        re = redis.Redis()
    except Exception as e:
        print(e)

    # 添加
    result = re.set('name', 'Xiaole Jin')
    print(result)
    # 查询
    name = re.get('name')
    print(name)