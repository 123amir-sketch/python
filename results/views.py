from django.shortcuts import render, redirect
from .models import Result
from .forms import resultform
# Create your views here.

def form_view(request):
    error_message = None
    if request.method == 'POST':
        form = resultform(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['roll_no']
            student_class = form.cleaned_data['student_class']
            try:
                # Try to get the result for the given roll number
                fm = Result.objects.get(roll_no=roll_no, student_class=student_class)
                return render(request, "result.html", {'fm': fm})
            except Result.DoesNotExist:
                # If no matching roll number is found, set the error message
                error_message = "No result found for the entered roll number."
    else:
        form = resultform()
    return render(request, "home.html", {'form':form, 'error_message':error_message})

def result_view(request):
    return render(request, "result.html")
