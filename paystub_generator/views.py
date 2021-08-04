from base64 import b64encode

from django.http import HttpResponse
from django.shortcuts import render
from datetime import timedelta, datetime, date
from .forms import image_upload_form
from .import forms as abc
# Create your views here.
from paystub_generator.models import State, image_upld

def about_us(request):
    return render(request, 'paystub_generator/aboutus.html')

def base(request):
    return render(request, 'paystub_generator/new aba.html')

def federal_tax(salary):
    if int(salary) >= 20000 and int(salary) <= 25000:
        fd_tax = int(salary) / 10.99
    elif int(salary) >= 25000 and int(salary) <= 30000:
        fd_tax = int(salary) / 10.39
    elif int(salary) > 30000 and int(salary) <= 35000:
        fd_tax = int(salary) / 10.01
    elif int(salary) > 35000 and int(salary) <= 40000:
        fd_tax = int(salary) / 9.75
    elif int(salary) > 40000 and int(salary) <= 45000:
        fd_tax = int(salary) / 9.55
    elif int(salary) > 45000 and int(salary) <= 50000:
        fd_tax = int(salary) / 8.78
    elif int(salary) > 50000 and int(salary) <= 55000:
        fd_tax = int(salary) / 8.07
    elif int(salary) > 55000 and int(salary) <= 60000:
        fd_tax = int(salary) / 7.56
    elif int(salary) > 60000 and int(salary) <= 65000:
        fd_tax = int(salary) / 7.18
    elif int(salary) > 65000 and int(salary) <= 70000:
        fd_tax = int(salary) / 6.88
    elif int(salary) > 70000 and int(salary) <= 75000:
        fd_tax = int(salary) / 6.64
    elif int(salary) > 75000 and int(salary) <= 80000:
        fd_tax = int(salary) / 6.45
    elif int(salary) > 80000 and int(salary) <= 85000:
        fd_tax = int(salary) / 6.29
    elif int(salary) > 85000 and int(salary) <= 90000:
        fd_tax = int(salary) / 6.16
    elif int(salary) > 90000 and int(salary) <= 95000:
        fd_tax = int(salary) / 6.01
    elif int(salary) > 95000 and int(salary) <= 100000:
        fd_tax = int(salary) / 5.88
    else:
        fd_tax = 0

    return fd_tax


def state_tax(salary, r1, r2, r3, r4, r5, r6, r7, r8):
    if 20000 <= int(salary) <= 30000:
        stat_tax = int(salary) / r1
    elif 30000 < int(salary) <= 40000:
        stat_tax = int(salary) / r2
    elif 40000 < int(salary) <= 50000:
        stat_tax = int(salary) / r3
    elif 50000 < int(salary) <= 60000:
        stat_tax = int(salary) / r4
    elif 60000 < int(salary) <= 70000:
        stat_tax = int(salary) / r5
    elif 70000 < int(salary) <= 80000:
        stat_tax = int(salary) / r6
    elif 80000 < int(salary) <= 90000:
        stat_tax = int(salary) / r7
    elif 90000 < int(salary) <= 100000:
        stat_tax = int(salary) / r8
    else:
        stat_tax = 0

    stat_tax = round(stat_tax, 2)
    return stat_tax


def homepage(request):
    return render(request, 'paystub_generator/home_page.html')


def faq(request):
    return render(request, 'paystub_generator/faq.html')


def stub_samples(request):
    return render(request, 'paystub_generator/stub_samples.html')


