from django.contrib import admin
from django.urls import path,include
from app_modules.adminapp import views

urlpatterns = [

    path('list_view/',views.list_view,name="list_view"),

    path('create_view/',views.create_view,name="create_view"),

    path('index_view/',views.index_view,name="index_view"),

    path('create_doctor/',views.create_doctor,name="create_doctor"),
    path('list_doctor/',views.list_doctor,name="list_doctor"),
    path('update_doctor/<int:id>',views.update_doctor,name="update_doctor"),
    path('delete_doctor/<int:id>',views.delete_doctor,name="delete_doctor"),
    

    path('create_caretaker/',views.create_caretaker,name="create_caretaker"),
    path('list_caretaker/',views.list_caretaker,name="list_caretaker"),
    path('update_caretaker/<int:id>',views.update_caretaker,name="update_caretaker"),
    path('delete_caretaker/<int:id>',views.delete_caretaker,name="delete_caretaker"),\
        
    path('create_adminreport/',views.create_adminreport,name="create_adminreport"),
    path('list_adminreport/',views.list_adminreport,name="list_adminreport"),
    path('update_adminreport/<int:id>',views.update_adminreport,name="update_adminreport"),
    path('delete_adminreport/<int:id>',views.delete_adminreport,name="delete_adminreport"),


    path('create_serviceapproval/',views.create_serviceapproval,name="create_serviceapproval"),
    path('list_serviceapproval/',views.list_serviceapproval,name="list_serviceapproval"),
    path('update_serviceapproval/<int:id>',views.update_serviceapproval,name="update_serviceapproval"),
    path('delete_serviceapproval/<int:id>',views.delete_serviceapproval,name="delete_serviceapproval"),
    
    path('list_booking_admin/', views.list_booking_admin, name="list_booking_admin"),
    path('approve_booking/<int:id>/', views.approve_booking, name="approve_booking"),
    path('reject_booking/<int:id>/', views.reject_booking, name="reject_booking"),

    path('list_healthrecord_admin/', views.list_healthrecord_admin, name="list_healthrecord_admin"),
    path('list_elderprofile_admin/', views.list_elderprofile_admin, name="list_elderprofile_admin"),
    
    path('create_medicine_admin/', views.create_medicine_admin, name="create_medicine_admin"),
    path('list_medicine_admin/', views.list_medicine_admin, name="list_medicine_admin"),
    path('update_medicine_admin/<int:id>/', views.update_medicine_admin, name="update_medicine_admin"),
    path('delete_medicine_admin/<int:id>/', views.delete_medicine_admin, name="delete_medicine_admin"),

    path('loginpage_view/',views.loginpage_view,name="loginpage_view"),

    path('register_view/',views.register_view,name="register_view"), 

    


    

        
]
