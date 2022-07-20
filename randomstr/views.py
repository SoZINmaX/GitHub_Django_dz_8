from django.shortcuts import render
import random
import string
from randomstr.models import Randomstr

def randomstr(request):
    rand_string = ''
    letters = string.ascii_lowercase
    digits = string.digits
    specials = "!№;%:?*()_+"
    digits_requested = request.GET.get('digits')
    specials_requested = request.GET.get('specials')
    length = request.GET.get('length')
    letters_and_digits_and_symbols = letters
    letters_and_digits_and_symbols += specials if specials_requested else ''
    letters_and_digits_and_symbols += digits if digits_requested else ''
    if length is None:
        length = 0
    elif int(length) > 100:
        message = 'Sorry, the number You entered is more than 100. Pls try again'
        return render(request, 'randomstr/lengthmore100.html', context={'message':message})
    else:
        rand_string = ''.join(random.choice(letters_and_digits_and_symbols) for i in range(int(length)))
        Randomstr.objects.create(length=length, digits=digits_requested if digits_requested else False, specials=specials_requested if specials_requested else False)
        
    return render(request, 'randomstr/random.html', context={'rand_string':rand_string})