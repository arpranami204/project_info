from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_modules.adminapp import forms
from app_modules.adminapp import models
from app_modules.userapp.models import Booking
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
# from app_modules.userapp.models import CustomUser

# Create your views here.

def list_view(request):
    return render(request,'admin_temp/list.html')

def create_view(request):
    return render(request,'admin_temp/create.html')

def index_view(request):
    # tt = CustomUser.objects.all()
 
    # approved_users = CustomUser.objects.filter(is_approved=True, role__in=['Parent', 'User'])
    # rejected_users = CustomUser.objects.filter(is_approved=False, role__in=['Parent', 'User'])
    # context = {'tt': tt,'approved_users':approved_users,'rejected_users':rejected_users}
    return render(request,'admin_temp/index.html')


# =================================================================================================================================================

    



def create_doctor(request):
    form = forms.doctor_form()
    if request.method == "POST":
        form = forms.doctor_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index_view)
        else:
            print(form.errors)
    return render(request,'admin_temp/create_doctor.html', {'form': form})


def list_doctor(request):
    doctor = models.Doctor.objects.all()
    context = {'doctor':doctor}
    return render(request,'admin_temp/list_doctor.html',context)

def update_doctor(request,id):
    doctor = models.Doctor.objects.get(id=id)
    form = forms.doctor_form(instance=doctor)
    if request.method == 'POST':
        form = forms.doctor_form(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect(list_doctor)
        else:
            print(form.errors)
    context = {'doctor':doctor, 'form': form}
    return render(request,'admin_temp/update_doctor.html',context)

def delete_doctor(request,id):
    doctor = models.Doctor.objects.get(id=id)
    doctor.delete()
    return redirect(list_doctor)


# ===================================================================================================================================


def create_caretaker(request):
    form = forms.caretaker_form()
    if request.method == "POST":
        form = forms.caretaker_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index_view)
        else:
            print(form.errors)
    return render(request,'admin_temp/create_caretaker.html', {'form': form})


def list_caretaker(request):
    caretaker = models.Caretaker.objects.all()
    context = {'caretaker':caretaker}
    return render(request,'admin_temp/list_caretaker.html',context)


def update_caretaker(request,id):
    caretaker = models.Caretaker.objects.get(id=id)
    form = forms.caretaker_form(instance=caretaker)
    if request.method == 'POST':
        form = forms.caretaker_form(request.POST, request.FILES, instance=caretaker)
        if form.is_valid():
            form.save()
            return redirect(list_caretaker)
        else:
            print(form.errors)
    context = {'caretaker':caretaker, 'form': form}
    return render(request,'admin_temp/update_caretaker.html',context)


def delete_caretaker(request,id):
    caretaker = models.Caretaker.objects.get(id=id)
    caretaker.delete()
    return redirect(list_caretaker)


# ==================================================================================================================================



def create_adminreport(request):
    if request.method == "POST":
        form = forms.adminreport_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index_view)
        else:
            print(form.errors)
    return render(request,'admin_temp/create_adminreport.html')


def list_adminreport(request):
    adminreport = models.AdminReport.objects.all()
    context = {'adminreport':adminreport}
    return render(request,'admin_temp/list_adminreport.html',context)


def update_adminreport(request,id):
    adminreport = models.AdminReport.objects.get(id=id)
    if request.method == 'POST':
        form = forms.adminreport_form(request.POST,instance=adminreport)
        if form.is_valid():
            form.save()
            return redirect(list_adminreport)
        else:
            form.errors
    context = {'adminreport':adminreport}
    return render(request,'admin_temp/update_adminreport.html',context)

def delete_adminreport(request,id):
    adminreport = models.AdminReport.objects.get(id=id)
    adminreport.delete()
    return redirect(list_adminreport)


# =====================================================================================================================================

  


def create_serviceapproval(request):
    if request.method == "POST":
        form = forms.serviceapproval_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index_view)
        else:
            print(form.errors)
    return render(request,'admin_temp/create_serviceapproval.html')


def list_serviceapproval(request):
    serviceapproval = models.ServiceApproval.objects.all()
    context = {'serviceapproval':serviceapproval}
    return render(request,'admin_temp/list_serviceapproval.html',context)


def update_serviceapproval(request,id):
    serviceapproval = models.ServiceApproval.objects.get(id=id)
    if request.method == 'POST':
        form = forms.serviceapproval_form(request.POST,instance=serviceapproval)
        if form.is_valid():
            form.save()
            return redirect(list_serviceapproval)
        else:
            form.errors
    context = {'serviceapproval':serviceapproval}
    return render(request,'admin_temp/update_serviceapproval.html',context)

def delete_serviceapproval(request,id):
    serviceapproval = models.ServiceApproval.objects.get(id=id)
    serviceapproval.delete()
    return redirect(list_serviceapproval)


def list_booking_admin(request):
    bookings = Booking.objects.all()
    return render(request, 'admin_temp/list_bookings.html', {'bookings': bookings})


def approve_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.status = 'Approved'
    booking.save()
    return redirect('list_booking_admin')


def reject_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.status = 'Rejected'
    booking.save()
    return redirect('list_booking_admin')




# =================================================================================================================================
from app_modules.userapp.models import HealthRecord, Medicine, ElderProfile

def list_elderprofile_admin(request):
    elders = ElderProfile.objects.all()
    return render(request, 'admin_temp/list_elderprofile.html', {'elders': elders})

def list_healthrecord_admin(request):
    records = HealthRecord.objects.all()
    return render(request, 'admin_temp/list_healthrecord.html', {'records': records})

def create_medicine_admin(request):
    selected_elder_id = request.GET.get('elder_id')
    if request.method == "POST":
        form = forms.MedicineFormAdmin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_medicine_admin')
    else:
        initial = {}
        if selected_elder_id:
            initial['elder'] = selected_elder_id
        form = forms.MedicineFormAdmin(initial=initial)
    return render(request, 'admin_temp/create_medicine.html', {'form': form})

def list_medicine_admin(request):
    medicines = Medicine.objects.all()
    return render(request, 'admin_temp/list_medicine.html', {'medicines': medicines})

def update_medicine_admin(request, id):
    medicine = Medicine.objects.get(id=id)
    if request.method == "POST":
        form = forms.MedicineFormAdmin(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('list_medicine_admin')
    else:
        form = forms.MedicineFormAdmin(instance=medicine)
    return render(request, 'admin_temp/update_medicine.html', {'form': form})

def delete_medicine_admin(request, id):
    medicine = Medicine.objects.get(id=id)
    medicine.delete()
    return redirect('list_medicine_admin')


def loginpage_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(index_view)
        else:
            return HttpResponse("User does not exist")
    return render(request,'admin_temp/loginpage.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            try:
                User.objects.get(username==username)
                return HttpResponse("Username Alredy Exists Please Try Again")
            except:
                User.objects.create_user(username=username,password=password)
                return redirect(register_view)
        else:
            return HttpResponse("Password Do Not Match!!")
    return render(request,'admin_temp/register.html')
