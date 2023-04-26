from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField("タスク名",max_length=50)
    detail=models.CharField("詳細",max_length=100)
    registeDate=models.DateField("登録日")
    priority=models.CharField("優先度",max_length=10)
    validDate=models.DateField("有効期限")
    complete=models.BooleanField("完了")