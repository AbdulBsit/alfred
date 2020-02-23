from django.urls import path
from . import views
urlpatterns = [
	path("",views.index, name="Home"),


	path("trilingo",views.trilingo, name="trilango"),
	path("tribalmatrimony",views.tribalmatrimony, name="tribalmatrimony"),
	path("toungestop",views.toungestop, name="toungestop"),
	path("mundaDhaba",views.mundaDhaba, name="mundaDhaba"),
	path("jharkhandmatrimony",views.jharkhandmatrimony, name="jharkhandmatrimony"),	

	path("services",views.services, name="services"),
	path("internship",views.internship, name="internship"),
	path("about",views.about, name="about"),
	path("philosophy",views.philosophy, name="philosophy"),
	path("portfolio",views.portfolio, name="portfolio"),
	path("contact",views.contact, name="contact"),
	path("research",views.research, name="research"),
	path("community",views.community, name="community"),

	path("team",views.team, name="team"),
	path("career",views.career, name="career"),

	path("apply",views.apply, name="apply"),
	
	path("adminupdate",views.adminupdate, name="adminupdate"),
	path("applicantlogin",views.applicantlogin, name="applicantlogin"),
	path("applicantlogin2",views.applicantlogin2, name="applicantlogin2"),
	path("applicantlogin3",views.applicantlogin3, name="applicantlogin3"),
	path("allinternsQ12rty3/<int:id>",views.allinterns, name="allintern"),
	path("internwork/<int:id>",views.internwork, name="internwork"),
	path("selectintern1Q12rty3",views.selectintern1, name="selectintern1"),
	path("selectintern2Q12rty3",views.selectintern2, name="selectintern2"),
	path("selectintern3Q12rty3",views.selectintern3, name="selectintern3"),


	path("solution1",views.solution1, name="solution1"),
	path("solution2",views.solution2, name="solution2"),
	path("solution3",views.solution3, name="solution3"),

	path("viewsolutionQ12rty3",views.viewsolution, name="viewsolution"),
	path("viewsolution2Q12rty3",views.viewsolution2, name="viewsolution2"),
	path("viewsolution3Q12rty3",views.viewsolution3, name="viewsolution3"),
	
]
