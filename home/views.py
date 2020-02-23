from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Contact, Applying, AdminUpdate, SelectIntern1, SelectIntern2, SelectIntern3, Solution1, Solution2, Solution3

def index(request):
	return render(request, 'home/index.html')

###################################################################

def trilingo(request):
	return render(request, 'home/trilingo.html')

def tribalmatrimony(request):
	return render(request, 'home/tribalmatrimony.html')

def toungestop(request):
	return render(request, 'home/toungestop.html')

def mundaDhaba(request):
	return render(request, 'home/mundaDhaba.html')

def jharkhandmatrimony(request):
	return render(request, 'home/jharkhandmatrimony.html')

####################################################################


def services(request):
	return render(request, 'home/services.html')

def internship(request):
	return render(request, 'home/internship.html')

def about(request):
	return render(request, 'home/about.html')

def philosophy(request):
	return render(request, 'home/philosophy.html')

def portfolio(request):
	return render(request, 'home/portfolio.html')

def contact(request):
	if request.method == "POST":
		name= request.POST.get('name','')		
		phone= request.POST.get('phone','')		
		email= request.POST.get('email','')	
		organization = request.POST.get('organization','')	
		message= request.POST.get('message','')		
		contact=Contact(name=name, phone=phone, email=email, organization=organization,message=message)
		contact.save()
		done = True
		return render(request, 'home/contact.html', {'done':done})
	return render(request, 'home/contact.html')

def research(request):
	return render(request, 'home/research.html')

def community(request):
	return render(request, 'home/community.html')

###################################################################

def team(request):
	return render(request, 'home/team.html')

def career(request):
	return render(request, 'home/career.html')


####################################################################


def apply(request):
	if request.method=="POST":
		firstname= request.POST.get('firstname','')		
		lastname= request.POST.get('lastname','')		
		phone= request.POST.get('phone','')		
		email= request.POST.get('email','')	
		position = request.POST.get('position','')	
		linkedin= request.POST.get('linkedin','')		
		github= request.POST.get('github','')		
		portfolio= request.POST.get('portfolio','')		
		other= request.POST.get('other','')		
		twitter= request.POST.get('twitter','')		
		aspiration= request.POST.get('aspiration','')		
		skills= request.POST.get('skills','')		
		project= request.POST.get('project','')		
		techstack= request.POST.get('techstack','')		
		education= request.POST.get('education','')		
		availablity= request.POST.get('availablity','')			
		protfoliolink=request.POST.get('protfoliolink','')
		opensourcecommit=request.POST.get('opensourcecommit','')
		resume=request.POST.get('resume','')
		applying=Applying(firstname=firstname, lastname=lastname, phone=phone, email=email,position=position ,linkedin=linkedin, github=github, portfolio=portfolio, other=other, twitter=twitter, aspiration=aspiration, skills=skills,project=project, techstack=techstack, education=education, availablity=availablity, protfoliolink=protfoliolink, opensourcecommit=opensourcecommit, resume=resume)
		applying.save()

		done=True
		return render(request, 'home/apply.html', {'done':done},)
	return render(request, 'home/apply.html')


#################################################################

def adminupdate(request):
	if request.method == "POST":
		email_entered = request.POST.get('email')
		phone_entered = request.POST.get('phone')
		admin = AdminUpdate.objects.filter(email=email_entered, phone=phone_entered)
		if len(admin)>0:
			interns = Applying.objects.all()
			n = len(interns)
			nSlides = n//4 + ceil((n/4) + (n//4))
			params = {'no_of_slides':nSlides,'range':range(1,nSlides), 'interns': interns}
			
			return render(request, 'home/adminupdate.html',params)
		else:
			#print('nO')
			messages = {'Hello'}
			return render(request, 'home/adminupdate.html', {'messages':messages})
	return render(request, 'home/adminupdate.html')

def allinterns(request, id):
	interns = Applying.objects.filter(app_id = id)[0]
	print(interns)
	return render(request, 'home/allinterns.html',{'interns':interns})

def selectintern1(request):


	if request.method =="POST":
		app_id = request.POST.get('app_id')
		task1name = request.POST.get('task1name')
		task1link = request.POST.get('task1link')
		applicantEmail = request.POST.get('applicantEmail')

		selectintern1=SelectIntern1(app_id=app_id, task1name=task1name,task1link=task1link, applicantEmail=applicantEmail)
		selectintern1.save()
		return render(request, 'home/selectintern1.html')
	return render(request, 'home/selectintern1.html')

def selectintern2(request):
	if request.method =="POST":
		app_id = request.POST.get('app_id')

		task2name = request.POST.get('task2name')
		task2link = request.POST.get('task2link')
		applicantEmail = request.POST.get('applicantEmail')

		selectintern2=SelectIntern2(app_id=app_id,task2name=task2name,task2link=task2link,applicantEmail=applicantEmail )
		selectintern2.save()
		return render(request, 'home/selectintern2.html')
	return render(request, 'home/selectintern2.html')

def selectintern3(request):
	if request.method =="POST":
		app_id = request.POST.get('app_id')

		task3name = request.POST.get('task3name','')
		task3link = request.POST.get('task3link','')
		applicantEmail = request.POST.get('applicantEmail','')

		selectintern3=SelectIntern3(app_id=app_id,task3name=task3name,task3link=task3link,applicantEmail=applicantEmail)
		selectintern3.save()
		return render(request, 'home/selectintern3.html')
	return render(request, 'home/selectintern3.html')

