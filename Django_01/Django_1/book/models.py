from django.db import models

# Create your models here.


"""
1. 定义模型类
2. 模型迁移
    2.1 先生成迁移文件 - 不会在数据库中生成表，只会创建一个数据表和模型的对应关系
        python manage.py makemigrations
    2.2 迁移
        python manage.py migrate
3. 操作数据库

1. 在哪定义模型
2. 模型继承谁
3. ORM 对应关系
    表 -> 类
    字段 -> 属性
"""


# 1. 定义模型类
class BookInfo(models.Model):
    """
    1. 主键 当前会自动生成
    2. 属性 直接复制
    """
    name = models.CharField(max_length=10)

    # admin 站点
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
