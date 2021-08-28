from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import Url
from .feeds import URLGenerator


generator = URLGenerator()


def generator_view(request):
    form = UrlForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            url = form.save()
            context['shotened_url'] = request.build_absolute_uri(url.key)
            form = UrlForm()
    context['form'] = form
    return render(request, 'index.html', context)


def navigate(request, key):
    if key.isalnum():
        id = generator.get_id(key)
        qs = Url.objects.filter(id=id)
        if not qs.exists():
            return render(request, 'failedurls.html', {"response": 'url was not found'})
        else:
            return redirect(qs.first().url)
    else:
        return render(request, 'failedurls.html', {"response": 'url is invalid'})
