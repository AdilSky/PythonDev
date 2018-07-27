# FileName : pyParamiko_practice.py
# Author   : Adil
# DateTime : 2018/7/27 16:10
# SoftWare : PyCharm


import paramiko

# 使用密钥链接
# 前提是我曾经执行相关操作生成过密钥，路径如下
# 获取密钥  注意密钥匙路径
private_key = paramiko.RSAKey.from_private_key_file('/Users/yyj/hello_ssh/id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 链接服务器
ssh.connect(hostname='47.96.131.92',port=22,username='yangyaojun03946',pkey=private_key)

# 执行命令，我还不明白这个命令的意思
stdin,stdout,stderr = ssh.exec_command('df')
result = stdout.read()
# 打印一下结果
print(result)

# 关闭链接
ssh.close()




