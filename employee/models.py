from django.db import models
from .validators import validate_file_extension

# Create your models here.

class candidate(models.Model):
    uni_choices=(('Ganpat University','Ganpat University'),('Other','Other'))

    firstName = models.CharField(max_length=70,
                     default='',
                    verbose_name="First Name")

    lastName = models.CharField(max_length=70,
                    default='',
                    verbose_name="Last Name")
            
    account_id = models.CharField(max_length=20,
                verbose_name="Account Id",default='',primary_key=True)

    email = models.EmailField(max_length=70,
                    verbose_name="Email")
    
    mobile = models.CharField(max_length=10,
               verbose_name="Mobile Number")
    
    password = models.CharField(max_length=70,
                    verbose_name="Password")
    university = models.CharField(max_length=50,
                    verbose_name="University",
                    choices=uni_choices)

class Candidate_profile(models.Model):
    gender_choices=(('M','Male'),('F','Female'),('O','Other'),)


    designation_choices=(('Fresher','Fresher'),
                    ('Developer','Developer'),
                    ('Consultant','Consultant'),
                    ('Analyst','Analyst'),
                    ('Manager','Manager'))
               
    # categories = (('Fresher','Fresher'),
    #             ('Developer(More than 5 years)','Developer(More than 5 years'),
    #             ('Developer(Less than 5 years)','Developer(Less than 5 years'),
    #             ('Consultant(More than 5 years)','Consultant(More than 5 years'),
    #             ('Consultant(Less than 5 years)','Consultant(Less than 5 years'),
    #             ('Analyst(More than 5 years)','Analyst(More than 5 years'),
    #             ('Analyst(Less than 5 years)','Analyst(Less than 5 years'),
    #             ('Manager(More than 5 years)','Manager(More than 5 years'),
    #             ('Manager(Less than 5 years)','Manager(Less than 5 years'))
               

    firstName = models.CharField(max_length=70,
                     default='',
                    verbose_name="First Name")

    middleName = models.CharField(max_length=70,
                    default='',
                    verbose_name="Middle Name",
                    blank=True)

    lastName = models.CharField(max_length=70,
                    default='',
                    verbose_name="Last Name")

    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)

    date = models.DateField(max_length=70,
                    verbose_name="Date of Birth")
     
    gender = models.CharField(max_length=7,
                    verbose_name="Gender",
                    choices=gender_choices)

    designation = models.CharField(max_length=20,
                    verbose_name="Designation",
                    choices=designation_choices)

    # category = models.CharField(max_length=70,
    #                 verbose_name="Category",
    #                 choices=categories,
    #                 )

    about = models.TextField(max_length=300,
                            verbose_name='About',
                            default = '',
                            blank=True)
                    
    image = models.ImageField(verbose_name="Profile Picture", upload_to='profile_pics', blank=True, null=True)

class ssc(models.Model):
    # account_id = models.CharField(max_length=20,
    #                 verbose_name="Account Id", default='', primary_key=True)

    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)

    startyear = models.CharField(max_length=4,
                    verbose_name="Starting Year")

    passyear = models.CharField(max_length=4,
                    verbose_name="Passing Year")

    instituteName = models.CharField(max_length=70,
                     default='',
                    verbose_name="Institute Name")

    marks = models.CharField(max_length=10,
                        default='',
                        verbose_name="Marks")
    ssc_marksheet = models.FileField(verbose_name="SSC Marksheet", blank=True, upload_to='ssc_result', validators=[validate_file_extension])


class hsc(models.Model):
    category_choices = (('Science','Science'),
                ('Diploma','Diploma'),
                ('Commerce','Commerce'),
                ('Arts','Arts'))
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    # account_id = models.CharField(max_length=20,
    #                 verbose_name="Account Id", default='', primary_key=True)
    category = models.CharField(max_length=70,
                    verbose_name="Category",
                    default='Science',
                    choices=category_choices)
    startyear = models.CharField(max_length=4,
                    verbose_name="Starting Year")
    passyear = models.CharField(max_length=4,
                    verbose_name="Passing Year")
    instituteName = models.CharField(max_length=70,
                     default='',
                    verbose_name="Institute Name")
    marks = models.CharField(max_length=50,
                        default='',
                        verbose_name="Marks")
    hsc_marksheet = models.FileField(verbose_name="HSC Marksheet", blank=True, upload_to='hsc_result', validators=[validate_file_extension])


class graduation(models.Model):
    category_choices = (('Post Graduate','Post Graduate'),
                ('Under Graduate','Under Graduate'),  
                ('MCA','MCA'),
                ('BCA','BCA'),      
                ('MSC','MSC'),
                ('BSC','BSC'),
                ('M.Com','M.Com'),
                ('B.Com','B.Com'),
                ('Other','Other'))
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    # account_id = models.CharField(max_length=20,
    #                 verbose_name="Account Id", default='', primary_key=True)
    category = models.CharField(max_length=70,
                    verbose_name="Category",
                    default='Science',
                    choices=category_choices)
    startyear = models.CharField(max_length=4,
                    verbose_name="Starting Year")
    passyear = models.CharField(max_length=4,
                    verbose_name="Paasing Year")
    instituteName = models.CharField(max_length=70,
                     default='',
                    verbose_name="Institute Name")
    marks = models.CharField(max_length=50,
                        default='',
                        verbose_name="Marks")
    graduation_marksheet = models.FileField(verbose_name="Graduation Marksheet", blank=True, upload_to='graduation_result', validators=[validate_file_extension])

    
class experience(models.Model):
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    # account_id = models.CharField(max_length=20,
    #                 verbose_name="Account Id", default='', primary_key=True)
    companyName = models.CharField(max_length=70,
                     default='',
                    verbose_name="Company Name")
    startyear = models.CharField(max_length=4,
                    verbose_name="Starting Year")
    endyear = models.CharField(max_length=4,
                    verbose_name="End Year")
    role= models.CharField(max_length=70,
                     default='',
                    verbose_name="Your Role")
    about = models.TextField(max_length=300,
                            verbose_name='Description',
                            default = '',
                            blank=True)
    ctc = models.CharField(max_length=50,
                        default='',
                        verbose_name="CTC")
    experience_file = models.FileField(verbose_name="Experience File", blank=True, upload_to='experience', validators=[validate_file_extension])




class social(models.Model):
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    # account_id = models.CharField(max_length=20,
    #                 verbose_name="Account Id", default='', primary_key=True)
    city = models.CharField(max_length=70,
                    default='',
                    verbose_name="city")

    linkedin = models.CharField(max_length=70,
                    default='',
                    verbose_name="linkedin")
    
    github = models.CharField(max_length=70,
                    default='',
                    verbose_name="github")
   