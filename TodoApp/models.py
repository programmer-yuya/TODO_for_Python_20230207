from django.db import models
from datetime import datetime
from django import forms
# Create your models here.

class Todo(models.Model):

    priorityList=(('1','低'),('2','中'),('3','高'))
    completeFlg=((False,'未'),(True,'済'))

    title=models.CharField("タスク名",max_length=50)
    detail=models.CharField("詳細",max_length=100,blank=True)
    registeDate=models.DateField("登録日",auto_now_add=True)
    priority=models.CharField("優先度",max_length=1,blank=False,choices=priorityList,help_text='1:低、2:中、3:高')
    validDate=models.DateField("有効期限",null=True)
    complete=models.BooleanField("完了",choices=completeFlg,blank=True, default=False,help_text='タスクが完了したら、True')