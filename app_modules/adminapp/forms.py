from django import forms
from app_modules.adminapp import models

class doctor_form(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = '__all__'

class caretaker_form(forms.ModelForm):
    class Meta:
        model = models.Caretaker
        fields = '__all__'

class adminreport_form(forms.ModelForm):
    class Meta:
        model = models.AdminReport
        fields = '__all__'


class serviceapproval_form(forms.ModelForm):
    class Meta:
        model = models.ServiceApproval
        fields = '__all__'


from app_modules.userapp.models import Medicine, ElderProfile

class MedicineFormAdmin(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['elder', 'medicine_name', 'dosage', 'frequency', 'start_date', 'end_date', 'instructions']
        widgets = {
            'elder': forms.Select(attrs={'class': 'form-control'}),
            'medicine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Paracetamol'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 500mg'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Twice a day'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['elder'].queryset = ElderProfile.objects.all()
        # Optionally customize label to include Username
        self.fields['elder'].label_from_instance = lambda obj: f"{obj.full_name} (User: {obj.user.username})"
