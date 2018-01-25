from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('polls/about.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def products(request):
    template = loader.get_template('polls/products.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('polls/contact.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
