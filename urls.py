from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views  # ✅ Import Django auth views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ Fix login/logout URL issue
    path('', views.homer, name='home'),  
    path('add/', views.add_expense, name='add_expense'),  
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),  
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # ✅ Custom login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # ✅ Logout functionality
]
