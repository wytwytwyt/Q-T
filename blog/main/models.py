from django.db import models

# Create your models here.
class Post(models):
    '''
    文章数据：
        
    '''
    # 标题
    title = models.CharField(max_length=50)
    
    # 内容
    body = models.TextField()

    # 创建时间
    created_time = models.DateTimeField(auto_now=True)
    
    # 作者
    auhor = models.ForeignKey('User')
    
    # 分类
    category = models.ManyToManyField('Category')

    # 标签
    tag = models.ManyToManyField('Tag', blank=True)

    # 摘要
    abstract = models.CharField(max_length=200)
    