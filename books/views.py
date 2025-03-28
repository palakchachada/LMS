from django.shortcuts import render, redirect
from .models import User, Role , Book
from .forms import LoginForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def home(request):
    return render(request,'home.html')

def login_page(request):
    error_message = ""
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        email=request.POST["email"]
        print("userrr",email)
        entered_password = request.POST['password']
        print("entered pass",entered_password)
        try:
            use = User.objects.get(email=email)
            print("use", use.password, use.email)

            role = Role.objects.get(email=use.email)
            print("rolee",role.email)
            print("password check",check_password(entered_password, use.password))
            print("password check2",entered_password)
            print("password check3",use.password)
            # Verify the entered password with the hashed password
            if check_password(entered_password, use.password):
                print("Password match")
                request.session['email'] = use.email  # Store email in sessio
                print(request.session['email'],"emm")
                if use.email in role.email and role.role_name == 'Admin':
                    return redirect('add_books')
                else:
                    return redirect('book_details')
            else:
                print("Invalid password")
                error_message = "Invalid Email or Password"
                # Handle invalid password (e.g., show error message or redirect to login)
        except User.DoesNotExist:
            print("User not found")
            error_message = "User not found. Please register."
            # Handle case when email does not exist in the database

    return render(request,'login_page.html',{'form': form, 'error_message':error_message})


def register(request):
    if request.method == 'POST':
        user_id = generate_random_code()
        password = make_password(request.POST['password'])
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        puser = User(user_id=user_id, email = email, name = name, password = password , role="User")
        puser.save()
        role = Role(email=email,role_name='User')
        role.save()


        return redirect('/login/')
    context = {
        'generated_user_id': generate_random_code(),
    }
    return render(request,'register.html',context)

import secrets
import string   
def generate_random_code(prefix="USER",length=2):
    alphabet = string.digits
    return prefix + ''.join(secrets.choice(alphabet) for _ in range(length))


def profile(request):
    user_email = request.session.get('email')
    print("profile",user_email)
    e = User.objects.get(email = user_email)
    print("profile e", e)
    context = {
        'e':e,
    }
    return render(request,'profile.html',context)

def add_books(request):
    q = Book.objects.all().order_by('-id')
    print("blog",q)
    if request.method=='POST':
        title = request.POST.get('title')
        print(title,"title")
        author = request.POST.get('author')
        print('author',author)
        date  = request.POST.get('date')
        print('date',date)
        isbn = request.POST.get('isbn')
        print('isbn',isbn)
        available_copies = request.POST.get('available_copies')
        print('available_copies',available_copies)
        bk = Book(title=title, author = author , date = date, isbn = isbn, available_copies= available_copies) 
        bk.save()
        messages.success(request,"Uploaded Successfully")
        
        
    context = {
        'q':q,
    }
    return render(request,'add_books.html',context)


def edit_book(request,isbn):
    q = Book.objects.get(isbn=isbn)
    print("q",q)
    if request.method=='POST':
        q.title = request.POST.get('title')
        q.author = request.POST.get('author')
        # q.date  = request.POST.get('date')
        q.isbn = request.POST.get('isbn')
        q.available_copies = request.POST.get('available_copies')
        q.save()
        messages.success(request,"Updated Successfully")
        return redirect('/add_books/')
    context = {
        'q':q,
    }
    return render(request,'edit_book.html',context)


def delete_book(request,isbn):
    cus = Book.objects.get(isbn = isbn)
    cus.delete()
    return redirect('/add_books/')

def book_details(request):
    q = Book.objects.all().order_by('-id')
    context = {
        'q':q,
    }
    return render(request,'book_details.html',context)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/login/')    
