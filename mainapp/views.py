from django.shortcuts import render

# Create your views here.
# views.py

from .models import Year, Branch, Subject, Module

def main_page(request):
    years = Year.objects.all()
    return render(request, 'main.html', {'years': years})

def branch_page(request, year_id):
    branches = Branch.objects.filter(year_id=year_id)
    year = Year.objects.get(id=year_id)  # Fetch the year name
    print(branches.query)  # Debug query
    print(branches)  # Debug result
    return render(request, 'branches.html', {'branches': branches,'year_name': year.name})

def subject_page(request, branch_id):
    subjects = Subject.objects.filter(branch_id=branch_id)
    return render(request, 'subjects.html', {'subjects': subjects})

def modules_page(request, subject_id):
    modules = Module.objects.filter(subject_id=subject_id)
    return render(request, 'modules.html', {'modules': modules})

def defualt(request):
    return render(request, 'index.html')
