from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

def page_1(request):
    processors = Processors.objects.all()
    return render(request, 'app/Page_1.html', {'processors': processors})

def page_2(request):
    videocards = VideoCards.objects.all()
    return render(request, 'app/Page_2.html', {'videocards': videocards})

def page_3(request):
    ram = RAM.objects.all()
    return render(request, 'app/Page_3.html', {'ram': ram})


def page_form(request):
    if request.method == "POST":
        caption = request.POST.get('caption', 'Undefined')
        price = request.POST.get('price', 'Undefined')
        path_img = request.POST.get('path_img', 'Undefined')
        input_select = request.POST.get('select', 'Undefined')

        if input_select == '1':
            Processors.objects.create(caption=caption, price=price, path_img=path_img)

        elif input_select == '2':
            VideoCards.objects.create(caption=caption, price=price, path_img=path_img)

        elif input_select == '3':
            RAM.objects.create(caption=caption, price=price, path_img=path_img)

        return HttpResponseRedirect('/')

    else:
        form_add = FormAdd()
        return render(request, 'app/Page_form.html', {'form_add': form_add})