from django.db import models

# Create your models here.
"""
我们的模型类需要继承models.Model
系统会自动为我们添加一个主键--id属性
定义字段
    字段名=model.类型(选项)
    字段名就是数据库表中的字段名
    字段名不要使用mysqk、python的关键字
    char(长度)
    varchar(长度)
    在model中被替换成是选项
"""
class Book(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Person(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BooleanField(default=False)
    #外键约束：人物属于哪本书
    book = models.ForeignKey(Book, on_delete=models.CASCADE)