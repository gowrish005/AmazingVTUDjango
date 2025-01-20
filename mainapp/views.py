from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from requests import request
from .models import Semester, Branch, Subject, Module, TempModule, TempBranch, TempSubject, PageView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from natsort import natsorted #to fix the issue where 10 comes before 1 in the modules page

def increment_page_view(page_name):
    page_view, created = PageView.objects.get_or_create(page_name=page_name)
    page_view.view_count += 1
    page_view.save()

def defualt(request):
    return render(request, 'index.html')
    

def main_page(request):
    increment_page_view('main_page')
    semesters = Semester.objects.all()
    page_views = {
        'main_page': PageView.objects.get(page_name='main_page').view_count,
    }
    return render(request, 'main.html', {'semesters': semesters, 'page_views': page_views})

def branch_page(request, semester_id):
    increment_page_view('branch_page')
    semester = get_object_or_404(Semester, id=semester_id)
    branches = Branch.objects.filter(semester=semester)
    page_views = {
        'branch_page': PageView.objects.get(page_name='branch_page').view_count,
    }
    return render(request, 'branches.html', {'branches': branches, 'semester_name': semester.name, 'page_views': page_views})

def subject_page(request, branch_id):
    increment_page_view('subject_page')
    branch = get_object_or_404(Branch, id=branch_id)
    subjects = Subject.objects.filter(branch=branch)
    page_views = {
        'subject_page': PageView.objects.get(page_name='subject_page').view_count,
    }
    return render(request, 'subjects.html', {'subjects': subjects, 'branch': branch, 'page_views': page_views})

def modules_page(request, subject_id):
    increment_page_view('modules_page')
    modules = Module.objects.filter(subject_id=subject_id)
    modules = natsorted(modules, key=lambda x: x.name) #to fix the issue where 10 comes before 1 in the modules page
    subject = get_object_or_404(Subject, id=subject_id)
    subject_code = subject.subjectcode
    page_views = {
        'modules_page': PageView.objects.get(page_name='modules_page').view_count,
    }
    return render(request, 'modules.html', {'modules': modules, 'subject_name': subject.name, 'subject_code': subject_code, 'page_views': page_views})


def upload_module(request):
    if request.method == 'POST':
        semester_id = request.POST.get('semester')
        branch_id = request.POST.get('branch')
        subject_id = request.POST.get('subject')
        semester = get_object_or_404(Semester, id=semester_id)
        branch = get_object_or_404(Branch, id=branch_id)
        subject = get_object_or_404(Subject, id=subject_id)
        
        module_count = len([key for key in request.POST.keys() if key.startswith('module_name_')])
        
        subject_id = request.POST.get('subject')
        semester = get_object_or_404(Semester, id=semester_id)
        branch = get_object_or_404(Branch, id=branch_id)
        subject = get_object_or_404(Subject, id=subject_id)
        
        module_count = len([key for key in request.POST.keys() if key.startswith('module_name_')])
        
        for i in range(1, module_count + 1):
            name = request.POST.get(f'module_name_{i}')
            description = request.POST.get(f'module_description_{i}')
            image = request.FILES.get(f'module_image_{i}')
            file = request.FILES.get(f'module_file_{i}')
            
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
        
        messages.success(request, "Modules uploaded successfully and are pending approval.")
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
    branches = Branch.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'create_branch.html', {'semesters': semesters, 'branches': branches, 'subjects': subjects})

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
    branches = Branch.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'create_subject.html', {'semesters': semesters, 'branches': branches, 'subjects': subjects})

def get_branches(request, semester_id):
    branches = Branch.objects.filter(semester_id=semester_id)
    branches_data = [{'id': branch.id, 'name': branch.name} for branch in branches]
    return JsonResponse({'branches': branches_data})

def get_subjects(request, branch_id):
    subjects = Subject.objects.filter(branch_id=branch_id)
    subjects = Subject.objects.all()
    subjects_data = [{'id': subject.id, 'name': subject.name} for subject in subjects]
    return JsonResponse({'subjects': subjects_data})

@staff_member_required
def admin_control_panel(request):
    semesters = Semester.objects.all()
    branches = Branch.objects.all().order_by('name', 'semester__name')
    subjects = Subject.objects.all()
    modules = Module.objects.all()
    return render(request, 'admin_control_panel.html', {
        'semesters': semesters,
        'branches': branches,
        'subjects': subjects,
        'modules': modules
    })

    modules = Module.objects.all()
    return render(request, 'admin_control_panel.html', {
        'semesters': semesters,
        'branches': branches,
        'subjects': subjects,
        'modules': modules
    })
