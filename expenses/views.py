# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models.functions import Lower


# Create your views here.
from django.shortcuts import render, get_object_or_404
from expenses.forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from expenses.forms import ExpenseUploadForm
from expenses.models import Product
from django.shortcuts import redirect
from django.views.generic import ListView
from django.db.models import Q




def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #user_form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            registered = True
        else:
            print("Errors are")
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request,'registration.html',
                          {'form':form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                #return redirect('add')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    #return redirect('index')
                    #return render(request, 'home.html', {})

                    return HttpResponseRedirect(reverse('expenses:home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

@login_required
def home(request):
    query_results = Product.objects.all()
    total = 0
    for prod in query_results:
        total+=prod.price
    context={
            "query_results" : query_results,
            "total_expenses":total
        }
    return render(request,'home.html',context)

@login_required
def add(request):
    if request.method == 'POST':
        expense_form = ExpenseUploadForm(request.POST,request.FILES)
        #user_form = UserForm(data=request.POST)
        if expense_form.is_valid():
            expense_form.save()
            #p= Product.object.get(pk=item_id)
            item = expense_form.cleaned_data.get('item')
            price = expense_form.cleaned_data.get('price')
            #image = expense_form.cleaned_data.get('image')
            #p.save()

            return HttpResponseRedirect(reverse('expenses:viewlist'))
        
    else:
        form = ExpenseUploadForm()
    return render(request,'add.html',
                          {'ExpenseUploadForm':ExpenseUploadForm})

@login_required
def viewlist(request):
    query=request.GET.get("q")
    order_column=request.GET.get("o") or "p_k"
    query_results = Product.objects.all().order_by("%s"% order_column)
    if query:
        queryset_list = query_results.filter(
            Q(item__icontains=query) |
            Q(price__icontains=query)
            ).distinct()
        if queryset_list:
            context={
                "query_results":queryset_list,
            }
        else :
            print("No item found")
            return render(request,'search.html')
        
    else:
        total = 0
        for prod in query_results:
            total+=prod.price
        print(total)
        context={
            "query_results":query_results,
            "total_expenses":total
        }
    return render(request, 'viewlist.html', context)

@login_required
def itemupdate(request, p_k=None):
    instance = get_object_or_404(Product, p_k=p_k)
    expense_form = ExpenseUploadForm(request.POST,request.FILES,instance=instance)
    if expense_form.is_valid():
        expense_form.save()
        return HttpResponseRedirect(reverse('expenses:viewlist'))

    context={
        "item":instance.item,
        "instance":instance,
        'ExpenseUploadForm':ExpenseUploadForm,
    }

    return render(request,"update.html",context)

@login_required
def itemdelete(request, p_k=None):
    item= get_object_or_404(Product, p_k=p_k)    
    if item.delete():
        return HttpResponseRedirect(reverse('expenses:viewlist'))
    return render(request, 'item_confirm_delete.html',{'item':item})

@login_required
def modify(request,p_k=None):
    instance = get_object_or_404(Product, p_k=p_k)
    return render(request,'modify.html', {'instance': instance})


