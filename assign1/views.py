from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random
# Create your views here.

quote_List= ["Scarlett johanneson I will drink ur bath water...", 
             "I'm just trying to grow. That's one thing I told myself is, Don't worry about who people say is the best player.",
             "You're the real MVP.",
              "Y'all know who I am. I'm Kevin Durant.",
              ]
imgUrl_List= ["https://i.ytimg.com/vi/qizrZjJfWiE/sddefault.jpg",
              "https://cdn.sanity.io/images/c1chvb1i/production/49b72189b71a4df4ca67d5fa21c7295db0eca04e-1100x735.jpg",
              "https://cdn.nba.com/teams/legacy/www.nba.com/thunder/sites/thunder/files/summerfeature_durant_160608.jpg",
              "https://grantland.com/wp-content/uploads/2014/10/kevin-durant-hurt-e1413169241143.jpg?w=1191",
              ]

def quote(request):
    template_name = 'assign1/quote.html'
    imageUrl = random.choice(imgUrl_List)
    quote = random.choice(quote_List)
    context={
        "imageUrl" : imageUrl,
        "qoute" : quote
    }

    return render(request, template_name, context, )

def about(request):
    template_name = 'assign1/about.html'

    return render(request, template_name)

def show_all(request):
    template_name = 'assign1/show_all.html'

    return render(request, template_name)