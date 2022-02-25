from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import ExpenseInformation
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from django.db.models import Sum
import matplotlib
import matplotlib.pyplot as plt


class UserRegister(FormView):
    template_name = 'budget_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('expenses')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

class UserLoginView(LoginView):
    template_name = 'budget_app/login.html'
    fields = '__all__'
    readirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('expenses')

class ExpenseList(LoginRequiredMixin, ListView):
    model = ExpenseInformation
    context_object_name = 'expenses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = context['expenses'].filter(user=self.request.user)

        return context

class ExpenseDetail(LoginRequiredMixin,DetailView):
    model = ExpenseInformation
    context_object_name = 'expense'
    template_name = 'budget_app/expense.html'

class ExpenseAdd(LoginRequiredMixin,CreateView):
    model = ExpenseInformation
    fields = ['category','description','expense']
    success_url = reverse_lazy('expenses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExpenseAdd, self).form_valid(form)

class ExpenseUpdate(LoginRequiredMixin,UpdateView):
    model = ExpenseInformation
    fields = ['category','description','expense']
    success_url = reverse_lazy('expenses')



class ExpenseDelete(LoginRequiredMixin,DeleteView):
    model = ExpenseInformation
    context_object_name = 'expense'
    success_url = reverse_lazy('expenses')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

def barchart(request):
    data = []
    labels = []
    dictionaries = ExpenseInformation.objects.filter(user=request.user).values('category').annotate(suma = Sum('expense'))

    for dictionary in dictionaries:
        for value in dictionary.values():
            if type(value) == int:
                data.append(value)
            else:
                labels.append(value)

    fig = plt.figure()
    print(data, labels)
    colors = [ 'plum', 'pink', 'purple','m', 'hotpink','orchid','darkorchid','deeppink']
    plt.pie(data, labels = labels,autopct='%1.1f%%',colors=colors)
    plt.savefig('piechart.png')
    return render(request,'budget_app/piechart.html')

