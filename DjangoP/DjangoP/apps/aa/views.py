from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Arti, Comm
from django.urls import reverse


def index(request):
    late_arti_list = Arti.objects.order_by('-pub_date')[:5]
    return render(request, 'arti/list.html', {'late_arti_list': late_arti_list})


def detail(request, arti_id):
    try:
        a = Arti.objects.get(id=arti_id)
    except:
       raise Http404('Not FOUND ((((')
    late_comm_list = a.comm_set.order_by('-id')[:10]
    return render(request, 'arti/detail.html', {'arti': a , 'late_comm_list':late_comm_list})

def leave_comm(request, arti_id):
    try:
        a = Arti.objects.get(id=arti_id)
    except:
       raise Http404('Not FOUND ((((')
    a.comm_set.create(author_name = request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('aa:detail', args=(a.id,)))