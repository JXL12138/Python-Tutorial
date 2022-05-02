from django.db import models

# Create your models here.


"""
1. ORM

2. 继承 models.Model

3. 模型类会自动添加主键

"""

"""
书籍表： id, name, pub_date, read_count, comment_count, is_delete

    null 是否为空
    unique 是否唯一
    default 默认值
    verbose_name 后台显示名字

"""


class BookInfo(models.Model):
    # 书名
    name = models.CharField(max_length=10, unique=True, verbose_name='书名')
    # 发布日期
    pub_date = models.DateField(null=True)
    # 阅读量
    read_count = models.IntegerField(default=0)
    # 评论量
    comment_count = models.IntegerField(default=0)
    # 是否逻辑删除
    is_delete = models.BooleanField(default=False)

    class Meta:
        # 修改表名
        db_table = 'bookinfo'
        # 修改后台 admin 显示信息配置
        verbose_name = '书籍名'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'unknown')
    )
    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=2, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='对应书名')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
