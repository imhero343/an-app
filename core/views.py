from django.shortcuts import render, redirect

from core.models import Person


def tech(request):
    return render(request, 'core/tech.html')


def done(request):
    return render(request, 'core/done.html')


def techAjax(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['direction']
        c = request.POST['represent']
        d = request.POST['gov']
        e = request.POST['area']
        f = request.POST['phone']
        g = request.POST['nkown_person']
        h = request.POST['nkown_person_phone']
        i = request.POST['nkown_person_relation']
        z = request.POST['age']
        x = request.POST['notes']

        person = Person(
            name=a,
            direction=b,
            represent=c,
            gov=d,
            area=e,
            phone=f,
            nkown_person=g,
            nkown_person_phone=h,
            nkown_person_relation=i,
            age=int(z),
            notes=x,
        )
        person.save()
        return redirect('done')
