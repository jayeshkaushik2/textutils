# this is made by me jayesh kaushik
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    # render(first takes the request, filename, takes an argument like dictnoary)
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone')
        massage = request.POST.get('massage')
        print(name)
        print(email)
        print(phoneNumber)

        # send_mail(subject, message, from_email, recipient_list)
        send_mail(f'send by: {name}', f'{massage}', email, [
                  'jayeshkaushik@gmail.com'])
    return render(request, 'contact.html')


def analyaz(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charcount = request.POST.get('charcount', 'off')

    
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc == 'on':
        analyazed = ""
        for char in djtext:
            if char not in punctuation:
                analyazed = analyazed+char
        pramas = {'purpose': 'remove punctuations',
                  'analyazed_text': analyazed}
        djtext = analyazed

    if fullcaps == 'on':
        analyazed = djtext.upper()
        pramas = {'purpose': 'all uppercase', 'analyazed_text': analyazed}
        djtext = analyazed

    if charcount == 'on':
        analyazed = 'number of charcters: '+str(len(djtext))
        pramas = {'purpose': 'count charcters', 'analyazed_text': analyazed}
        return render(request, 'analyaz.html', pramas)
    
    if removepunc=='off' and charcount=='off' and fullcaps=='off':
        return HttpResponse("you didn't on any checkbox!")

    return render(request, 'analyaz.html', pramas)
