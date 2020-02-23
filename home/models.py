from django.db import models
from datetime import datetime

class Contact(models.Model):
    con_id = models.AutoField(primary_key = True)
    date = models.DateField(default=datetime.now)
    name = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    organization = models.CharField(max_length=100,default="")
    message = models.CharField(max_length=2000,default="")

    def __str__(self):
        return '%d %s %s' % (self.con_id, self.name, self.date)

class Applying(models.Model):
    app_id = models.AutoField(primary_key = True)
    date = models.DateField(default=datetime.now)
    firstname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, default="")
    email = models.EmailField(max_length=50, default="")
    position = models.CharField(max_length=50, default="")
    linkedin = models.CharField(max_length=150, default="")
    github = models.CharField(max_length=150, default="")
    portfolio = models.CharField(max_length=150, default="")
    other = models.CharField(max_length=150, default="")
    twitter = models.CharField(max_length=150, default="")
    aspiration = models.CharField(max_length=500, default="")
    skills = models.CharField(max_length=500, default="")
    project = models.CharField(max_length=500, default="")
    techstack = models.CharField(max_length=500, default="")
    education = models.CharField(max_length=500, default="")
    availablity = models.CharField(max_length=500, default="")
    protfoliolink = models.CharField(max_length=500, default="")
    opensourcecommit = models.CharField(max_length=1000, default="")
    resume = models.CharField(max_length=1000, default="")
    def __str__(self):
        return '%d %s %s %s %s' % (self.app_id, self.firstname, self.lastname, self.date, self.position)

class AdminUpdate(models.Model):
    admin_id = models.AutoField(primary_key = True)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s' % (self.fullname, self.position)

class SelectIntern1(models.Model):
    app_id = models.IntegerField()
    task1name = models.CharField(max_length=500, default="")
    task1link = models.CharField(max_length=1000, default="")
    applicantEmail = models.CharField(max_length=100,default="")
    def __str__(self):
        return '%d %s' % (self.app_id, self.applicantEmail)
    
class SelectIntern2(models.Model):
    app_id = models.IntegerField()
    task2name = models.CharField(max_length=500, default="")
    task2link = models.CharField(max_length=1000, default="")
    applicantEmail = models.CharField(max_length=100,default="")
    def __str__(self):
        return '%d %s' % (self.app_id, self.applicantEmail) 
class SelectIntern3(models.Model):
    app_id = models.IntegerField()

    task3name = models.CharField(max_length=500, default="")
    task3link = models.CharField(max_length=1000, default="")
    applicantEmail = models.CharField(max_length=100,default="")
    def __str__(self):
        return '%d %s' % (self.app_id, self.applicantEmail)

    
class Solution1(models.Model):
    solution1 = models.CharField(max_length=500, default="")
    appid = models.CharField(max_length=10,default="")
    def __str__(self):
        return '%s' % (self.appid)

class Solution2(models.Model):
    solution2 = models.CharField(max_length=500, default="")
    appid = models.CharField(max_length=10,default="")
    def __str__(self):
        return '%s' % (self.appid)

class Solution3(models.Model):
    solution3 = models.CharField(max_length=500, default="")
    appid = models.CharField(max_length=10,default="")
    def __str__(self):
        return '%s' % (self.appid)


    
    
    
    
    
    
   	
   	
   	
   	
   	
   	


 