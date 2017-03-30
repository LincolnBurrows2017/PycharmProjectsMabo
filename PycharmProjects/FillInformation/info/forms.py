from django import forms
# Create your models here.
TOPIC_CHOICES=[('level1','差评'),('level2','中评'),('level3','好评')]
class RemarkForm(forms.Form):
    subject = forms.CharField(max_length=100, label='留言标题')
    mail = forms.EmailField(label='电子邮件')
    topic = forms.ChoiceField(choices=TOPIC_CHOICES, label='选择评分')
    message = forms.CharField(label='留言内容', widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False, label='订阅该贴')