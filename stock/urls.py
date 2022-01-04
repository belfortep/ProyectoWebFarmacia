from django.urls import path

from . import views

app_name='stock'

urlpatterns = [

    path('', views.farmacia, name="Farmacia"), 
    path('edit/<int:id>', views.edit, name="Edit"),
    path('create/', views.create, name="Create"),
    path('delete/<int:id>', views.delete, name="Delete"),
    path('liquidos/', views.farmaciaLiquido, name="FarmaciaLiquido"),
    path('editliq/<int:id>', views.editLiquido, name="EditLiquido"),
    path('createliq/', views.createLiquido, name="CreateLiquido"),
    path('deleteliq/<int:id>', views.deleteLiquido, name="DeleteLiquido")
    
    
    
    

]