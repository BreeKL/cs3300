from django.urls import path
from . import views
#from portfolio_app.views import StudentListView, StudentDetailView

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('login/', views.login, name='login'),
path('logout/', views.logout, name='logout'),
path('students/', views.StudentListView.as_view(), name='students'),
path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
]

# url patterns for Create-Update-Delete forms
urlpatterns += [
    path('project/create/', views.CreateProject.as_view(), name='create-project'),
    path('project/<int:pk>/update/', views.UpdateProject.as_view(), name='update-project'),
    path('project/<int:pk>/delete/', views.DeleteProject.as_view(), name='delete-project'),
    path('portfolio/<int:pk>/update', views.UpdatePortfolio.as_view(), name = 'update-portfolio'),
]
