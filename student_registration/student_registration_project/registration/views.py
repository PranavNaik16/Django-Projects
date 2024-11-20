from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the student data to the database
            return redirect('success')  # Redirect to success page after submission
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def success(request):
    return render(request, 'registration/success.html')
