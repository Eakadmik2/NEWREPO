from django.shortcuts import render


def staff_home(request):
    return render(request, "staff_template/staff_home_template.html")

def staff_take_attendance(request):
    return render(request,"staff_template/staff_take_attendance.html")
