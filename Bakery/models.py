from django.db import models

# Create your models here.
class Department(models.Model):
    '''
     Department Employee belongs to. eg. Transport, Engineering.
    '''
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=2000,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True)


    class Meta:
        verbose_name = ('Department')
        verbose_name_plural = ('Departments')
        ordering = ['name','created']

    def __str__(self):
        return self.name


# Create your models here.
class Catergory(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=2000,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True)


    class Meta:
        verbose_name = ('Catergory')
        verbose_name_plural = ('Categories')
        ordering = ['name','created']

    def __str__(self):
        return self.name
# -------------------------------- /Nationality --------------------------------------#

class Customer(models.Model):
# ------- Gender --------#
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    BUSINESS = 'Business'
    INSTITUTION = 'Institution'

    GENDER = (
    (MALE,'Male'),
    (FEMALE,'Female'),
    (OTHER,'Other'),
    (BUSINESS, 'Business'),
    (INSTITUTION, 'Institution'),
    )

# ------- Title --------#
    MR = 'Mr'
    MRS = 'Mrs'
    MSS = 'Mss'
    DR = 'Dr'
    SIR = 'Sir'
    MADAM = 'Madam'

    TITLE = (
    (MR,'Mr'),
    (MRS,'Mrs'),
    (MSS,'Mss'),
    (DR,'Dr'),
    (SIR,'Sir'),
    (MADAM,'Madam'),
    )

# ------- Employement Status --------#
    ACTIVE = 'Active'
    NON_ACTIVE = 'Non_Active'

    CLIENTSTATUS = (
    (ACTIVE,'Active'),
    (NON_ACTIVE,'Non_Active'),

    )


    # PERSONAL DATA
    #user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(('Title'),max_length=15,default=MR,choices=TITLE,blank=False,null=True)
    #image = models.FileField(('Profile Image'),upload_to='profiles',default='default.png',blank=True,null=True,help_text='upload image size less than 2.0MB')#work on path username-date/image
    fulltname = models.CharField(('Full Name'),max_length=125,null=False,blank=False)
    othername = models.CharField(('Othername (optional)'),max_length=125,null=True,blank=True)

    # Demographics
    gender = models.CharField(('Gender'),max_length=255,default=MALE,choices=GENDER,blank=False)
    quarter = models.CharField(('Current Quarter'),max_length=125,null=False,blank=False)
    address = models.TextField(('Address'),help_text='Address of Business Place',max_length=125,null=True,blank=True)

    # Contact
    tel = models.CharField( max_length=255, null = True, blank=True, verbose_name='Phone Number 1 ' )
    tel2 = models.CharField( max_length=255 ,null = True, blank=True, verbose_name='Phone Number 2 ')
    status = models.CharField(('Customer Status'),max_length=15,default=ACTIVE,choices=CLIENTSTATUS,blank=False,null=True)

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    class Meta:
        verbose_name = ('Customer')
        verbose_name_plural = ('Customers')
        ordering = ['-created']

class Suppliers(models.Model):
# ------- Gender --------#
    INDIVIDUAL= 'Individual'
    BUSINESS = 'Business'
    INSTITUTION = 'Institution'

    GENDER = (
    (INDIVIDUAL,'Individual'),
    (BUSINESS, 'Business'),
    (INSTITUTION, 'Institution'),
    )

# ------- Title --------#
    MR = 'Mr'
    MRS = 'Mrs'
    MSS = 'Mss'
    DR = 'Dr'
    SIR = 'Sir'
    MADAM = 'Madam'

    TITLE = (
    (MR,'Mr'),
    (MRS,'Mrs'),
    (MSS,'Mss'),
    (DR,'Dr'),
    (SIR,'Sir'),
    (MADAM,'Madam'),
    )

# ------- Employement Status --------#
    ACTIVE = 'Active'
    NON_ACTIVE = 'Non_Active'

    CLIENTSTATUS = (
    (ACTIVE,'Active'),
    (NON_ACTIVE,'Non_Active'),

    )


    # PERSONAL DATA
    #user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(('Title'),max_length=15,default=MR,choices=TITLE,blank=False,null=True)
    #image = models.FileField(('Profile Image'),upload_to='profiles',default='default.png',blank=True,null=True,help_text='upload image size less than 2.0MB')#work on path username-date/image
    fulltname = models.CharField(('Full Name'),max_length=125,null=False,blank=False)
    othername = models.CharField(('Othername (optional)'),max_length=125,null=True,blank=True)

    # Demographics
    gender = models.CharField(('Gender'),max_length=255,default=INDIVIDUAL,choices=GENDER,blank=False)
    quarter = models.CharField(('Current Quarter'),max_length=125,null=False,blank=False)
    address = models.TextField(('Address'),help_text='Address of Business Place',max_length=125,null=True,blank=True)

    # Contact
    tel = models.CharField( max_length=255, null = True, blank=True, verbose_name='Phone Number 1 ' )
    tel2 = models.CharField( max_length=255 ,null = True, blank=True, verbose_name='Phone Number 2 ')
    status = models.CharField(('Customer Status'),max_length=15,default=ACTIVE,choices=CLIENTSTATUS,blank=False,null=True)

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    class Meta:
        verbose_name = ('Supplier')
        verbose_name_plural = ('Suppliers')
        ordering = ['-created']


class Product(models.Model):
    name = models.CharField(('Full Name'),max_length=125,null=False,blank=False)
    category =  models.ForeignKey(Catergory,verbose_name =('Category'),on_delete=models.SET_NULL,null=True,default=None)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        ordering = ['-created']
