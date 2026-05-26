from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from app_modules.userapp import models as userapp_models
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from app_modules.adminapp import models
   



 
# Create your views here.
def indexuser_view(request):
    return render(request,'user_temp/indexuser.html')

def about_view(request):
    return render(request,'user_temp/about.html')

@login_required
def dashboardindex_view(request):
    elder_count = userapp_models.ElderProfile.objects.filter(user=request.user).count() 
    booking_count = userapp_models.Booking.objects.filter(user=request.user).count()
    medicine_count = userapp_models.Medicine.objects.filter(elder__user=request.user).count()
    sos_count = userapp_models.EmergencyAlert.objects.filter(user=request.user).count()
    
    # Get the latest health record for any of the user's elders
    latest_record = userapp_models.HealthRecord.objects.filter(elder__user=request.user).order_by('-recorded_date').first()
    
    context = {
        'elder_count': elder_count,
        'booking_count': booking_count,
        'medicine_count': medicine_count,
        'sos_count': sos_count,
        'latest_record': latest_record,
    }
    return render(request, 'user_temp/dashboardindex.html', context)

@login_required
def appointment_view(request):
    bookings = userapp_models.Booking.objects.filter(user=request.user).order_by('-created_at')
    
    # Calculate stats
    total_bookings = bookings.count()
    completed_count = bookings.filter(status='Completed').count()
    pending_count = bookings.filter(status__in=['Pending', 'Approved']).count()
    
    # Calculate total spent (from completed payments)
    total_spent = userapp_models.Payment.objects.filter(booking__user=request.user, payment_status='Completed').aggregate(Sum('amount'))['amount__sum'] or 0
    
    context = {
        'bookings': bookings,
        'total_bookings': total_bookings,
        'completed_count': completed_count,
        'pending_count': pending_count,
        'total_spent': total_spent,
    }
    return render(request, 'user_temp/appointment_history.html', context)

def contact_view(request):
    return render(request,'user_temp/contact.html')

def bookdoctor_view(request):
    return render(request,'user_temp/book_doctor.html')


def caretaker_view(request):
     caretakers = models.Caretaker.objects.all()
     return render(request,'user_temp/caretaker_list.html', {'caretaker': caretakers})

def dashboard_view(request):
     return render(request,'user_temp/dashboard.html')

def doctorlist_view(request):
     doctors = models.Doctor.objects.all()
     context = {'doct': doctors}
     return render(request,'user_temp/doctor_list.html', context)

def elderlist_view(request):
    return render(request,'user_temp/elder_list.html') 

def login_view(request):
    return render(request,'user_temp/login.html')

def profile_view(request):
    return render(request,'user_temp/profile.html')

def register_view(request):
    return render(request,'user_temp/register.html')

def requestcaretaker_view(request):
    return render(request,'user_temp/request_caretaker.html')

def services_view(request):
    return render(request,'user_temp/services.html')






from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app_modules.userapp import forms
from django.contrib import messages


