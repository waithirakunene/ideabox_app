from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(ListView, 
								DetailView,
								CreateView,
								UpdateView,
								DeleteView
								) 
from .models import Ideas


# Create your views here.
class IdeaListView(ListView):
	model = Ideas
	template_name = 'ideabox/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'ideabox'
	ordering = ['-date_posted']


class IdeaDetailView(DetailView):
	model = Ideas

class IdeaCreateView(LoginRequiredMixin, CreateView):
	model = Ideas
	fields = ['title', 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class IdeaUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Ideas
	fields = ['title', 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class IdeaDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Ideas
	success_url = '/'
	


	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False







def about(request):
	return render(request, 'ideabox/about.html')

#from django.http import HttpResponse




	