def applicantlogin(request):
	if request.method == "POST":
		email_entered = request.POST.get('email')
		phone_entered = request.POST.get('phone')
		match = Applying.objects.filter(email=email_entered, phone=phone_entered)
		if len(match)>0:
			#print('yes')
			check = SelectIntern1.objects.filter(applicantEmail=email_entered)
			if len(check)>0:
				All = SelectIntern1.objects.filter(applicantEmail=email_entered).values('app_id','applicantEmail', 'task1name', 'task1link')
				#print(All)

				return render(request, 'home/applicantlogin.html', {'All':All})
			else:
				msgs = {'Hello'}
				return render(request, 'home/applicantlogin.html', {'msgs':msgs})
	
		
		else:
			#print('nO')
			messages = {'Hello'}
			return render(request, 'home/applicantlogin.html', {'messages':messages})

	return render(request, 'home/applicantlogin.html')


def applicantlogin2(request):
	if request.method == "POST":
		email_entered = request.POST.get('email')
		phone_entered = request.POST.get('phone')
		match = Applying.objects.filter(email=email_entered, phone=phone_entered)
		if len(match)>0:
			#print('yes')
			check = SelectIntern2.objects.filter(applicantEmail=email_entered)
			if len(check)>0:
				All2 = SelectIntern2.objects.filter(applicantEmail=email_entered).values('app_id','applicantEmail', 'task2name', 'task2link')
				
				#print(All2)

				return render(request, 'home/applicantlogin2.html', {'All2':All2})
				
		else:
			#print('nO')
			messages = {'Hello'}
			return render(request, 'home/applicantlogin2.html', {'messages':messages})

	return render(request, 'home/applicantlogin2.html')

def applicantlogin3(request):
	if request.method == "POST":
		email_entered = request.POST.get('email')
		phone_entered = request.POST.get('phone')
		match = Applying.objects.filter(email=email_entered, phone=phone_entered)
		if len(match)>0:
			#print('yes')
			check = SelectIntern3.objects.filter(applicantEmail=email_entered)
			if len(check)>0:
				All3 = SelectIntern3.objects.filter(applicantEmail=email_entered).values('app_id','applicantEmail', 'task3name', 'task3link')
				
				#print(All3)

				return render(request, 'home/applicantlogin3.html', {'All3':All3})
		
		else:
			#print('nO')
			messages = {'Hello'}
			return render(request, 'home/applicantlogin3.html', {'messages':messages})

	return render(request, 'home/applicantlogin3.html')


def internwork(request, id):
	interns = selectintern1.objects.filter(app_id = id)[0]
	print(interns)
	return render(request, 'home/internwork.html',{'interns':interns})


def solution1(request):
	if request.method =="POST":
		solution1 = request.POST.get('solution1','')
		appid = request.POST.get('appid','')

		Sol1=Solution1(solution1=solution1, appid=appid)
		Sol1.save()
		#print(Sol1)
		done = True
		return render(request, 'home/solution1.html', {'done':done},)
	return render(request,'home/solution1.html')


def solution2(request):
	if request.method =="POST":
		solution2 = request.POST.get('solution2','')
		appid = request.POST.get('appid','')

		Sol2=Solution2(solution2=solution2, appid=appid)
		Sol2.save()
		#print(Sol2)
		done = True
		return render(request, 'home/solution2.html', {'done':done},)
	return render(request,'home/solution2.html')


def solution3(request):
	if request.method =="POST":
		solution3 = request.POST.get('solution3','')
		appid = request.POST.get('appid','')

		Sol3=Solution3(solution3=solution3, appid=appid)
		Sol3.save()
		#print(Sol3)
		done = True
		return render(request, 'home/solution3.html', {'done':done},)
	return render(request,'home/solution3.html')


def viewsolution(request):
	if request.method =="POST":
		app_id_entered=request.POST.get('app_id','')
		check = Solution1.objects.filter(appid=app_id_entered)
		if len(check)>0:
			#print('yes')
			All = Solution1.objects.filter(appid=app_id_entered).values('appid','solution1')
				
			#print(All)

			return render(request, 'home/viewsolution.html', {'All':All})
		
		else:
			#print('nO')
			messages = {'Hello'}
			return render(request, 'home/viewsolution.html', {'messages':messages})


	return render(request,'home/viewsolution.html')

def viewsolution2(request):
	if request.method =="POST":
		app_id_entered=request.POST.get('app_id','')
		check = Solution2.objects.filter(appid=app_id_entered)
		if len(check)>0:
			#print('yes')
			All = Solution2.objects.filter(appid=app_id_entered).values('appid','solution2')
				
			#print(All)

			return render(request, 'home/viewsolution2.html', {'All':All})
		
		else:
			#print('nO')
			messages = {'Hello'}
			return render(request, 'home/viewsolution2.html', {'messages':messages})


	return render(request,'home/viewsolution2.html')

def viewsolution3(request):
	if request.method =="POST":
		app_id_entered=request.POST.get('app_id','')
		check = Solution3.objects.filter(appid=app_id_entered)
		if len(check)>0:
			#print('yes')
			All = Solution3.objects.filter(appid=app_id_entered).values('appid','solution3')
				
			#print(All)

			return render(request, 'home/viewsolution3.html', {'All':All})
		
		else:
			#print('nO')
			messages = {'Hello'}
			return render(request, 'home/viewsolution3.html', {'messages':messages})


	return render(request,'home/viewsolution3.html')

##########################################################
