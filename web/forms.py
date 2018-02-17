# -*- coding: UTF-8 -*-
from django import forms
from web.models import Content

class ContentForm(forms.ModelForm):
        class Meta:
                model = Content
                fields = ['description', 'reporter', 'phone', 'picture', 'picname']
          
        def __init__(self, *args, **kwargs):
                super(ContentForm, self).__init__(*args, **kwargs)
                self.fields['description'].label = "問題描述"
                self.fields['reporter'].label = "報修人"
                self.fields['phone'].label = "連絡電話"          
                self.fields['picture'].label = "照片"   
                self.fields['picname'].widget = forms.HiddenInput()
                
# 使用者登入表單
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "帳號"
        self.fields['password'].label = "密碼"
        
class ContentEditForm(forms.ModelForm): 
        class Meta:
                model = Content
                fields = ['status', 'comment']        
          
        def __init__(self, *args, **kwargs):
                super(ContentEditForm, self).__init__(*args, **kwargs)
                self.fields['status'].label = "狀態"
                self.fields['comment'].label = "處理情況"
    