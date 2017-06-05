import os
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.conf import settings
from .forms import HomeTextForm

class Home(TemplateView):
    template_name = 'home.html'


def home_text(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            f = open(os.path.join(settings.BASE_DIR, 'home_text.txt'), 'r+')
            home_text = f.read()
            f.close()
            form = HomeTextForm()
            return render(request, 'home_text.html', {'home_text': home_text, 'form': form})
        return render(request, '403.html')
    return redirect('/admin/login/?next=/home-text/')

def home_text_edit(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            if request.method == 'POST':
                form = HomeTextForm(request.POST)
                if form.is_valid():
                    home_text = request.POST.get('home_text', None)
                    if home_text is not None and home_text != '':
                        f = open(os.path.join(settings.BASE_DIR, 'home_text.txt'), 'w+')
                        f.write(home_text)
                        f.close()
                    return redirect('/home-text/')
        return render(request, '403.html')
    return redirect('/admin/login/?next=/home-text/')