# REGISTER
def register_view(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login_view')
    else:
        form = forms.RegisterForm()

    return render(request, 'user_temp/register.html', {'form': form})


# LOGIN (COMMON)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'admin':
                return redirect('index_view')
            else:
                return redirect('dashboardindex_view')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'user_temp/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required
def create_elderprofile(request):
    if request.method == "POST":
        form = forms.ElderProfileForm(request.POST)
        if form.is_valid():
            elder = form.save(commit=False)
            elder.user = request.user
            elder.save()
            return redirect('list_elderprofile')
    else:
        form = forms.ElderProfileForm()
    return render(request, 'user_temp/create_elderprofile.html', {'form': form})

@login_required
def list_elderprofile(request):
    profiles = userapp_models.ElderProfile.objects.filter(user=request.user)
    return render(request, 'user_temp/list_elderprofile.html', {'profiles': profiles})


@login_required
def create_healthrecord(request):
    if not userapp_models.ElderProfile.objects.filter(user=request.user).exists():
        messages.error(request, "Please create an Elder Profile first to add a Health Record.")
        return redirect('create_elderprofile')

    if request.method == "POST":
        form = forms.HealthRecordForm(request.user, request.POST)
        if form.is_valid():
            hr = form.save(commit=False)
            hr.save()
            return redirect('list_healthrecord')
    else:
        form = forms.HealthRecordForm(request.user)
    return render(request, 'user_temp/create_healthrecord.html', {'form': form})

@login_required
def list_healthrecord(request):
    records = userapp_models.HealthRecord.objects.filter(elder__user=request.user)
    return render(request, 'user_temp/list_healthrecord.html', {'records': records})




@login_required
def list_medicine(request):
    medicines = userapp_models.Medicine.objects.filter(elder__user=request.user)
    return render(request, 'user_temp/list_medicine.html', {'medicines': medicines})

@login_required
def create_medicine(request):
    if not userapp_models.ElderProfile.objects.filter(user=request.user).exists():
        messages.error(request, "Please create an Elder Profile first to add Medicine.")
        return redirect('create_elderprofile')
        
    if request.method == "POST":
        form = forms.MedicineForm(request.user, request.POST)
        if form.is_valid():
            med = form.save(commit=False)
            med.save()
            return redirect('list_medicine')
    else:
        form = forms.MedicineForm(request.user)
    return render(request, 'user_temp/create_medicine.html', {'form': form})

@login_required
def update_medicine(request, id):
    obj = get_object_or_404(userapp_models.Medicine, id=id, elder__user=request.user)
    if request.method == "POST":
        form = forms.MedicineForm(request.user, request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_medicine')
    else:
        form = forms.MedicineForm(request.user, instance=obj)
    return render(request, 'user_temp/update_medicine.html', {'form': form})

@login_required
def delete_medicine(request, id):
    obj = get_object_or_404(userapp_models.Medicine, id=id, elder__user=request.user)
    obj.delete()
    return redirect('list_medicine')


@login_required
def create_booking(request):
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('list_booking')
    else:
        initial_data = {}
        if 'doctor' in request.GET:
            initial_data['service_type'] = 'Doctor Consultation'
            initial_data['description'] = f"Requested Booking for Dr. {request.GET.get('doctor')}"
        elif 'caretaker' in request.GET:
            initial_data['service_type'] = 'Caretaker Request'
            initial_data['description'] = f"Requested Caretaker: {request.GET.get('caretaker')}"
            
        form = forms.BookingForm(initial=initial_data)
        
    return render(request, 'user_temp/create_booking.html', {'form': form})

@login_required
def list_booking(request):
    bookings = userapp_models.Booking.objects.filter(user=request.user)
    return render(request, 'user_temp/list_booking.html', {'bookings': bookings})


@login_required
def create_payment(request):
    if request.method == "POST":
        form = forms.PaymentForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_payment')
    else:
        form = forms.PaymentForm(request.user)
    return render(request, 'user_temp/create_payment.html', {'form': form})

import random
import string

@login_required
def checkout_view(request, booking_id):
    booking = get_object_or_404(userapp_models.Booking, id=booking_id, user=request.user)
    
    # Static amounts for demonstration
    amount = 500.00
    if 'caretaker' in booking.service_type.lower():
        amount = 1000.00
    elif 'doctor' in booking.service_type.lower():
        amount = 750.00
        
    if request.method == "POST":
        payment_method = request.POST.get('payment_method', 'Manual')
        transaction_id = 'STATIC-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        
        # Create a real payment record in the DB (Simulated)
        userapp_models.Payment.objects.create(
            booking=booking,
            amount=amount,
            payment_method=payment_method,
            payment_status='Completed',
            transaction_id=transaction_id
        )
        
        # Update booking status
        booking.status = 'Confirmed'
        booking.save()
        
        return redirect('payment_success_view', transaction_id=transaction_id)
        
    return render(request, 'user_temp/checkout.html', {'booking': booking, 'amount': amount})

@login_required
def payment_success_view(request, transaction_id):
    payment = get_object_or_404(userapp_models.Payment, transaction_id=transaction_id, booking__user=request.user)
    return render(request, 'user_temp/payment_success.html', {'payment': payment})

@login_required
def list_payment(request):
    payments = userapp_models.Payment.objects.filter(booking__user=request.user)
    return render(request, 'user_temp/list_payment.html', {'payments': payments})


@login_required
def create_emergencyalert(request):
    if request.method == "POST":
        form = forms.EmergencyAlertForm(request.user, request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            return redirect('list_emergencyalert')
    else:
        form = forms.EmergencyAlertForm(request.user)
    return render(request, 'user_temp/create_emergencyalert.html', {'form': form})

@login_required
def list_emergencyalert(request):
    alerts = userapp_models.EmergencyAlert.objects.filter(user=request.user)
    return render(request, 'user_temp/list_emergencyalert.html', {'alerts': alerts})


@login_required
def create_notification(request):
    if request.method == "POST":
        form = forms.NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.user = request.user
            notification.save()
            return redirect('list_notification')
    else:
        form = forms.NotificationForm()
    return render(request, 'user_temp/create_notification.html', {'form': form})

@login_required
def list_notification(request):
    notifications = userapp_models.Notification.objects.filter(user=request.user)
    return render(request, 'user_temp/list_notification.html', {'notifications': notifications})

# ==========================================
# UPDATE AND DELETE VIEWS
# ==========================================

@login_required
def update_elderprofile(request, id):
    obj = get_object_or_404(userapp_models.ElderProfile, id=id, user=request.user)
    if request.method == "POST":
        form = forms.ElderProfileForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_elderprofile')
    else:
        form = forms.ElderProfileForm(instance=obj)
    return render(request, 'user_temp/update_elderprofile.html', {'form': form})

@login_required
def delete_elderprofile(request, id):
    obj = get_object_or_404(userapp_models.ElderProfile, id=id, user=request.user)
    obj.delete()
    return redirect('list_elderprofile')

@login_required
def update_healthrecord(request, id):
    obj = get_object_or_404(userapp_models.HealthRecord, id=id, elder__user=request.user)
    if request.method == "POST":
        form = forms.HealthRecordForm(request.user, request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_healthrecord')
    else:
        form = forms.HealthRecordForm(request.user, instance=obj)
    return render(request, 'user_temp/update_healthrecord.html', {'form': form})

@login_required
def delete_healthrecord(request, id):
    obj = get_object_or_404(userapp_models.HealthRecord, id=id, elder__user=request.user)
    obj.delete()
    return redirect('list_healthrecord')




@login_required
def update_booking(request, id):
    obj = get_object_or_404(userapp_models.Booking, id=id, user=request.user)
    if request.method == "POST":
        form = forms.BookingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_booking')
    else:
        form = forms.BookingForm(instance=obj)
    return render(request, 'user_temp/update_booking.html', {'form': form})

@login_required
def delete_booking(request, id):
    obj = get_object_or_404(userapp_models.Booking, id=id, user=request.user)
    obj.delete()
    return redirect('list_booking')


@login_required
def update_payment(request, id):
    obj = get_object_or_404(userapp_models.Payment, id=id, booking__user=request.user)
    if request.method == "POST":
        form = forms.PaymentForm(request.user, request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_payment')
    else:
        form = forms.PaymentForm(request.user, instance=obj)
    return render(request, 'user_temp/update_payment.html', {'form': form})

@login_required
def delete_payment(request, id):
    obj = get_object_or_404(userapp_models.Payment, id=id, booking__user=request.user)
    obj.delete()
    return redirect('list_payment')


@login_required
def update_emergencyalert(request, id):
    obj = get_object_or_404(userapp_models.EmergencyAlert, id=id, user=request.user)
    if request.method == "POST":
        form = forms.EmergencyAlertForm(request.user, request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_emergencyalert')
    else:
        form = forms.EmergencyAlertForm(request.user, instance=obj) 
    return render(request, 'user_temp/update_emergencyalert.html', {'form': form})

@login_required
def delete_emergencyalert(request, id):
    obj = get_object_or_404(userapp_models.EmergencyAlert, id=id, user=request.user) 
    obj.delete()
    return redirect('list_emergencyalert')


@login_required
def update_notification(request, id):
    obj = get_object_or_404(userapp_models.Notification, id=id, user=request.user)
    if request.method == "POST":
        form = forms.NotificationForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_notification')
    else:
        form = forms.NotificationForm(instance=obj)
    return render(request, 'user_temp/update_notification.html', {'form': form})

@login_required
def delete_notification(request, id):
    obj = get_object_or_404(userapp_models.Notification, id=id, user=request.user)
    obj.delete()
    return redirect('list_notification')
