from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ImageForm
from .models import Images

# Create your views here.
def homes(request):
    if request.method == 'POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    img=Images.objects.all()
    form=ImageForm()
    return render(request,'homes.html',{'img':img , 'form':form})

#def abc(request):
    return render(request,'test.html')