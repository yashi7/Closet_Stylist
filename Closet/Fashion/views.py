from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .models import user_new,user_files
from static.Model.Model_interface import predict

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            return redirect('profile')
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('UserName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        con_pass=request.POST.get('confirm_password')

        if password!=con_pass:
            return redirect('signup')
        
        my_user=User.objects.create_user(username,email,password)
        my_user.save() 

        user=user_new(Username=username,
                      Email=email)
        user.save()
        return redirect('login')  
    return render(request, 'signup.html')

def aboutus(request):
    return render(request,'aboutus.html')

def upload(request):
    
    if request.method == 'POST':
        image = request.FILES.get('item-image')
        # category = request.POST.get('item-category')
        #gender,category,color,occassion
        
        print(request.POST)
        print("the image is",image)
        # print("the category is",category)
        if image: 
            gender,category,color,occassion=predict(image)
            my_image = user_files(image=image,gender=gender,category=category,color=color,occassion=occassion)
            my_image.save()
            print(gender,category,color,occassion)
            return redirect('upload')
        else:
            return render(request, 'upload.html', {'error': 'All fields are required'})
    return render(request,'upload.html')

# def demo(request):
#     return render(request, 'demo_recommendation.html')

def profile(request):
    return render(request,'profile.html')

def recommendation(request):
    print("hi ............../////////////.............//////////////............/////////////")
    if request.method == 'POST':
        occassion_rec = request.POST.get('occassion')
    
    # Check if the occasion exists in the database
        matching_items = user_files.objects.filter(occassion=occassion_rec)  # Filter the records in one query
    
        if matching_items.exists():  # Check if there are any matching items
        # Print the image field of the matching items
            for item in matching_items:
                print(item.image.url)  # Assuming image is stored as an ImageField
        else:
            print("No matching items found.")
        return render(request,'recommendation.html',{'recommendations':matching_items})
    return render(request,'recommendation.html')
