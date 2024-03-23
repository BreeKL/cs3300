from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import ListView, DetailView

# for forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# and HttpResponseRedirect from above

# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    # Render index.html
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

def login(request):
    return render (HttpResponse, 'Login page')
def logout(request):
    return render (HttpResponse, 'Logout Page')

# def student_list(request):
#     student_list = Student.objects.select_related('name').all()
#     print("active student_list query set:", student_list)
#     return render( request, 'portfolio_app/student_list.html', {'student_list':student_list})

# def student_detail(request):
#     return render( request, 'portfolio_app/student_detail.html')

# def portfolio_detail(request, id):
#     project_list = Project.objects.all()
#     print("Projects in portfolio: ", project_list)
#     return render( request, 'portfolio_app/portfolio_detail.html', {'project_list':project_list})

class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class PortfolioDetailView(DetailView):
    model = Portfolio

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project
    
# --------------------------------------------------------
# for generic forms
# --------------------------------------------------------
class CreateProject(CreateView):
    model = Project
    fields = '__all__'

class UpdateProject(UpdateView):
    model = Project
    fields = ['title', 'description']

class DeleteProject(DeleteView):
    model = Project
    success_url = reverse_lazy('index')

class UpdatePortfolio(UpdateView):
    model = Portfolio
    fields = '__all__'