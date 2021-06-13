## centos7 安装rabbitmq

[1](https://blog.csdn.net/yexiaomodemo/article/details/80473411)

[2](https://www.cnblogs.com/yang-hao/p/11737646.html)



## 需要安装的库

`pika`



## 官方的python代码无法跑通，需要加入用户名密码

```python

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))
```



## FAQs

1. rabbitmq中，guest是默认用户，拥有管理员权限，但是只允许使用`localhost`登陆。如果需要使用外界的浏览器登陆，需要再[创建一个管理员账户](https://www.cnblogs.com/gongshun/p/10694659.html)。