def create_your_stub(request):
    global fd, St, M, wkc, td, SS, mediC, sdi, D, ytd_sui, ytd_deduction, ytd_gross, sui, current_deduction, ytd_netpay, current_total, net_pay, ytd_td, ytd_st, ytd_fd, ytd_ss, ytd_sdi, ytd_wkc, ytd_medic
    fd = St = M = wkc = td = SS = mediC = sdi = D = ytd_sui = ytd_deduction = ytd_gross = sui = current_deduction = ytd_netpay = current_total = net_pay = 0
    pay_date_minus = date(2021, 1, 1)

    if request.POST:
        state = request.POST.get("state")
        img = image_upld.objects.all()
        img.delete()
        form = abc.image_upload_form(request.POST, request.FILES)
        form.save()

        obj2 = image_upld.objects.last()


        obj = State.objects.get(state_name=state)
        print(obj)

        # inImg = request.FILES["logo"]
        emp_radio = request.POST.get("Emp_radio")
        emp_name = request.POST.get("emp_name")
        security = request.POST.get("emp_sec_num")
        emp_address = request.POST.get("emp_address")
        zip_code = request.POST.get("zip_code")
        emp_id = request.POST.get("emp_id")
        martial_status = request.POST.get("martial_status")
        dependants = request.POST.get("dependants")
        blind_exem = request.POST.get("blind_exem")
        company_name = request.POST.get("company_name")
        company_address = request.POST.get("company_address")
        company_phone = request.POST.get("company_phone")
        company_zip_code = request.POST.get("company_zip_code")
        ein_ssn_no = request.POST.get("ein_ssn_no")
        salary_info_hourly = request.POST.get("salary_info_hourly")
        salary_info_salary = request.POST.get("salary_info_salary")
        weekly = request.POST.get("weekly")
        hourly = request.POST.get("hourly")
        pay_date = request.POST.get("pay_date")
        total_hour = request.POST.get("total_hour")
        fixed_schedule = request.POST.get("fixed_schedule")
        varied_schedule = request.POST.get("varied_schedule")
        hours_worked = request.POST.get("hours_worked")
        joined_in2021 = request.POST.get("joined_in2021")
        ch_no_Choose = request.POST.get("ch_no_Choose")
        emp_sec_num = request.POST.get("emp_sec_num")
        company_ein_ssn_no = request.POST.get("company_ein/ssn_no")
        salary_type = request.POST.get("salary_info")
        hourly_rate = request.POST.get("hourly_rate")
        hours_worked = request.POST.get("total_hour")

        print("salary type", salary_type)

        # print("emp_address" + emp_address)
        # print("zip_code0 " + zip_code)
        # print("emp_id"+ emp_id)
        # print("martial_status" + martial_status)
        # print("dependants" + dependants)
        # print("blind_exem" + blind_exem)
        # print("company_name" + company_name)
        # print("company_address" + company_address)
        # print("company_phone" + company_phone)
        # print("company_zip_code" + company_zip_code)
        # print("pay_date" + pay_date)
        # # print("salary_info_hourly" + salary_info_hourly)
        # print("total_hour" + total_hour)
        # print("hours_worked" + hours_worked)
        # print("fixed_schedule" + fixed_schedule)
        firstdate = date(date.today().year, 1, 1)

        pay_date = datetime.strptime(pay_date, '%Y-%m-%d')

        print(pay_date)
        days = pay_date.date() - firstdate
        days = days.days
        week = datetime.strftime(pay_date, '%U')
        week = int(week)
        print("weeks :", week)
        month = pay_date.month

        semi_monthly = month * 2
        if 1 <= month <= 3:
            quartely = 1
        if 4 <= month <= 6:
            quartely = 2
        if 7 <= month <= 9:
            quartely = 3
        if 10 <= month <= 12:
            quartely = 4
        if 1 <= month <= 6:
            semi_anuaaly = 1
        if 7 <= month <= 12:
            semi_anuaaly = 2
        print("--------------")
        print(week)
        print("===========")
        days_3_pay_date = pay_date - timedelta(days=3)
        # start_date = date(2021,1,1)
        print("----------------------")
        print(days_3_pay_date.date())
        print("----------------------")
        # jke= ab.date() - start_date
        # jky_days = jke.days
        # print(jky_days)

        if salary_type == "salary":
            print(salary_type)
            if weekly == "Once":
                print("Once")
                D = 1
                M = 1
                print("federal tax ==")
                print(fd)

                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)

                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    # fd = fd /2
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Daily":
                print('Daily')
                D = 360
                M = days
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 360
                print(pay_date)
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 360
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 360
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 360
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 360
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 360
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 360
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 360
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 360
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 360
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 360
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 360
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 360
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 360
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Weekly":
                print("Weekly")
                D = 52
                M = week
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 52
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 52
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 52
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 52
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 52
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 52
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 52
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 52
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 52
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 52
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 52
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 52
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 52
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 52
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "BI_Weekly":
                print("BI_Weekly")
                D = 26
                M = int(week) / 2
                print("federal tax ==")
                print(M)
                # hourly = int(hourly) * 26
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 26
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 26
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 26
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 26
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 26
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 26
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 26
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 26
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 26
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 26
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 26
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 26
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 26
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Semi_Monthly":
                print("Semi_Monthly")

                D = 24
                M = semi_monthly
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 24
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 24
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 24
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 24
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 24
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 24
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 24
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 24
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 24
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 24
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 24
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 24
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 24
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 24
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Monthly":
                print("Monthly")

                D = 12
                M = month
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 12
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 12
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sui = sui / 12
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 12
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 12
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 12
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 12
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 12
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 12
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 12
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        sui = sui / 4
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 12
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 12
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 12
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 12
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Quartely":
                print("Quartely")

                D = 4
                M = quartely
                print("federal tax ==")
                print(fd)
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 4
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sui = sui / 4
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 4
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 4
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                        St = St / 4
                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 4
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 4
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 4
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        sui = sui / 4
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)

                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    fd = fd / 4
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    SS = SS / 4
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    mediC = mediC / 4
                    ytd_fd = fd * M

                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M

                    ytd_td = td * M

                    ytd_ss = SS * M

                    ytd_medic = mediC * M

                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 4
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Semi_Annually":
                print("Semi_Annually")
                D = 2
                M = semi_anuaaly
                print("federal tax ==")
                print(fd)
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 2
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sui = sui / 2
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 2
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 2
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                        St = St / 2
                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 2
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 2
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 2
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        sui = sui / 2
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)

                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    fd = fd / 2
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    SS = SS / 2
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    mediC = mediC / 2
                    ytd_fd = fd * M

                    ytd_st = St * M

                    ytd_wkc = wkc * M
                    ytd_sui = sui * M

                    ytd_td = td * M

                    ytd_ss = SS * M

                    ytd_medic = mediC * M

                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 2
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Annually":
                print("Annually")
                D = 1
                M = 1
                print("federal tax ==")
                print(fd)

                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)

                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    # fd = fd /2
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                if int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

        elif salary_type == "Hourly":
            print(salary_type)
            hours_worked = int(hours_worked)
            hourly_rate = int(hourly_rate)
            if weekly == "Once":
                hourly = hours_worked * hourly_rate * 1
                print("Once")
                D = 1
                M = 1
                print("federal tax ==")
                print(fd)

                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)

                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    # fd = fd /2
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Daily":
                hourly = hours_worked * hourly_rate * 360

                print('Daily')
                D = 360
                M = days
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 360
                print(pay_date)
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 360
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 360
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 360
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 360
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 360
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 360
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 360
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 360
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 360
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 360
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 360
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 360
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 360
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 360
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Weekly":
                hourly = hours_worked * hourly_rate * 52

                print("Weekly")
                D = 52
                M = week
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 52
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 52
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 52
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 52
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 52
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 52
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 52
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 52
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 52
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 52
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 52
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 52
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 52
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 52
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 52
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "BI_Weekly":
                print("BI_Weekly")
                hourly = hours_worked * hourly_rate * 26

                D = 26
                M = int(week) / 2
                print("federal tax ==")
                print(M)
                # hourly = int(hourly) * 26
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 26
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 26
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 26
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 26
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 26
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 26
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 26
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 26
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 26
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 26
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 26
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 26
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 26
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 26
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Semi_Monthly":
                print("Semi_Monthly")
                hourly = hours_worked * hourly_rate * 24

                D = 24
                M = semi_monthly
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 24
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 24
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380

                        sui = sui / 24
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 24
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 24
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 24
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 24
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 24
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 24
                        St = round(St, 2)
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = int(hourly) / 1428.5714

                        sui = sui / 24
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 24
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 24
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 24
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 24
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 24
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Monthly":
                print("Monthly")
                hourly = hours_worked * hourly_rate * 12

                D = 12
                M = month
                print("federal tax ==")
                print(fd)
                # hourly = int(hourly) * 12
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 12
                        St = round(St, 2)

                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sui = sui / 12
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 12
                        St = round(St, 2)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 12
                        sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 12
                        St = round(St, 2)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        St = St / 12
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 12
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 12
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 12
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 12
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        sui = sui / 4
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        St = St / 12
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = fd / 12
                    fd = round(fd, 2)
                    SS = int(hourly) / 16.129

                    SS = SS / 12
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655

                    mediC = mediC / 12
                    mediC = round(mediC, 2)

                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 12
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Quartely":
                print("Quartely")
                hourly = hours_worked * hourly_rate * 4

                D = 4
                M = quartely
                print("federal tax ==")
                print(fd)
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 4
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sui = sui / 4
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 4
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 4
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                        St = St / 4
                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 4
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 4
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 4
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        sui = sui / 4
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)

                        St = St / 4
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    fd = fd / 4
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    SS = SS / 4
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    mediC = mediC / 4
                    ytd_fd = fd * M

                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M

                    ytd_td = td * M

                    ytd_ss = SS * M

                    ytd_medic = mediC * M

                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 4
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui

                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Semi_Annually":
                hourly = hours_worked * hourly_rate * 2
                print("Semi_Annually")
                D = 2
                M = semi_anuaaly
                print("federal tax ==")
                print(fd)
                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        St = St / 2
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sui = sui / 2
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        St = St / 2
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        if 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sdi = sdi / 2
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        if 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        if 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        if 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        if 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        if 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        if 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        if 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        if 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        if 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        if 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0
                        St = St / 2
                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = St / 2
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = St / 2
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        St = St / 2
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        sui = sui / 2
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)

                        St = St / 2
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    fd = fd / 2
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    SS = SS / 2
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    mediC = mediC / 2
                    ytd_fd = fd * M

                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M

                    ytd_td = td * M

                    ytd_ss = SS * M

                    ytd_medic = mediC * M

                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    # current_total = current_total / 2
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    print(ytd_deduction)
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)
                elif int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

            elif weekly == "Annually":
                hourly = hours_worked * hourly_rate * 1

                print("Annually")
                D = 1
                M = 1
                print("federal tax ==")
                print(fd)

                pay_date_minus = pay_date - timedelta(days=362)
                if 20000 <= int(hourly) <= 100000:
                    if obj.state_name == "Alabama":
                        # if 20000 <= int(hourly) <= 200000:
                        #     St = int(hourly) / 25.3
                        #     St = round(St, 2)
                        # if int(hourly) > 200000:
                        #     St = int(hourly) / 28.7
                        #     St = round(St, 2)
                        St = state_tax(hourly, 24.3, 25.7, 25.1, 25.2, 25.27, 25.32, 25.35, 25.42)
                        print("lhr")
                        print(St)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Alaska":
                        St = 0
                        sui = int(hourly) / 175.4380
                        sui = round(sui, 2)
                        sdi = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arizona":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Arkansas":
                        St = state_tax(hourly, 33.11, 26, 22.36, 20.35, 19.16, 18.37, 17.81, 17.39)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "California":
                        St = state_tax(hourly, 86.5, 50, 34.22, 25.89, 21.02, 18.22, 16.54, 15.41)
                        if 20000 <= int(hourly) <= 50000:
                            sdi = int(hourly) / 111.111
                            sdi = round(sdi, 2)
                        elif 50000 < int(hourly) <= 55000:
                            sdi = int(hourly) / 112.66
                            sdi = round(sdi, 2)
                        elif 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 136.57
                            sdi = round(sdi, 2)
                        elif 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 166.22
                            sdi = round(sdi, 2)
                        elif 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 203.92
                            sdi = round(sdi, 2)
                        elif 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 253.49
                            sdi = round(sdi, 2)
                        elif 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 321.57
                            sdi = round(sdi, 2)
                        elif 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 420.91
                            sdi = round(sdi, 2)
                        elif 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 579.47
                            sdi = round(sdi, 2)
                        elif 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 872.64
                            sdi = round(sdi, 2)
                        elif 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1598.36
                            sdi = round(sdi, 2)
                        elif 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)

                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Colorado":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Connecticut":
                        St = state_tax(hourly, 55.55, 21.80, 17.28, 14.3, 11.99, 10.35, 9.23, 8.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Delaware":
                        St = state_tax(hourly, 37.36, 29.28, 25.71, 23.66, 22.72, 21.4, 20.41, 19.69)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Florida":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Georgia":
                        St = state_tax(hourly, 21.33, 19.75, 18.97, 18.5, 18.19, 17.97, 17.81, 17.68)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Hawaii":
                        St = state_tax(hourly, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42, 71.42)
                        if 20000 <= int(hourly) <= 55000:
                            sdi = int(hourly) / 200
                            sdi = round(sdi, 2)
                        elif 55000 < int(hourly) <= 60000:
                            sdi = int(hourly) / 217.80
                            sdi = round(sdi, 2)
                        elif 60000 < int(hourly) <= 65000:
                            sdi = int(hourly) / 261.50
                            sdi = round(sdi, 2)
                        elif 65000 < int(hourly) <= 70000:
                            sdi = int(hourly) / 315.42
                            sdi = round(sdi, 2)
                        elif 70000 < int(hourly) <= 75000:
                            sdi = int(hourly) / 383.59
                            sdi = round(sdi, 2)
                        elif 75000 < int(hourly) <= 80000:
                            sdi = int(hourly) / 472.56
                            sdi = round(sdi, 2)
                        elif 80000 < int(hourly) <= 85000:
                            sdi = int(hourly) / 593.52
                            sdi = round(sdi, 2)
                        elif 85000 < int(hourly) <= 90000:
                            sdi = int(hourly) / 767.54
                            sdi = round(sdi, 2)
                        elif 90000 < int(hourly) <= 95000:
                            sdi = int(hourly) / 1039.32
                            sdi = round(sdi, 2)
                        elif 95000 < int(hourly) <= 100000:
                            sdi = int(hourly) / 1523.43
                            sdi = round(sdi, 2)
                        elif 100000 < int(hourly):
                            sdi = 0
                            sdi = round(sdi, 2)
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "Idaho":
                        St = state_tax(hourly, 17.48, 16.12, 15.46, 15.06, 14.8, 14.61, 14.84, 14.37)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Illinois":
                        St = state_tax(hourly, 29.2, 28.43, 28.01, 27.76, 27.58, 27.46, 27.36, 27.29)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Indiana":
                        St = state_tax(hourly, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303, 30.303)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Lowa":
                        St = state_tax(hourly, 171.23, 167.46, 165.44, 20.14, 19.42, 336.57, 340, 341.72)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kansas":
                        St = state_tax(hourly, 34.38, 29.48, 27.32, 26.1, 25.32, 24.77, 24.37, 24.06)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Kentucky":
                        St = state_tax(hourly, 22.44, 20.66, 19.78, 19.27, 18.92, 18.68, 18.44, 18.23)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Louisiana":
                        St = state_tax(hourly, 34.48, 31.96, 30.71, 28.91, 27, 25.75, 24.87, 24.22)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maine":
                        St = state_tax(hourly, 23.32, 18.74, 16.9, 15.9, 15.28, 14.86, 14.54, 14.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Maryland":
                        St = state_tax(hourly, 13.97, 13.63, 13.45, 13.33, 13.26, 13.2, 13.16, 13.13)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Massachusetts":
                        St = state_tax(hourly, 21.02, 20.6, 20.32, 20.15, 20.03, 19.95, 19.88, 19.83)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Michigan":
                        St = state_tax(hourly, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294, 23.5294)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Minnesota":
                        St = state_tax(hourly, 20.59, 18.62, 17.41, 16.72, 16.27, 15.96, 15.72, 15.34)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Mississippi":
                        St = state_tax(hourly, 22.72, 21.87, 21.42, 21.15, 20.96, 20.83, 20.73, 20.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Missouri":
                        St = state_tax(hourly, 32.8, 27.13, 24.84, 22.88, 21.64, 20.81, 20.22, 19.77)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Montana":
                        St = state_tax(hourly, 27.23, 25.77, 25.02, 24.57, 24.27, 24.05, 23.88, 23.76)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nebraska":
                        St = state_tax(hourly, 36.44, 24.15, 21.34, 19.87, 18.86, 18.11, 17.58, 17.17)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Nevada":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Hampshire":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    elif obj.state_name == "New Jersey":
                        St = state_tax(hourly, 62.5, 58.33, 40.9, 32.16, 28.01, 25.59, 23.41, 21.93)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "New Mexico":
                        St = state_tax(hourly, 29.94, 26.47, 24.83, 23.89, 23.28, 22.85, 22.53, 22.29)
                        sdi = 0
                        sui = 0
                        wkc = 8.0
                        td = 0
                    elif obj.state_name == "New York":
                        St = state_tax(hourly, 31.52, 24.71, 21.83, 20.32, 19.39, 18.76, 18.31, 17.91)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Carolina":
                        St = state_tax(hourly, 24.85, 22.13, 20.87, 20.13, 19.66, 19.32, 19.07, 18.88)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "North Dakota":
                        St = state_tax(hourly, 99.2, 93.58, 83.64, 71.89, 65.52, 61.52, 58.58, 55.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Ohio":
                        St = state_tax(hourly, 48.44, 40.65, 36.46, 33.61, 31.89, 30.73, 29.61, 28.52)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oklahoma":
                        St = state_tax(hourly, 34.77, 28.13, 25.43, 23.97, 23.09, 22.42, 21.96, 21.62)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Oregon":
                        St = state_tax(hourly, 15.52, 14.57, 14.12, 13.95, 13.42, 13.06, 12.79, 12.59)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Pennsylvania":
                        St = state_tax(hourly, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732, 32.5732)
                        sdi = 0
                        sui = int(hourly) / 1428.5714
                        sui = round(sui, 2)
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Rhode Island":
                        St = state_tax(hourly, 26.68, 26.67, 26.67, 26.67, 26.18, 25.36, 24.76, 24.31)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 770.4
                    elif obj.state_name == "South Carolina":
                        St = state_tax(hourly, 17.24, 16.27, 15.78, 15.49, 15.29, 15.15, 15.04, 14.96)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "South Dakota":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0

                        td = 0
                    elif obj.state_name == "Tennessee":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Texas":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Utah":
                        St = state_tax(hourly, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Virginia":
                        St = state_tax(hourly, 24.82, 22.12, 20.86, 20.13, 19.65, 19.31, 19.07, 18.87)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Washington":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "West Virginia":
                        St = state_tax(hourly, 27.77, 25.92, 24, 22.22, 20.96, 20, 19.31, 18.81)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wisconsin":
                        St = state_tax(hourly, 19.65, 18.43, 17.81, 17.44, 17.19, 17.01, 16.88, 16.78)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Wyoming":
                        St = 0
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "Vermont":
                        St = state_tax(hourly, 31.52, 30.48, 26.88, 23.36, 21.42, 20.19, 19.34, 18.65)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0
                    elif obj.state_name == "District of Columbia":
                        St = state_tax(hourly, 25, 25, 25, 25, 25, 25, 25, 25)
                        sdi = 0
                        sui = 0
                        wkc = 0
                        td = 0

                    fd = federal_tax(hourly)
                    fd = round(fd, 2)
                    # fd = fd /2
                    SS = int(hourly) / 16.129
                    SS = round(SS, 2)
                    mediC = int(hourly) / 68.9655
                    mediC = round(mediC, 2)
                    ytd_fd = fd * M
                    ytd_st = St * M
                    ytd_sui = sui * M

                    ytd_wkc = wkc * M
                    ytd_td = td * M
                    ytd_ss = SS * M
                    ytd_medic = mediC * M
                    ytd_sdi = sdi * M

                    current_total = float(hourly) / D
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi + ytd_sui
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)

                    ytd_wkc = round(ytd_wkc, 2)
                    ytd_td = round(ytd_td, 2)
                    ytd_ss = round(ytd_ss, 2)
                    ytd_medic = round(ytd_medic, 2)
                    ytd_sdi = round(ytd_sdi, 2)
                    ytd_sui = round(ytd_sui, 2)
                    ytd_fd = round(ytd_fd, 2)
                    ytd_st = round(ytd_st, 2)
                    ytd_deduction = round(ytd_deduction, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi + sui
                    current_deduction = round(current_deduction, 2)
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)
                if int(hourly) > 100000 or int(hourly) < 20000:
                    St = 0
                    fd = 0
                    SS = 0
                    mediC = 0
                    ytd_fd = 0
                    ytd_st = 0
                    ytd_wkc = 0
                    ytd_td = 0
                    ytd_ss = 0
                    ytd_medic = 0
                    ytd_sdi = 0
                    current_total = 0
                    ytd_gross = current_total * M
                    ytd_deduction = ytd_fd + ytd_td + ytd_st + ytd_wkc + ytd_ss + ytd_medic + ytd_sdi
                    ytd_netpay = ytd_gross - ytd_deduction
                    ytd_netpay = round(ytd_netpay, 2)
                    # print(ytd_netpay)
                    ytd_deduction = round(ytd_deduction, 2)
                    current_total = round(current_total, 2)
                    ytd_gross = round(ytd_gross, 2)

                    current_deduction = fd + St + SS + wkc + mediC + td + sdi
                    net_pay = current_total - current_deduction
                    net_pay = round(net_pay, 2)

        print(company_ein_ssn_no)

        dic = {'state': state, 'emp_rad': emp_radio, 'emp_nam': emp_name, 'security': security,
               'company_name': company_name, 'company_address': company_address,
               'company_phone': company_phone, 'company_zip_code': company_zip_code, 'ein_ssn_no': ein_ssn_no,
               'ch_no_Choose': ch_no_Choose, "emp_id": emp_id, 'emp_sec_num': emp_sec_num, 'ytd_gross': ytd_gross,
               'ytd_deduction': ytd_deduction, 'pay_date_minus': pay_date_minus,
               'ytd_netpay': ytd_netpay, 'current_total': current_total, 'current_deduction': current_deduction,
               'net_pay': net_pay, 'company_ein_ssn_no': company_ein_ssn_no, 'fd': fd, 'sdi': sdi, 'St': St, 'SS': SS,
               'mediC': mediC, 'wkc': wkc, 'td': td, 'pay_date': pay_date, 'days_3_pay_date': days_3_pay_date,
               'ytd_td': ytd_td, 'ytd_st': ytd_st, 'ytd_fd': ytd_fd, 'ytd_ss': ytd_ss, 'ytd_sdi': ytd_sdi,
               'ytd_wkc': ytd_wkc, "salary_type": salary_type, 'sui': sui, "ytd_sui": ytd_sui,
               'ytd_medic': ytd_medic, 'hours_worked': hours_worked, 'hourly_rate': hourly_rate,'obj2':obj2,
                'form':form}
        # print(dic)

        return render(request, 'paystub_generator/generate_stub.html', dic)
    s = State.objects.all()

    return render(request, 'paystub_generator/create_your_stub.html', {'s': s})
