from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    School,
    AdmissionEnquiry,
    AdmissionDetails,
    Admission,
    Facilities,
    Fees
)

from .forms import (
    SchoolForm,
    AdmissionForm,
    AdmissionDetailsForm,
    AdmissionEnquiryForm,
    FeesForm
)


def home(request):
    return render(request, "home.html")


def facilities(request,pk):
    school_obj = School.objects.get(pk=pk)
    if not Facilities.objects.filter(school = school_obj):
        if request.method == 'POST':
            sports = request.POST.getlist('sports')
            education = request.POST.getlist('education')
            classroom = request.POST.getlist('classroom')
            visual = request.POST.getlist('visual')
            laboratories = request.POST.getlist('laboratories')
            transport = request.POST.getlist('transport')
            boarding = request.POST.getlist('boarding')
            accessibility = request.POST.getlist('accessibility')
            digital = request.POST.getlist('digital')
            safety = request.POST.getlist('safety')
            food = request.POST.getlist('food')
            medical = request.POST.getlist('medical')
            other = request.POST.getlist('other')


            facilities = Facilities.objects.create(
                school = school_obj,
                sports_facilities = ",".join(sports),
                education_facilities = ",".join(education),
                classroom_facilities = ",".join(classroom),
                visual_and_performing_art_facilities = ",".join(visual),
                laboratories_facilities = ",".join(laboratories),
                transport_facilities = ",".join(transport),
                boarding_facilities = ",".join(boarding),
                accessibility_facilities = ",".join(accessibility),
                digital_facilities = ",".join(digital),
                safety_and_security_facilities = ",".join(safety),
                food_and_catering_facilities = ",".join(food),
                medical_facility_facilities = ",".join(medical),
                other_infra_facilities = ",".join(other)
            )
            facilities.save()
            return render(request, 'success.html')
    else:
        return render(request, 'success.html')
    return render(request, "facilities.html")


def school(request):
    if request.method == 'POST':
        #school form
        school_obj = None
        school_form_a = SchoolForm(request.POST)
        if school_form_a.is_valid(): 
            try:
                task = school_form_a.save()
                school_obj = get_object_or_404(School, pk=task.id)
            except:
                print("SchoolForm form error")

        #fee form
        class_name = request.POST.getlist("class_name")
        fee_type = request.POST.getlist("fee_type")
        amount = request.POST.getlist("amount")
        frequency = request.POST.getlist("frequency")
        for i in range(len(fee_type)):
            form = Fees.objects.create(
                school = school_obj,
                class_name=class_name[i],
                fee_type=fee_type[i],
                amount=amount[i],
                frequency=frequency[i])
            try:
                form.save()
            except:
                print("Fees form error")
        
        #admission form
        admission_details = AdmissionDetailsForm(request.POST)
        if admission_details.is_valid(): 
            temp_obj = admission_details.save(commit=False)
            temp_obj.school = school_obj
            temp_obj.save()

        #admission form
        admission_form_a = AdmissionForm(request.POST)
        if admission_form_a.is_valid(): 
            admission_form_a.save()

        #facilities form
        sports = request.POST.getlist('sports')
        education = request.POST.getlist('education')
        classroom = request.POST.getlist('classroom')
        visual = request.POST.getlist('visual')
        laboratories = request.POST.getlist('laboratories')
        transport = request.POST.getlist('transport')
        boarding = request.POST.getlist('boarding')
        accessibility = request.POST.getlist('accessibility')
        digital = request.POST.getlist('digital')
        safety = request.POST.getlist('safety')
        food = request.POST.getlist('food')
        medical = request.POST.getlist('medical')
        other = request.POST.getlist('other')

        facilities = Facilities.objects.create(
            school = school_obj,
            sports_facilities = ",".join(sports),
            education_facilities = ",".join(education),
            classroom_facilities = ",".join(classroom),
            visual_and_performing_art_facilities = ",".join(visual),
            laboratories_facilities = ",".join(laboratories),
            transport_facilities = ",".join(transport),
            boarding_facilities = ",".join(boarding),
            accessibility_facilities = ",".join(accessibility),
            digital_facilities = ",".join(digital),
            safety_and_security_facilities = ",".join(safety),
            food_and_catering_facilities = ",".join(food),
            medical_facility_facilities = ",".join(medical),
            other_infra_facilities = ",".join(other)
        )
        try:
            facilities.save()
        except:
            print("facilities form error")
        return render(request, 'success.html')
    else:
        school_form = SchoolForm()
        admission_details_form = AdmissionDetailsForm()
        admission_form = AdmissionForm()
        context = {
            'school_form': school_form,
            'admission_details_form': admission_details_form,
            'admission_form': admission_form,
        }
    return render(request, 'school.html', context=context)



def admissionDetails(request):
    if request.method == 'POST':
        form = AdmissionDetailsForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = AdmissionDetailsForm()
    return render(request, 'admissionDetails.html', {'form': form})


def admissionEnquiry(request):
    if request.method == 'POST':
        form = AdmissionEnquiryForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = AdmissionEnquiryForm()
    return render(request, 'admissionEnquiry.html', {'form': form})

def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = AdmissionForm()
    return render(request, 'admission.html', {'form': form})


def fees(request):
    if request.method == 'POST':
        class_name = request.POST.getlist("class_name")
        fee_type = request.POST.getlist("fee_type")
        amount = request.POST.getlist("amount")
        frequency = request.POST.getlist("frequency")
        for i in range(len(class_name)):
            form = Fees.objects.create(
                class_name=class_name[i],
                fee_type=fee_type[i],
                amount=amount[i],
                frequency=frequency[i])
            form.save()
        return render(request, 'success.html')
    return render(request, 'fees.html')