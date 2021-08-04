from django.shortcuts import render

# Create your views here.



def w2_form_generator(request):

    return render(request, 'W2_form/w2_form_generator.html' )


def w2_form(request):
    return render(request, 'W2_form/w2_form_home.html')