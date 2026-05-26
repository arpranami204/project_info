from django.contrib import admin
from django.urls import path,include
from app_modules.userapp import views


urlpatterns = [
    
    path('',views.indexuser_view,name="indexuser_view"),
    path('about_view/',views.about_view,name="about_view"),
    path('dashboardindex_view/',views.dashboardindex_view,name="dashboardindex_view"),

    path('appointment_view/',views.appointment_view,name="appointment_view"),

    path('bookdoctor_view/',views.bookdoctor_view,name="bookdoctor_view"),

    path('caretaker_view/',views.caretaker_view,name="caretaker_view"),

    path('doctorlist_view/',views.doctorlist_view,name="doctorlist_view"),

    path('elderlist_view/',views.elderlist_view,name="elderlist_view"),

    path('profile_view/',views.profile_view,name="profile_view"),

    path('requestcaretaker_view/',views.requestcaretaker_view,name="requestcaretaker_view"),

    path('services_view/',views.services_view,name="services_view"),
    
    path('contact_view/',views.contact_view,name="contact_view"),

    path('login_view/',views.login_view,name="login_view"),
    
    path('register_view/',views.register_view,name="register_view"),
   
    path('logout/', views.logout_view, name='logout'),

    # path('approve/<int:user_id>/', views.approve_user, name='approve_user'),
    # path('reject/<int:user_id>/', views.reject_user, name='reject_user'),
    
    

    path('elderprofile/create/', views.create_elderprofile, name='create_elderprofile'),
    path('elderprofile/', views.list_elderprofile, name='list_elderprofile'),

    path('healthrecord/create/', views.create_healthrecord, name='create_healthrecord'),
    path('healthrecord/', views.list_healthrecord, name='list_healthrecord'),

    path('medicine/create/', views.create_medicine, name='create_medicine'),
    path('medicine/update/<int:id>/', views.update_medicine, name='update_medicine'),
    path('medicine/delete/<int:id>/', views.delete_medicine, name='delete_medicine'),
    path('medicine/', views.list_medicine, name='list_medicine'),

    path('booking/create/', views.create_booking, name='create_booking'),
    path('booking/', views.list_booking, name='list_booking'),

    path('payment/create/', views.create_payment, name='create_payment'),
    path('payment/checkout/<int:booking_id>/', views.checkout_view, name='checkout_view'),
    path('payment/success/<str:transaction_id>/', views.payment_success_view, name='payment_success_view'),
    path('payment/', views.list_payment, name='list_payment'),

    path('emergencyalert/create/', views.create_emergencyalert, name='create_emergencyalert'),
    path('emergencyalert/', views.list_emergencyalert, name='list_emergencyalert'),

    path('notification/create/', views.create_notification, name='create_notification'),
    path('notification/', views.list_notification, name='list_notification'),

    path('elderprofile/update/<int:id>/', views.update_elderprofile, name='update_elderprofile'),
    path('elderprofile/delete/<int:id>/', views.delete_elderprofile, name='delete_elderprofile'),

    path('healthrecord/update/<int:id>/', views.update_healthrecord, name='update_healthrecord'),
    path('healthrecord/delete/<int:id>/', views.delete_healthrecord, name='delete_healthrecord'),



    path('booking/update/<int:id>/', views.update_booking, name='update_booking'),
    path('booking/delete/<int:id>/', views.delete_booking, name='delete_booking'),

    path('payment/update/<int:id>/', views.update_payment, name='update_payment'),
    path('payment/delete/<int:id>/', views.delete_payment, name='delete_payment'),

    path('emergencyalert/update/<int:id>/', views.update_emergencyalert, name='update_emergencyalert'),
    path('emergencyalert/delete/<int:id>/', views.delete_emergencyalert, name='delete_emergencyalert'),

    path('notification/update/<int:id>/', views.update_notification, name='update_notification'),
    path('notification/delete/<int:id>/', views.delete_notification, name='delete_notification'),

]
