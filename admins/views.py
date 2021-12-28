from django.shortcuts import render
from company.forms import *
from company.models import *
from employee.models import *
from employee.forms import *
# Create your views here.
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def admin_home_view(request,*args):
    return render(request,"admins/home.html")

def admin_candidates_view(request,*args):
    data= Candidate_profile.objects.all()
    print(data)
    context = {
        'data':data,
    }
    # sscd =  ssc.objects.all()
    # print(sscd)
    context['ssc_data'] = ssc.objects.all()
    context['hsc_data'] = hsc.objects.all()
    context['graduation_data'] = graduation.objects.all()
    context['exp_data'] = experience.objects.all()
    # for i in data:
    #     print(i.candidate)
    #     print(ssc.objects.filter(candidate=i.candidate))
    #     context[i.candidate]= ssc.objects.filter(candidate=i.candidate)
    # print(context)
    
    
    
    
    return render(request,"admins/candidates.html",context)

# def export_excel_view(request,job_id,*args):
#     data= Candidate_profile.objects.all()

    
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename={date}-Applicants.xlsx'.format(
#         date=datetime.now().strftime('%d-%m-%Y'),
#     )
#     workbook = Workbook()
    
#     # Get active worksheet/tab
#     worksheet = workbook.active
#     worksheet.title = 'Applications'

#     # Define the titles for columns
#     columns = [
#         'Job',
#         'Position',
#         'Experience',
#         'Name',
#         'Email',
#         'Mobile',
#     ]
#     row_num = 1

#     # Assign the titles for each cell of the header
#     for col_num, column_title in enumerate(columns, 1):
#         cell = worksheet.cell(row=row_num, column=col_num)
#         cell.value = column_title

#     # Iterate through all movies
#     for i in data:
#         print('titlle',i.job.job_title)
#         row_num += 1
        
#         # Define the data for each cell in the row 
#         row = [
#             i.job.job_title,
#             i.job.position,
#             i.job.experience_required,
#             i.candidate.firstName + ' ' + i.candidate.lastName,
#             i.candidate.email,
#             i.candidate.mobile,
#         ]
        
#         # Assign the data for each cell of the row 
#         for col_num, cell_value in enumerate(row, 1):
#             cell = worksheet.cell(row=row_num, column=col_num)
#             cell.value = cell_value

#     workbook.save(response)

#     res=response
#     print(res)
#     return response



def admin_companies_view(request,*args):
    data= company.objects.all()
    context={
        'data':data
    }
    return render(request,"admins/companies.html",context)

def admins_companies_jobs_view(request,account_id,*args):
    comp = company.objects.filter(account_id=account_id)
    print(comp)
    data = job_application.objects.filter(company=comp[0])
    if data:
        selected_data_sheet = selected_candidates.objects.filter(job=data[0].job)
    else:
        selected_data_sheet = 'empty'
    select_data={}
    for i in data:
        print(i.job)
        print(i.job.job_title)
        select_data[i.job.job_title] = selected_candidates.objects.filter(job=i.job)
    print(select_data)
    context={
        'data':data,
        'selected_data_sheet':selected_data_sheet[0],
        'selected_data':select_data,
    }
    return render(request,'admins/companies_job.html',context)

def admins_applications_view(request,job_id,account_id,*args):
    comp = company.objects.filter(account_id=account_id)
    jobobj = Job.objects.filter(company=comp[0])
    data = job_application.objects.filter(job=jobobj[0],company=comp[0])
    print(data)
    context = {
        'data':data,
    }
    return render(request,"admins/admins_applications.html",context)