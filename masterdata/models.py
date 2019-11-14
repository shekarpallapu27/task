from django.db import models
from django.contrib.auth.models import Group, User
# Create your models here.


ACTIVE = ((0,'Inactive'), (2, 'Active'),)
BOOL_CHOICES = ((True,'Pass'), (False, 'Fail'),)

class Base(models.Model):
    
    """ Basic Fields """

    active = models.PositiveIntegerField(choices = ACTIVE, default=2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    def switch(self):
        self.active = {0: 2, 2: 0}[self.active]
        self.save()
        return self.active

    class Meta:
        abstract = True



class IdMapping(Base):
    """ 
        Id Mapping 
    """
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.student_name



class ReportDetails(Base):
    """
        Report Details


        # TotalMarks(%)     Grade Point

        # 91-100          10.0
        # 81-90           9.0
        # 71-80           8.0
        # 61-70           7.0
        # 51-60           6.0
        # 41-50           5.0
        # 33-40           4.0
        # 21-32           2.0

    """
    report_details_id = models.AutoField(primary_key=True)
    std = models.CharField(max_length=200,blank=True, null=True)
    Year = models.CharField(max_length=200,blank=True,null=True)
    Total = models.CharField(max_length=200,blank=True,null=True)
    Sci = models.CharField(max_length=200,blank=True,null=True)
    Math = models.CharField(max_length=200,blank=True,null=True)
    Language = models.CharField(max_length=200,blank=True,null=True)
    Social = models.CharField(max_length=200,blank=True,null=True)
    Grade = models.CharField(max_length=200,blank=True,null=True)
    student = models.ForeignKey(IdMapping,related_name='student_reportdetails')
    result_status = models.BooleanField(choices=BOOL_CHOICES)
    def __str__(self):
        return self.std

    # BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    # is_active = models.BooleanField(choices=BOOL_CHOICES,default=True)

class Login(Base):
    """ 
        Login details
    """
    username = models.CharField(max_length=200,blank=True, null=True)
    password = models.CharField(max_length=200,blank=True, null=True)
    allowed_ip = models.CharField(max_length=200,blank=True, null=True)
    user = models.OneToOneField(User,related_name='users',on_delete=models.PROTECT)
    def __str__(self):
        return self.username




#script for populating the 5 years data of 5 student

# import random
# student_data = ['amit','rahul','uday','shaker','mani']
# cls_year = [('Class_X','2019'),('Class_IX','2018'),('Class_IIX','2017'),('Class_VII','2016'),('Class_VI','2015')]

# for j in range(len(student_data)):
#     id_map = IdMapping.objects.create(student_name=student_data[j])
#     id_map.save()
#     for i in range(5):
#         sub_mrks=random.sample(range(20,101),4)
#         ttl = sum(sub_mrks)
#         per=(ttl*100)/400
#         grade = str(per)[0]
#         status = [True if res>35 else False for res in sub_mrks]
#         rd=ReportDetails(
#                         std = cls_year[i][0],
#                         Year = cls_year[i][1],
#                         Total = ttl,
#                         Sci = sub_mrks[0],
#                         Math = sub_mrks[1],
#                         Language = sub_mrks[2],
#                         Social = sub_mrks[3],
#                         Grade = grade,
#                         student = id_map,
#                         result_status = all(status)
#                         )
#         rd.save()


