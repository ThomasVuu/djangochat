from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignupForm

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()
            # Log the user in
            login(request, user)
            # Redirect to homepage
            return redirect('frontpage')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})