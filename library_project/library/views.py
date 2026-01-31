from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required 
from library.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

# login page
def loginpage(request):
    return render(request,'login.html')


def loginUser(request):
    if request.method == 'POST':
        # 1. Get data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 2. Check if the credentials are valid
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 3. Check if they are an admin
            if user.is_superuser:
                login(request, user)  # Using the default login function
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': "You are not an admin."})
        else:
            # 4. If authenticate returns None
            return render(request, 'login.html', {'error': "Invalid username or password."})

    # If the request is GET, just show the page
    return render(request, 'login.html')



# Add this to your urls.py to test properly!
@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def addBook(request):
    if request.method=='POST':
        name=request.POST.get('name')
        edition=request.POST.get('edition')
        writer=request.POST.get('writer')

        result=AddBook(book_name=name,book_edition=edition,book_writer=writer)
        try:
            result.save()
            return render(request,'addbook.html',context={'success':'book added'})
        
        except result.DoesNotExist:
            return render(request,'addbook.html',context={'error':'no table exists'})
        
    else:
        return render(request,'addbook.html')



# add teacher
@login_required(login_url='/login/')
def addteacher(request):
    if request.method=='POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')

        result=AddTeacher(name=name,gender=gender)
        try:
            result.save()
            return render(request,'addteacher.html',context={'success':'teacher added'})
        
        except result.DoesNotExist:
            return render(request,'addteacher.html',context={'error':'no table exists'})
        
    else:
        return render(request,'addteacher.html')


# add student
@login_required(login_url='/login/')
def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        faculty=request.POST.get('faculty')


        result=AddStudent(name=name,gender=gender,faculty=faculty)
        try:
            result.save()
            return render(request,'addstudent.html',context={'success':'student added'})
        
        except result.DoesNotExist:
            return render(request,'addstudent.html',context={'error':'no table exists'})
        
    else:
        return render(request,'addstudent.html')


# book list
@login_required(login_url='/login/')
def booklist(request):
    book_list=AddBook.objects.all()
    
    context={
       'books':book_list
    }
    return render(request,'booklist.html',context)


# withdraw book
@login_required(login_url='/login/')
def withdrawbook(request):
    if request.method=='POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        faculty=request.POST.get('faculty')
        book=request.POST.get('book')
        t_or_a=request.POST.get('t/a')
        date=request.POST.get('date')

        result=WithdrawBook(student_name=name,gender=gender,faculty=faculty,date=date,book_name=book,teacher_or_student=t_or_a)
        try:
            result.save()
            return render(request,'withdrawbook.html',context={'success':'book withdrawn'})
        
        except result.DoesNotExist:
            return render(request,'withdrawbook.html',context={'error':'no table exists'})
        
    else:
        return render(request,'withdrawbook.html')



# withdraw list
@login_required(login_url='/login/')
def withdrawlist(request):
    book_withdraw=WithdrawBook.objects.all()
    context={
        'books':book_withdraw
    }
    return render(request,'withdrawlist.html',context)


@login_required(login_url='/login/')
def deletewithdrawlist(request,id):
    book_withdraw=WithdrawBook.objects.get(id=id)
    book_withdraw.delete()
    return redirect('withdrawlist')


@login_required(login_url='/login/')
def returned(request,id):
    returned=WithdrawBook.objects.get(id=id)
    returned.is_returned=True
    returned.save()
    return redirect('withdrawlist')


@login_required(login_url='/login/')
def passwordchange(request):
    if request.method=='POST':
        old=request.POST.get('old')
        password1=request.POST.get('new-password')
        password2=request.POST.get('confirm-password')
        user=request.user
        if user.is_authenticated:
            user2=authenticate(username=request.user.username,password=old)
            if user2:
                if password1==password2:
                    user2.set_password(password1)
                    user2.save()
                    return render(request,'changepassword.html',context={'change':"successfully changed"})
                else:
                    return render(request,'changepassword.html',context={'error':"password must be same"})
            else:
                return render(request,'changepassword.html',context={'error':"wrong credential"})
        else:
            return redirect('passwordchange')
    return render(request,'changepassword.html')


def passwordforgot(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('new-password')
        password2=request.POST.get('confirm-password')
        user2=User.objects.get(username=username)
        if user2:
            if password1==password2:
                user2.set_password(password1)
                user2.save()
                return render(request,'forgotpassword.html',context={'change':"success"})
            else:
                return render(request,'forgotpassword.html',context={'error':"password must be same"})
        else:
            return render(request,'forgotpassword.html',context={'error':"wrong credential"})
    else:
        return render(request,'forgotpassword.html')


# dashboard
@login_required(login_url='/login/')
def dashboard(request):
    stats = [
        {'name':'Total Books','count': AddBook.objects.count()},
        {'name':'BCA Student','count': AddStudent.objects.filter(faculty__icontains='bca').count()},
        {'name':'BHM Student','count': AddStudent.objects.filter(faculty__icontains='bhm').count()},
        {'name':'BSc.CSIT Student','count': AddStudent.objects.filter(faculty__icontains='bsc.csit').count()},
        {'name':'BIM Student','count': AddStudent.objects.filter(faculty__icontains='bim').count()},
        {'name':'Total Student','count': AddStudent.objects.all().count()},

    ]

    return render(request, 'dashboard.html', {'stats': stats})
