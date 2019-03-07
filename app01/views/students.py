from django.shortcuts import render, HttpResponse
from app01 import models
# Create your views here.
def students(request):
    if request.method == 'GET':
        num = request.GET.get('nid')
        models.Student.objects.filter(id=num).delete()
    stu = models.Student.objects.all()
    # for n in stu:
    #     print(n.cs.all())
    # cos = stu.cs.all()
    # print(cos)
    return render(request, 'students.html', {'stu': stu})

def cources(request):
    cources = models.Course.objects.all()
    return render(request, 'cource.html', {'cources': cources})

def add_stu(request):
    if request.method == 'POST':
        name = request.POST.get('stu_name')
        age = request.POST.get('stu_age')
        sex = request.POST.get('stu_sex')
        card= request.POST.get('stu_id_card')
        tel = request.POST.get('stu_tel')
        addr = request.POST.get('stu_addr')
        n_cource = request.POST.get('stu_cource')
        print(n_cource)
        stu = models.Student.objects.create(name=name, age=age, sex=sex, id_card=card, tel=tel, addr=addr)
        stu.cs.add(n_cource)
    courc = models.Course.objects.all()
    return render(request, 'add_stu.html', {'courc': courc})

def add_cources(request):
    if request.method == 'POST':
        name = request.POST.get('co_name')
        describe = request.POST.get('co_describe')
        times = request.POST.get('co_times')
        models.Course.objects.create(name=name, describe=describe, times=times)
    return render(request, 'add_cource.html')
