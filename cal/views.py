from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
# from .forms import EventForm

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Task
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):


        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        eid=1
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        date=self.request.GET.get('date','1')
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        t=Task.objects.filter(eid=eid,date=str(d.year)+"-"+str(d.month)+"-"+str(date))
        context['t']=t
        context['date']=months[d.month-1] + " "+str(date)+", "+str(d.year)
        if self.request.method == "POST":
            context["hiii"]="hiiiiiii"
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def submit(request,id):
    t=Task.objects.get(pk=id)
    t.status=request.POST["status"]
    t.duration=request.POST["duration"]
    t.save()
    return HttpResponseRedirect(reverse('cal:calendar'))