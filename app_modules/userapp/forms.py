
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ElderProfile, HealthRecord, Medicine, Booking, Payment, EmergencyAlert, Notification


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'phone_number',
            'profile_image',
            'date_of_birth',
            'gender',
            'address'
        ] 

    def clean_username(self):  
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():  
            raise forms.ValidationError("Email already registered!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match!")

        return cleaned_data

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters!")

        if password.isdigit():
            raise forms.ValidationError("Password cannot be only numbers!")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'user'
        if commit:
            user.save()
        return user




    


class ElderProfileForm(forms.ModelForm):
    class Meta:
        model = ElderProfile
        fields = ['full_name', 'age', 'gender', 'blood_group', 'medical_condition', 'emergency_contact', 'relation_with_user']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. Ramesh Kumar'}),
            'age': forms.NumberInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. 72', 'min': '0'}),
            'gender': forms.Select(attrs={'class': 'form-ctrl'}, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
            'blood_group': forms.Select(attrs={'class': 'form-ctrl'}, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')]),
            'medical_condition': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. Diabetes, Hypertension'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': '+91 XXXXX XXXXX'}),
            'relation_with_user': forms.Select(attrs={'class': 'form-ctrl'}, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Grandfather', 'Grandfather'), ('Grandmother', 'Grandmother'), ('Other', 'Other')]),
        }

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['elder', 'blood_pressure', 'sugar_level', 'weight', 'heart_rate', 'temperature', 'notes', 'recorded_date']
        widgets = {
            'elder': forms.Select(attrs={'class': 'form-ctrl'}),
            'blood_pressure': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. 120/80'}),
            'sugar_level': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. 95 mg/dL'}),
            'weight': forms.NumberInput(attrs={'class': 'form-ctrl', 'step': '0.1'}),
            'heart_rate': forms.NumberInput(attrs={'class': 'form-ctrl'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-ctrl', 'step': '0.1'}),
            'notes': forms.Textarea(attrs={'class': 'form-ctrl', 'rows': 3}),
            'recorded_date': forms.DateTimeInput(attrs={'class': 'form-ctrl', 'type': 'datetime-local'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(HealthRecordForm, self).__init__(*args, **kwargs)
        self.fields['elder'].queryset = ElderProfile.objects.filter(user=user)


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['elder', 'medicine_name', 'dosage', 'frequency', 'start_date', 'end_date', 'instructions']
        widgets = {
            'elder': forms.Select(attrs={'class': 'form-ctrl'}),
            'medicine_name': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. Paracetamol'}),
            'dosage': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. 500mg'}),
            'frequency': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. Twice a day'}),
            'start_date': forms.DateInput(attrs={'class': 'form-ctrl', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-ctrl', 'type': 'date'}),
            'instructions': forms.Textarea(attrs={'class': 'form-ctrl', 'rows': 3}),
        }

    def __init__(self, user, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)
        self.fields['elder'].queryset = ElderProfile.objects.filter(user=user)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service_type', 'booking_date', 'booking_time', 'description']
        widgets = {
            'service_type': forms.TextInput(attrs={'class': 'form-ctrl', 'placeholder': 'e.g. Doctor Consultation'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-ctrl', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-ctrl', 'type': 'time'}),
            'description': forms.Textarea(attrs={'class': 'form-ctrl', 'rows': 3}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount', 'payment_method']
        widgets = {
            'booking': forms.Select(attrs={'class': 'form-ctrl'}),
            'amount': forms.NumberInput(attrs={'class': 'form-ctrl', 'step': '0.01'}),
            'payment_method': forms.Select(attrs={'class': 'form-ctrl'}, choices=[('Card', 'Card'), ('UPI', 'UPI'), ('Cash', 'Cash')]),
        }

    def __init__(self, user, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['booking'].queryset = Booking.objects.filter(user=user)


class EmergencyAlertForm(forms.ModelForm):
    class Meta:
        model = EmergencyAlert
        fields = ['elder', 'alert_message']
        widgets = {
            'elder': forms.Select(attrs={'class': 'form-ctrl'}),
            'alert_message': forms.Textarea(attrs={'class': 'form-ctrl', 'rows': 3, 'placeholder': 'Describe emergency...'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(EmergencyAlertForm, self).__init__(*args, **kwargs)
        self.fields['elder'].queryset = ElderProfile.objects.filter(user=user)


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-ctrl'}),
            'message': forms.Textarea(attrs={'class': 'form-ctrl', 'rows': 3}),
        }