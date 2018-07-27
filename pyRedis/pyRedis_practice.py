# FileName : pyRedis_practice.py
# Author   : Adil
# DateTime : 2018/7/26 16:33
# SoftWare : PyCharm

# redis  练习

# 导入 redis
import redis

# 创建连接

#  严格连接方式
r = redis.StrictRedis(host='127.0.0.1',port=6379)
# python 化连接
pr = redis.Redis(host='127.0.0.1',port=6379)

# StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令
# Redis与StrictRedis的区别是：Redis是StrictRedis的子类，用于向前兼容旧版本的redis-py，并且这个连接方式是更加"python化"的


# 连接池

# 为了节省资源，减少多次连接损耗，连接池的作用相当于总揽多个客户端与服务端的连接，
# 当新客户端需要连接时，只需要到连接池获取一个连接即可，实际上只是一个连接共享给多个客户端。

pool = redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)

# 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。


r1 = redis.Redis(connection_pool=pool)

r2 = redis.Redis(connection_pool=pool)

r.set('a','1')
print(r.get('a'))

print(r.client_list())

print(pr.client_list())

print(r1.client_list())

print(r2.client_list())

# r1  r2 的 的连接id 是一样的，说明他们是一个客户端连接

