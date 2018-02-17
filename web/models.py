# -*- coding: utf8 -*-
from django.db import models

class Content(models.Model):
    Status_CHOICES = [
        (0, '待處理'),
        (1, '處理中'),
        (2, '已處理'),
    ]
    
    # 報修事項
    description = models.TextField()
    # 報修人
    reporter = models.CharField(max_length=20)    
    # 連絡電話
    phone = models.CharField(max_length=20)
    # 報修日期
    publication_date = models.DateTimeField(auto_now_add=True)    
    # 處理人
    handler = models.CharField(max_length=20)
    # 處理狀況
    status = models.IntegerField(default=0, choices=Status_CHOICES)
    # 處理說明
    comment = models.TextField()
    # 處理日期
    handle_date = models.DateTimeField(null=True, blank=True)     
    # 照片
    picture = models.ImageField(blank=True,null=True)
    picname = models.CharField(max_length=32,null=True,blank=True)     
    
    def status_choice(self):
        return dict(Content.Status_CHOICES)[self.status]    

