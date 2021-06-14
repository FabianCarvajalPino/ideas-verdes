from django.shortcuts import render, redirect, render_to_response
from . models import Idea
from ..logreg_app.models import User
from .forms.add_idea import IdeaForm
from django.db.models import Count
#from django.http.response import JsonResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

# Create your views here

def ideas(request):
    try:
        idea_form = IdeaForm(request.POST)
        if request.method == 'POST':
            if idea_form.is_valid():
                print('is_valid'+'*'*15)
                user_selected = User.objects.get(id = int(request.session['user_id']))
                Idea.objects.create(
                    owner = user_selected,
                    idea = request.POST['idea']
                )
                ideas_ordered = Idea.objects.annotate(count = Count('likes')).order_by('-count')
                
                context = {
                    'ideas': ideas_ordered,
                    'user_selected': user_selected,
                }
                if request.is_ajax():
                    html = render_to_string('ideas_table.html', context, request=request)
                    return JsonResponse({'form': html})
                
                return redirect('/ideas_brillantes')

                
            else:
                print('is not valid'+'*'*15)
                idea_form = IdeaForm(request.POST)
                print(idea_form)
                user_selected = User.objects.get(id = int(request.session['user_id']))
                ideas_ordered = Idea.objects.annotate(count = Count('likes')).order_by('-count')
                msg_idea_error = 'La idea debe tener al menos 10 caracteres'
                context = {
                    'ideas': ideas_ordered,
                    'user_selected': user_selected,
                    'idea_form': idea_form,
                    'msg_idea_error': msg_idea_error
                }
                return render(request, 'all_ideas.html', context)

        elif request.method=='GET':
            idea_form = IdeaForm(request.POST)
            user_selected = User.objects.get(id = int(request.session['user_id']))
            ideas_ordered = Idea.objects.annotate(count = Count('likes')).order_by('-count')
            context = {
                'ideas': ideas_ordered,
                'user_selected': user_selected,
                'idea_form': idea_form
            }
            return render(request, 'all_ideas.html', context)
    except:
        return redirect('/')

def idea_detail(request, idea_id):
    try:
        user_selected = User.objects.get(id = int(request.session['user_id']))
        idea = Idea.objects.get(id=int(idea_id))
        count = idea.likes.all().count()
        print(count)
        context = {
            'user_selected': user_selected,
            'idea': idea,
            'count':count
        }
        return render(request, 'idea.html', context)
    except:
        return redirect('/')

def add(request):
    pass
    '''
    try:
        idea_form = IdeaForm(request.POST)
        if idea_form.is_valid():
            user_selected = User.objects.get(id = int(request.session['user_id']))
            Idea.objects.create(
                owner = user_selected,
                idea = request.POST['idea']
            )
            return redirect('/ideas_brillantes')
    except:
        return redirect('/')
'''
def delete(request, idea_id):
    try:
        user_selected = User.objects.get(id= int(request.session['user_id']))
        idea = Idea.objects.get(id = int(idea_id))
        idea.delete()
        return redirect('/ideas_brillantes')
    except:
        return redirect('/')


def like(request, idea_id):
    try:
        if request.method == 'POST':

            user_selected = User.objects.get(id= int(request.session['user_id']))
            idea = Idea.objects.get(id = int(idea_id))
            idea.likes.add(user_selected)
            ideas_ordered = Idea.objects.annotate(count = Count('likes')).order_by('-count')
            context = {
                'ideas': ideas_ordered,
                'user_selected': user_selected,
            }
            if request.is_ajax():
                print('ajax working baby')
                html = render_to_string('ideas_table.html', context, request=request)

                return JsonResponse({'form': html})
        print('ajax not working baby')
        return redirect('/ideas_brillantes')
    except:
        return redirect('/')

def unlike(request, idea_id):
    try:
        user_selected = User.objects.get(id= int(request.session['user_id']))
        idea = Idea.objects.get(id = int(idea_id))
        idea.likes.remove(user_selected)
        return redirect('/ideas_brillantes')
    except:
        return redirect('/')