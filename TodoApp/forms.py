from django import forms
from django.forms import ModelForm
from datetime import datetime as dt
import datetime

from .models import Todo

class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            'validDate': forms.DateInput(attrs={"type": "date"}),
            'complete': forms.CheckboxInput(attrs={'class': 'check'}),
            # 'complete': forms.MultipleChoiceField(
            #     required=False,
            #     widget=forms.CheckboxSelectMultiple,
            #     ),
            }

class MessageForm(forms.Form):
    msgText = forms.CharField(max_length=100, label = 'メッセージ')
    msgTo = forms.CharField(max_length=10, label = '宛先')
    date=forms.DateField(widget=forms.DateInput(attrs={"type":"date","min":dt.strftime(dt.now(),'%Y-%m-%d')}), required=False, label = '登録日', initial=dt.now() + datetime.timedelta(days=7))
    # date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}), required=False, label = '登録日', initial=dt.now() + datetime.timedelta(days=7))
    # date=forms.DateField(widget=forms.DateInput(attrs={"type":"date","min":datetime.now().strftime('%Y-%m-%d')}), required=False, label = '登録日')
    # date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}), required=False, label = '登録日',initial=datetime.now())
