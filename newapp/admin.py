from django.contrib import admin
from .models import (
            School, 
            AdmissionEnquiry, 
            AdmissionDetails, 
            Admission,
            Facilities,
            Fees
        )

admin.site.register(School)
admin.site.register(Fees)
admin.site.register(AdmissionEnquiry)
admin.site.register(AdmissionDetails)
admin.site.register(Admission)
admin.site.register(Facilities)
