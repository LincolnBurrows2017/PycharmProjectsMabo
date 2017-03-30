from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RemarkForm
from django.shortcuts import render
# Create your views here.
def remark(request):
    if request.method=='POST':
        form=RemarkForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request,'提交成功')
    else:
        form=RemarkForm()
    return render(request,'info/index.html',{'form':form})