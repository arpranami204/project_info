from django.contrib import admin
from .models import Doctor,Caretaker,ServiceApproval,AdminReport

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Caretaker)
admin.site.register(ServiceApproval)
admin.site.register(AdminReport)



