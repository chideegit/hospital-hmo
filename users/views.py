from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import RegisterUserForm
from userprofile.form import AddUserProfileForm 

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Login successful. Welcome {user.get_username}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Sorry, something went wrong')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Your session has ended. Please log in to continue')
    return redirect('login')


# Register users from the frontend 
def register_user(request):
    if request.method == 'POST':
        form1 = RegisterUserForm(request.POST)
        form2 = AddUserProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            var1 = form1.save(commit=False)
            var2 = form2.save(commit=False)
            var2.user = var1 # assign the current created user to the user profile 
            var1.save() # save 
            var2.save() # save 
            messages.success(request, 'User is now added to DB')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Sorry, something went wrong.')
            return redirect('register-user')
    else:
        context = {'form1':form1, 'form2':form2}
        return render(request, 'users/register_user.html', context)
