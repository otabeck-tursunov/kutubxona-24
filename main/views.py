from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

from .models import *
from .forms import *

def home_view(request):
    today = datetime.today()
    context = {
        'today': today,
    }
    return render(request, 'home.html', context)


def talabalar_view(request):
    form = TalabaForm
    if request.method == "POST":
        form = TalabaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Talaba.objects.create(
                ism=data.get('ism'),
                kurs=data.get('kurs'),
                guruh=data.get('guruh'),
                kitob_soni=data.get('kitob_soni')
            )
        return redirect('talabalar')
    talabalar = Talaba.objects.all()
    guruhlar = [item['guruh'] for item in Talaba.objects.all().values('guruh')]
    guruhlar = sorted(list(set(guruhlar)))

    search = request.GET.get('search')
    kurs = request.GET.get('kurs')
    guruh = request.GET.get('guruh')

    if search is not None:
        talabalar = talabalar.filter(ism__icontains=search)

    if kurs is not None and kurs != '0':
        talabalar = talabalar.filter(kurs=kurs)

    if guruh is not None and guruh != '0':
        talabalar = talabalar.filter(guruh=guruh)

    context = {
        'talabalar': talabalar,
        'guruhlar': guruhlar,
        'search': search,
        'kurs': kurs,
        'guruh': guruh,
        'form': form,
    }
    return render(request, 'talabalar.html', context)


def talaba_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_details.html', context)


def talaba_delete_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    talaba.delete()
    return redirect('talabalar')


def talaba_update_view(request, talaba_id):
    talaba = get_object_or_404(Talaba, id=talaba_id)
    if request.method == "POST":
        talaba.ism = request.POST.get('ism')
        talaba.kurs = request.POST.get('kurs')
        talaba.guruh = request.POST.get('guruh')
        talaba.kitob_soni = request.POST.get('kitob_soni')
        talaba.save()
        return redirect('talabalar')
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_update.html', context)


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context)


def muallif_delete_confirm_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_confirm_delete.html', context)


def muallif_delete_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    muallif.delete()
    return redirect('mualliflar')


def muallif_update_view(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    if request.method == "POST":
        muallif.ism = request.POST.get('ism')
        muallif.jins = request.POST.get('jins')
        muallif.t_sana = request.POST.get('t_sana')
        muallif.kitob_soni = request.POST.get('kitob_soni')
        if request.POST.get('tirik') == 'on':
            muallif.tirik = True
        else:
            muallif.tirik = False
        muallif.save()
        return redirect('mualliflar')
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_update.html', context)


def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar,
    }
    return render(request, 'kitoblar.html', context)


def kitob_qoshish_view(request):
    form = KitobForm
    if request.method == "POST":
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('kitoblar')
    context = {
        'form': form,
    }
    return render(request, 'kitob_qoshish.html', context)


def kitob_update_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    if request.method == "POST":
        kitob.nom = request.POST.get('nom')
        kitob.janr = request.POST.get('janr')
        kitob.sahifa = request.POST.get('sahifa')
        kitob.muallif = Muallif.objects.get(id=request.POST.get('muallif_id'))
        kitob.save()
        return redirect('kitoblar')
    mualliflar = Muallif.objects.all().order_by('ism')
    context = {
        'kitob': kitob,
        'mualliflar': mualliflar,
    }
    return render(request, 'kitob_update.html', context)


def recordlar_view(request):
    recordlar = Record.objects.all()
    context = {
        'recordlar': recordlar,
    }
    return render(request, 'recordlar.html', context)


def record_update_view(request, pk):
    record = get_object_or_404(Record, id=pk)
    if request.method == "POST":
        qaytardi = request.POST.get('qaytardi')
        if qaytardi == 'on':
            qaytardi = True
        else:
            qaytardi = False
        Record.objects.filter(id=pk).update(
            talaba=get_object_or_404(Talaba, id=request.POST.get('talaba_id')),
            kitob=get_object_or_404(Kitob, id=request.POST.get('kitob_id')),
            kutubxonachi=get_object_or_404(Kutubxonachi, id=request.POST.get('kutubxonachi_id')),
            olingan_sana=request.POST.get('olingan_sana'),
            qaytardi=qaytardi,
        )
        qaytargan_sana = request.POST.get('qaytargan_sana', None)
        print(qaytargan_sana)
        if qaytargan_sana is not None:
            Record.objects.filter(id=pk).update(
                qaytargan_sana=qaytargan_sana,
            )
        return redirect('recordlar')

    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    kutubxonachilar = Kutubxonachi.objects.all()
    context = {
        'record': record,
        'talabalar': talabalar,
        'kitoblar': kitoblar,
        'kutubxonachilar': kutubxonachilar,
    }
    return render(request, 'record_update.html', context)
