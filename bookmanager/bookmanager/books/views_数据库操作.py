from django.db.models import F
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def login(request):
    return HttpResponse


#####################################新增数据#####################################

from books.models import BookInfo

# 方法1
# 会把新生成的对象返回
book = BookInfo(
    name='python',
    pub_date='2000-01-20'
)
book.save()

# 方法2
# object 模型管理类

BookInfo.objects.create(
    name='java',
    pub_date='2010-01-20'
)
#####################################修改数据#####################################
from books.models import BookInfo

# 先查询数据
book = BookInfo.objects.get(id=1)
# 更新数据 - 直接修改实例
book.read_count = 20
book.save()

# 更新数据 - 直接更新
BookInfo.objects.filter(id=1).update(
    read_count=100,
    comment_count=200
)

#####################################删除数据#####################################

# 方法1
book = BookInfo.objects.get(id=5)
book.delete()

# 方法2
BookInfo.objects.filter(id=6).delete()


#####################################查询数据#####################################

# 基本查询
# get 获取单个数据
# all 获取所有数据
# count 个数

book = BookInfo.objects.get(id=1)

try:
    book = BookInfo.objects.get(id=100)

except BookInfo.DoesNotExist as e:
    pass
"""
books.models.BookInfo.DoesNotExist: BookInfo matching query does not exist.
"""

# 返回所有数据 【列表】
BookInfo.objects.all()

# 返回统计
BookInfo.objects.count()
BookInfo.objects.all().count()



##################################### filter get exclude #####################################

"""
相当于 where 查询
filter      ： 筛选/过滤 返回n个结果
get         ： 返回1个结果
exclude     ： 排除调符合条件剩下的结果 相当于not

语法形式：   filter(字段名__运算符 = 值)
"""

# 查询编号为1的图书
BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')


##################################### 多属性比较 - F对象 #####################################
from django.db.models import F

"""
F对象的语法形式

filter(字段名__运算符=F（'字段名'）)
"""

# 查询阅读量大于评论量2倍

BookInfo.objects.filter(read_count__gt=F('comment_count')*2)



##################################### 多条件查询(or) - Q对象 #####################################

"""
Q(字段名__运算符)

或 Q() | Q() ...
与 Q() & Q() ...
非 ～Q()


"""

# 查询id 大于2 并且阅读量大于20
# 方法1
BookInfo.objects.filter(id__gt=2).filter(read_count__gt=20)

# 方法2
BookInfo.objects.filter(id__gt=2, read_count__gt=20)

# 查询id 大于2 或者阅读量大于20
from django.db.models import Q

BookInfo.objects.filter(Q(id__gt=2) | Q(read_count__gt=20))


##################################### 聚合函数 #####################################

"""
Sum Max Min Avg Count

语法形式: objects.aggragte(xxx('字段'))
"""

# 当前数据的阅读总量
from django.db.models import Sum, Max, Min, Avg, Count
BookInfo.objects.aggregate(Sum('read_count'))


##################################### 排序 #####################################
# 默认升序
BookInfo.objects.all().order_by('read_count')
# 降序
BookInfo.objects.all().order_by('-read_count')



##################################### 关联查询 #####################################
"""
书籍和人物的关系 1：n
书籍 中没有任何关于人物的字段
人物 中有关于书籍的字段book 外键

语法形式： 
    通过书籍查询人物信息（已知主表数据，关联查询从表数据）
        主表模型（实例对象）.关联模型类的小写——set.all()
    通过人物查询书籍信息（已知 从表数据，关联查询主表数据）
        从表模型（实例对象）.外键
        
"""

from books.models import PeopleInfo

# 查询书籍为1 的所有人物信息 - 通过书籍查询人物
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

# 查询人物为1 的书籍信息 - 根据书籍查询人物
people = PeopleInfo.objects.get(id=1)
people.book.name

##################################### 关联查询 + 筛选#####################################

"""
根据从表查总表
    filter(关联模型类小写__ 字段__ 运算符=)
根据主表查总表
    filter(外键__字段__运算符=)
"""

# 查询图书，要求人物为郭靖
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')

# 查询图书，要求图书中的人物描述包含 "八"
BookInfo.objects.filter(peopleinfo__description__contains='八')


# 查询书名为'天龙八部'的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于30 的所有人物
PeopleInfo.objects.filter(book__read_count__gt=30)

##################################### 查询集#####################################

[book.id for book in BookInfo.objects.all()]

books = BookInfo.objects.all()

[book.id for book in books]


##################################### 分页 #####################################
from django.core.paginator import Paginator
books = BookInfo.objects.all()
p = Paginator(books, 2)
p.page(1)




