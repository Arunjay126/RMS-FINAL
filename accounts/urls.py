
from django.urls import path
from .views import login_view,home_view,ai_department,cs_department,ec_department,chemical_department,industrial_chemistry_department,civil_department,physics_department,mathematics_department,mechanical_department

urlpatterns = [
    path('login/', login_view, name='login'),
    path("home/", home_view, name="home"),
    path("ai-department/", ai_department, name="ai-department"),
    path("cs-department/", cs_department, name="cs-department"),
    path("ec-department/", ec_department, name="ec-department"),
    path("chemical-department/", chemical_department, name="chemical-department"),
    path("industrial-chemistry-department/", industrial_chemistry_department, name="industrial-chemistry-department"),
    path("civil-department/",civil_department, name="civil-department"),
    path("physics-department/", physics_department, name="physics-department"),
    path("mathematics-department/", mathematics_department, name="mathematics-department"),
    path("mechanical-department/", mechanical_department, name="mechanical-department"), 
]