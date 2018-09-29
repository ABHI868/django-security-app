from django.shortcuts import render,get_object_or_404
from .models import Visitors,Public
from .forms import Visitors_form_1,maintenance_modelform,PublicModelform
from django.views.generic import CreateView,UpdateView,DeleteView

def home(request):
    all_visitors=Visitors.objects.all()
    return render(request,'Sangaria/home.html',{'all_visitors':all_visitors})

def form(request):
    return render(request,'Sangaria/form.html')

def submit(request):
	all_records=Visitors.objects.all()
	print(all_records)
	return render(request,'Sangaria/submit.html',{'all_records':all_records})
'''
def Visitors_detail_view(request):
	form=Visitors_form()
	if form.request==POST:
		if form.is_valid():
			form.save()
	context={ "form_data":form}
	return render(request,'Sangaria/form_data_view.html',context)


'''
def maintenance_modelform_view(request):
	print("Hi")
	myform=maintenance_modelform()	
	print(myform)
	

	context={"form_data":myform}
	return render(request,"Sangaria/maintenance_model.html",context)

def Visitors_detail_view1(request):	

	myform=Visitors_form_1()
	name="Abhishek"
	context={ "form_data":myform}
	#print(context)
	return render(request,'Sangaria/form_data_view1.html',context)

class createviewpublic(CreateView):
	form_class=PublicModelform
	template_name="Sangaria/createviewtemplate.html"
	queryset=Public.objects.all()

class updateviewpublic(UpdateView):
	form_class=PublicModelform
	template_name="Sangaria/updateviewtemplate.html"
	queryset=Public.objects.all()

	def get_object(self):
		id_=self.kwargs.get("id")
		return get_object_or_404(Public,id=id_)


