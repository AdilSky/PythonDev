# FileName : pyConnPgUseParamiko.py
# Author   : Adil
# DateTime : 2018/7/27 16:14
# SoftWare : PyCharm

# 通过 paramiko 建立ssh 进行连接

import paramiko
import psycopg2


from sshtunnel import SSHTunnelForwarder
# 获取密钥 注意密钥匙路径
private_key = paramiko.RSAKey.from_private_key_file('/Users/yyj/hello_ssh/id_rsa')
with SSHTunnelForwarder(
    # 指定ssh登录的跳转机的address
    ssh_address_or_host = ('47.96.131.92',22),
    # 设置密钥
    ssh_pkey = private_key,
    # 如果是通过密码访问，可以把下面注释打开，将密钥注释即可。
    # ssh_password = "password"
    # 设置用户
    ssh_username = 'yangyaojun03946',
    # 设置数据库服务地址及端口
    remote_bind_address= ('10.111.50.127',3503)) as server:

    conn = psycopg2.connect(database='bike_report',
                            user='bike_report',
                            password='bike_report',
                            host='127.0.0.1',  # 因为上面没有设置 local_bind_address,所以这里必须是127.0.0.1,如果设置了，取设置的值就行了。
                            port=server.local_bind_port) # 这里端口也一样，上面的server可以设置，没设置取这个就行了


    print(conn)

    cur = conn.cursor()
    # 执行查询，查看结果，验证数据库是否链接成功。
    cur.execute("select * from t_bike_data limit 1")

    rows = cur.fetchone()

    print(rows)

    conn.close()



