from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Board


# Create your views here.
def home(request):
	boards = Board.objects.all()
	'''board_list = list()

	for board in board:
		board_list.append(board.name)

	response_html = '<br>'.join(board_list)

	return HttpResponse(response_html)'''
	return render(request, 'home.html',{'boards' : boards})


	