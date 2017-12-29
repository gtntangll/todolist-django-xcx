from django.db import models
import django.utils.timezone as timezone

# Create your models here.
 
class UserExt(models.Model):
	
	openid = models.CharField(max_length = 128)
	nickname = models.CharField(u'昵称', max_length = 128)
	headimgurl = models.CharField(u'头像地址', max_length =128)	

class Task(models.Model):

	user = models.ForeignKey(UserExt)#用户
	style = models.CharField(max_length = 128, default = '无')#无 紧急重要 紧急次要 不急重要 不急次要
	title = models.CharField(max_length = 128)#任务标题
	deadline = models.DateTimeField(default = timezone.now)#截止时间
	content = models.CharField(max_length = 128, default = u'无')#任务内容
	status = models.CharField(max_length = 32, default = u'进行中')#任务状态
