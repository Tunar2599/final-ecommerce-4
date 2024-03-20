from django.shortcuts import render,redirect
from customer.forms import ContactForm, RegisterForm
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout
from .models import BlogPost
from .models import Post




def contact(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': form, 'result': 'success'})
            return render(request, 'contact.html', {'form': form, 'result': 'fail'})
    return render(request,'contact.html',{'form':form})



def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            customer=form.save()
            login(request, customer.user)
            return redirect('customer:login')
    return render(request,'register.html', {'form':form})





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('shop:home')  
        else:
            return render(request, 'login.html', {'fail': True})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('customer:login') 



def blog(request):
    recent_posts = Post.objects.all().order_by('-created_at')[:5]  
    all_posts = Post.objects.all()
    context = {'recent_posts': recent_posts, 'all_posts': all_posts}
    return render(request, 'blog.html', context)
