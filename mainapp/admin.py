from django.contrib import admin
from .models import Semester, Branch, Subject, Module, TempModule, TempBranch, TempSubject

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester__name')
    search_fields = ('name', 'semester__name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'subjectcode', 'semester__name', 'branch__name')
    search_fields = ('name', 'subjectcode')
    list_filter = ('semester__name', 'branch__name')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject__name', 'semester__name', 'branch__name', 'uploaded_at')
    search_fields = ('name', 'subject__name')
    list_filter = ('subject__name', 'semester__name', 'branch__name')

@admin.register(TempModule)
class TempModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'semester', 'branch', 'uploaded_at', 'approved')
    actions = ['approve_modules', 'reject_modules']

    def approve_modules(self, request, queryset):
        for temp_module in queryset:
            if not temp_module.approved:
                module = Module(
                    name=temp_module.name,
                    description=temp_module.description,
                    image=temp_module.image,
                    file=temp_module.file,
                    subject=temp_module.subject,
                    semester=temp_module.semester,
                    branch=temp_module.branch
                )
                module.save()
                temp_module.approved = True
                temp_module.save()
        self.message_user(request, "Selected modules have been approved and moved to the main database.")

    def reject_modules(self, request, queryset):
        for temp_module in queryset:
            temp_module.delete()
        self.message_user(request, "Selected modules have been rejected and deleted.")

@admin.register(TempBranch)
class TempBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester__name', 'approved')
    actions = ['approve_branches', 'reject_branches']

    def approve_branches(self, request, queryset):
        for temp_branch in queryset:
            if not temp_branch.approved:
                branch = Branch(name=temp_branch.name, semester=temp_branch.semester)
                branch.save()
                temp_branch.approved = True
                temp_branch.save()
        self.message_user(request, "Selected branches have been approved and moved to the main database.")

    def reject_branches(self, request, queryset):
        for temp_branch in queryset:
            temp_branch.delete()
        self.message_user(request, "Selected branches have been rejected and deleted.")

@admin.register(TempSubject)
class TempSubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'subjectcode', 'semester', 'branch', 'approved')
    actions = ['approve_subjects', 'reject_subjects']

    def approve_subjects(self, request, queryset):
        for temp_subject in queryset:
            if not temp_subject.approved:
                subject = Subject(
                    name=temp_subject.name,
                    subjectcode=temp_subject.subjectcode,
                    semester=temp_subject.semester,
                    branch=temp_subject.branch
                )
                subject.save()
                temp_subject.approved = True
                temp_subject.save()
        self.message_user(request, "Selected subjects have been approved and moved to the main database.")

    def reject_subjects(self, request, queryset):
        for temp_subject in queryset:
            temp_subject.delete()
        self.message_user(request, "Selected subjects have been rejected and deleted.")