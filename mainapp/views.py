from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from requests import request
from .models import Semester, Branch, Subject, Module, TempModule, TempBranch, TempSubject
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def main_page(request):
    semesters = Semester.objects.all()
    return render(request, 'main.html', {'semesters': semesters})

def branch_page(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    branches = Branch.objects.filter(semester=semester)
    return render(request, 'branches.html', {'branches': branches, 'semester_name': semester.name})

def subject_page(request, branch_id):
    subjects = Subject.objects.filter(branch_id=branch_id)
    branch = get_object_or_404(Branch, id=branch_id)
    return render(request, 'subjects.html', {'subjects': subjects, 'branch': branch})

def modules_page(request, subject_id):
    modules = Module.objects.filter(subject_id=subject_id)
    subject = get_object_or_404(Subject, id=subject_id)
    subject_code = subject.subjectcode
    return render(request, 'modules.html', {'modules': modules, 'subject_name': subject.name, 'subject_code': subject_code})

def defualt(request):
    return render(request, 'index.html')
    
def upload_module(request):
       if request.method == 'POST':
           name = request.POST.get('name')
           description = request.POST.get('description')
           image = request.FILES.get('image')
           file = request.FILES.get('file')
           subject_id = request.POST.get('subject')
           semester_id = request.POST.get('semester')
           branch_id = request.POST.get('branch')
           subject = get_object_or_404(Subject, id=subject_id)
           semester = get_object_or_404(Semester, id=semester_id)
           branch = get_object_or_404(Branch, id=branch_id)
           temp_module = TempModule(
               name=name,
               description=description,
               image=image,
               file=file,
               subject=subject,
               semester=semester,
               branch=branch
           )
           temp_module.save()
           messages.success(request, "Module uploaded successfully and is pending approval.")
           return redirect('main')
       
       semesters = Semester.objects.all()
       branches = Branch.objects.none()
       subjects = Subject.objects.all()

       return render(request, 'upload_module.html', {'semesters': semesters, 'branches': branches, 'subjects': subjects})


def create_branch(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        semester_ids = request.POST.getlist('semesters')
        for semester_id in semester_ids:
            semester = get_object_or_404(Semester, id=semester_id)
            temp_branch = TempBranch(name=name, semester=semester)
            temp_branch.save()
        messages.success(request, "Branch created successfully for selected semesters and is pending approval.")
        return redirect('main')
    
    semesters = Semester.objects.all()
    return render(request, 'create_branch.html', {'semesters': semesters})

def create_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject_code = request.POST.get('subject_code')
        semester_id = request.POST.get('semester')
        branch_id = request.POST.get('branch')
        semester = get_object_or_404(Semester, id=semester_id)
        branch = get_object_or_404(Branch, id=branch_id)
        temp_subject = TempSubject(name=name, subjectcode=subject_code, semester=semester, branch=branch)
        temp_subject.save()
        messages.success(request, "Subject created successfully and is pending approval.")
        return redirect('main')
    
    semesters = Semester.objects.all()
    branches = Branch.objects.none()
    return render(request, 'create_subject.html', {'semesters': semesters, 'branches': branches})

def get_branches(request, semester_id):
    branches = Branch.objects.filter(semester_id=semester_id)
    branches_data = [{'id': branch.id, 'name': branch.name} for branch in branches]
    return JsonResponse({'branches': branches_data})

def get_subjects(request, branch_id):
    subjects = Subject.objects.filter(branch_id=branch_id)
    subjects_data = [{'id': subject.id, 'name': subject.name} for subject in subjects]
    return JsonResponse({'subjects': subjects_data})
