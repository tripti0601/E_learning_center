from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Question_Model

def home_view(request):
    NCERT_question = Question_Model.objects.filter(publication="NCERT")[:3]
    RD_question = Question_Model.objects.filter(publication="RD_Sharma_and_RS_Agrawal")[:3]
    return render(request, 'learn/Home.html', 
        {'class12' : NCERT_question,
         'rd_sharma' : RD_question,})

def  detail_view(request, question_id):
	try:
		question = Question_Model.objects.get(id=question_id)
	except Question_Model.DoesNotExist:
		raise Http404("Solution does not exist")
	return render(request, 'learn/details.html', {'question': question })

def search_view(request):
	if request.method == 'POST':
		result = Question_Model.objects.get(Question=request.POST.get('usr-input'))
		print(result)
		return render(request, 'learn/details.html', {'question': result})
	else:
	 	return redirect('home')


def like_view(request, question_id):
	print(question_id)
	try:
		question = Question_Model.objects.get(id=question_id)
		question.like += 1
		question.save()
		return reverse('detail-view', kwargs={'question_id':question_id})
	except Question_Model.DoesNotExist:
		raise Http404("Solution does not exist")
	finally:
		return redirect('home')




def publication_view(request, publication):
	question_list = Question_Model.objects.filter(publication=publication)
	return render(request, 'learn/Question_list.html',{'question_list' : question_list,})

def standard_view(request, std):
	print(std)
	question_list = Question_Model.objects.filter(std=std)[:]
	return render(request, 'learn/Question_list.html',{'question_list' : question_list,})



# Create your views here.
