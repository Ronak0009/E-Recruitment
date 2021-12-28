from django.db.models.deletion import CASCADE
from django.http import request
from employee.models import candidate, graduation
from django.db import models
from employee.models import candidate
from .validators import validate_file_extension,validate_excel_file_extension
from datetime import datetime

# Create your models here.


class company(models.Model):
    account_id = models.CharField(max_length=20,
                verbose_name="Account Id",default='',primary_key=True)
    
    company_name = models.CharField(max_length=100,
                verbose_name="Company Name")

    email = models.EmailField(max_length=70,
                    verbose_name="Email")
    
    mobile = models.CharField(max_length=10,
               verbose_name="Mobile Number")
    
    password = models.CharField(max_length=70,
                    verbose_name="Password")
    
class Job(models.Model):
    uni_choices=(('Ganpat University','Ganpat University'),('Other','Other'))
    test_choices = (('Aptitude Test', 'Aptitude Test'),
                    ('None','None'))
    interview_choices = (('Online Interview', 'Online Interview'),
                    ('None','None'))
    job_id = models.CharField(max_length=20,
                verbose_name="Job ID",primary_key=True)
                
    company = models.ForeignKey(company, on_delete=models.CASCADE)

    job_title = models.CharField(max_length=100,
                verbose_name="Job Title")

    job_description = models.TextField(max_length=1000,
                            verbose_name='About',
                            default = '',
                            blank=True)

    salary = models.FloatField(verbose_name="Minimum Salary")
    
    maxSalary = models.FloatField(verbose_name="Maximum Salary", blank=True, null=True)

    is_active = models.BooleanField(verbose_name='Active', default=True)

    position = models.CharField(max_length=100,
                verbose_name="Position")
    
    experience_required = models.IntegerField(verbose_name='Experience Required', default=0)
    
    vacancies = models.IntegerField(verbose_name='Vacancies')

    ssc = models.FloatField(verbose_name="SSC Percentage",null=True,blank=True)

    hsc = models.FloatField(verbose_name="HSC Percentage", null=True,blank=True)

    graduation_cgpa = models.FloatField(verbose_name="Graduation CGPA", null=True,blank=True)

    aptitude_test = models.CharField(verbose_name="Aptitude Test", choices=test_choices, max_length=50, default=('None','None'))

    video_chat = models.CharField(verbose_name="Video Chat", choices=interview_choices, max_length=50)

    location = models.CharField(max_length=100,blank=True,null=True,
                verbose_name="Location")

    university = models.CharField(max_length=50,
                    verbose_name="University",
                    choices=uni_choices)

    year = models.CharField(max_length=50,blank=True,
                    verbose_name="Passing Year",)
    campus_date = models.DateField(blank=True,default='',null=True,
                    verbose_name="Campus Date")

class Company_profile(models.Model):
    email = models.EmailField(max_length=70,
                    verbose_name="Email")
               
    companyLink= models.CharField(max_length=70,
                     default='',
                    verbose_name="Company Link")

    company = models.ForeignKey(company, on_delete=models.CASCADE)

    about = models.TextField(max_length=300,
                            verbose_name='About',
                            default = '',
                            blank=True)
                    
    image = models.ImageField(verbose_name="Profile Picture", upload_to='company_profile_pics', blank=True, null=True)


class job_application(models.Model):
    job= models.ForeignKey(Job, on_delete=models.CASCADE)

    company = models.ForeignKey(company, on_delete=models.CASCADE)

    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)

    resume_file = models.FileField(verbose_name="Resume",upload_to='resume_files', validators=[validate_file_extension])

    application_time = models.DateTimeField(verbose_name="Application Time",default=datetime.now)


class Test_Schedule(models.Model):
    uni_choices=(('Ganpat University','Ganpat University'),('Other','Other'))
    job= models.ForeignKey(Job, on_delete=models.CASCADE)

    test_date= models.DateField(verbose_name="Test Time",default=datetime.now)
    test_time =  models.TimeField(verbose_name="Test Time")

    university = models.CharField(max_length=50,
                    verbose_name="University",
                    choices=uni_choices)

    # test_link = models.CharField(verbose_name="Test Link", max_length=200)

class quiz(models.Model):
    job= models.ForeignKey(Job, on_delete=models.CASCADE)

    company = models.ForeignKey(company, on_delete=models.CASCADE)

    schedule =models.ForeignKey(Test_Schedule,on_delete=models.CASCADE)
    
    number_of_questions = models.IntegerField(default=1)


    name = models.CharField(max_length=50)

    time = models.IntegerField(help_text="Duration of the quiz in minutes", default="1")

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()

class Questions(models.Model):
    quiz = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question_num= models.CharField(max_length=20,
                verbose_name="question Id",default='')
    question = models.CharField(verbose_name="Question",max_length=1000)

class Option(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"question: {self.question.question}, answer: {self.content}, correct: {self.correct}"


class Marks_Of_Candidate(models.Model):
    quiz = models.ForeignKey(quiz, on_delete=models.CASCADE)
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.quiz)

class online_schedule(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)

    candidate_sheet = models.FileField(verbose_name="Candidate Sheet", upload_to='candidate_sheet', validators=[validate_excel_file_extension])


class selected_candidates(models.Model):

    job = models.ForeignKey(Job,on_delete=models.CASCADE)

    selected_sheet = models.FileField(verbose_name="Selected Sheet", upload_to='selected_sheet', validators=[validate_excel_file_extension])













