from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Contact,post,Catagory
from django.http import HttpResponse

def index(request):
    dataa = post.acceptpost.all().order_by('-post_id')
    datar = post.acceptpost.filter().order_by('-post_id')[0:3]
    cat = Catagory.objects.all()

    paginator = Paginator(dataa, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    d = {'data': page_obj, 'data1': datar , 'catag':cat}
    return render(request, 'blog/home.html', d)




def post_detail(request ,id):
    dataa = post.objects.get(post_id =id)
    datar = post.objects.filter().order_by('-post_id')[0:3]
    cat = Catagory.objects.all()
    d={'i':dataa,'data1':datar ,'catag':cat}
    return render(request , 'blog/blog-details.html',d)


def post_Search(request):
    d=""
    if request.method=="POST":
        datas = request.POST['query']
        data1 = post.objects.filter(title__icontains=datas)
        data2 = post.objects.filter(author__username__contains=datas)
        data3=  post.objects.filter(content__icontains=datas)
        data = data1.union(data2,data3)
        if data.count==0:
            messages.warning(request,"no result can be found please refine your query")



    d={'data':data}
    return render(request, 'blog/search.html', d)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print("=========================")
        print(name)
        print("=========================")
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, 'contractus.html')


