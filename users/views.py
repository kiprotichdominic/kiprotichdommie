# from django.views.generic import CreateView, TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render, redirect 
# from django.http import HttpResponse
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.contrib.auth import authenticate, login, logout

# from django.contrib import messages
# from .decorators import unauthenticated_user


# @unauthenticated_user
# def loginPage(request):
# 	if request.method == 'POST':
# 		email = request.POST.get('email')
# 		password =request.POST.get('password')
# 		user = authenticate(request, email=email, password=password)
# 		if user is not None:
# 			login(request, user)
# 			return redirect('dashboard')
# 		else:	
# 		    messages.info(request, 'Email OR password is incorrect')	
# 	context = {}
# 	return render(request, 'account/login.html', context)	

# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')

# class ProfilePageView(LoginRequiredMixin ,TemplateView):
#     template_name = 'users/profile.html'