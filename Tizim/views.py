from django.shortcuts import render,redirect

from .models import *
from .forms import *

"Bosh sahifa"
def tizim(request):
    return render(request,"Tizim.html")


"Tizimlar"

def xona(request):
    if request.method == "POST":
        Xona.objects.create(
            nom =request.POST.get("nomi"),
            raqam = request.POST.get("raqami")
        )
        return redirect('/xona/')

    natija = Xona.objects.all()
    kiritilgan_nom = request.GET.get("nomi")
    if kiritilgan_nom is not None:
        natija = Xona.objects.filter(nom__contains=kiritilgan_nom)
    content = {
        "xona" : natija
    }
    return render(request,"Xona.html",content)


def yonalish(request):
    if request.method == "POST":
        Yonalish.objects.create(
            nom=request.POST.get("nomi"),
            narx =request.POST.get("narxi")
        )
        return redirect('/yonalish/')

    natija = Yonalish.objects.all()
    kiritilgan_nom = request.GET.get("nomi")
    if kiritilgan_nom is not None:
        natija = Yonalish.objects.filter(nom__contains=kiritilgan_nom)
    context = {
        "yonalish": natija
    }
    return render(request,"yonalish.html",context)



def ustoz(request):
    if request.method == "POST":
        Ustoz.objects.create(
            ism = request.POST.get("ismi"),
            tel_raqam = request.POST.get("tel_raqami"),
            manzil = request.POST.get("manzili"),
            yonalish = Yonalish.objects.get(id=request.POST.get("yonalish"))
        )
        return redirect('/ustoz/')

    natija = Ustoz.objects.all()
    kiritilgan_ism = request.GET.get("ismi")
    if kiritilgan_ism is not None:
        natija = Yonalish.objects.filter(ism__contains=kiritilgan_ism)
    context = {
        "ustoz": natija,
        "yonalish": Yonalish.objects.all()
    }
    return render(request,"ustoz.html",context)


def guruh(request):
    if request.method == "POST":
        Guruh.objects.create(
            nom = request.POST.get("nomi"),
            vaqt = request.POST.get("vaqti"),
            xona = Xona.objects.get(id=request.POST.get("xona")),
            yonalish = Yonalish.objects.get(id=request.POST.get("yonalish")),
            ustoz = Ustoz.objects.get(id=request.POST.get("ustoz"))
        )
        return redirect('/guruh/')
    natija = Guruh.objects.all()
    kiritilgan_nom = request.GET.get("nomi")
    if kiritilgan_nom is not None:
        natija = Guruh.objects.filter(nom__contains=kiritilgan_nom)
    context = {
        "guruh": natija,
        "xona": Xona.objects.all(),
        "yonalish": Yonalish.objects.all(),
        "ustoz": Ustoz.objects.all()
    }
    return render(request,"guruh.html",context)

def talaba(request):
    if request.method == "POST":
        Talaba.objects.create(
            ism =request.POST.get("ismi"),
            tel_raqam = request.POST.get("tel_raqami"),
            manzil = request.POST.get("manzili"),
            guruh = Guruh.objects.get(id=request.POST.get("guruh")),
            yonalish = Yonalish.objects.get(id=request.POST.get("yonalish")),
        )
        return redirect('/talaba/')

    natija = Talaba.objects.all()
    kiritilgan_ism = request.GET.get("ismi")
    if kiritilgan_ism is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ism)
    content = {
        "talaba" : natija,
        "guruh" : Guruh.objects.all(),
        "yonalish" : Yonalish.objects.all()
    }
    return render(request,"talaba.html",content)


def tolov(request):
    if request.method == "POST":
        Tolov.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get("talaba")),
            guruh=Guruh.objects.get(id=request.POST.get("guruh")),
            summa =request.POST.get("summa"),
            chegirma = request.POST.get("chegirma"),
            qarz = request.POST.get("qarz"),
        )
        return redirect('/tolov/')

    natija = Tolov.objects.all()
    kiritilgan_talaba = request.GET.get("talaba")
    if kiritilgan_talaba is not None:
        natija = Tolov.objects.filter(talaba__ism__contains=kiritilgan_talaba)
    content = {
        "tolov" : natija,
        "guruh" : Guruh.objects.all(),
        "talaba" : Talaba.objects.all()
    }
    return render(request,"tolov.html",content)



"Malumot"
def bitta_talaba(req,pk):
    data = {
        "talaba": Talaba.objects.get(id=pk)
    }
    return render(req, 'bitta_talaba.html',data)


def bitta_ustoz(req,pk):
    data = {
        "ustoz": Ustoz.objects.get(id=pk)
    }
    return render(req, 'bitta_ustoz.html',data)

"Ochirish"
def xona_ochir(request, pk):
    Xona.objects.get(id=pk).delete()
    return redirect("/xona/")


def yonalish_ochir(request,pk):
    Yonalish.objects.get(id=pk).delete()
    return redirect('/yonalish/')

def ustoz_ochir(request,pk):
    Ustoz.objects.get(id=pk).delete()
    return redirect('/ustoz/')

def guruh_ochir(request,pk):
    Guruh.objects.get(id=pk).delete()
    return redirect("/guruh/")

def talaba_ochir(request,pk):
    Talaba.objects.get(id=pk).delete()
    return redirect('/talaba/')


def tolov_ochir(request,pk):
    Tolov.objects.get(id=pk).delete()
    return redirect('/tolov/')



"Tahrirlash"
def xona_update(request, pk):
    if request.method == "POST":
        Xona.objects.filter(id=pk).update(
            nom = request.POST.get("nomi"),
            raqam = request.POST.get("raqami"),
        )
        return redirect('/xona/')

    context = {
        "xona": Xona.objects.get(id=pk)
    }
    return render(request,"xona_update.html",context)


def yonalish_update(request,pk):
    if request.method =="POST":
        Yonalish.objects.filter(id=pk).update(
            nom=request.POST.get("nomi"),
            narx=request.POST.get("narxi"),
        )
        return redirect('/yonalish/')
    context = {
        "yonalish": Yonalish.objects.get(id=pk)
    }
    return render(request,"yonalish_update.html",context)



def ustoz_update(request,pk):
    if request.method == "POST":
        Ustoz.objects.filter(id=pk).update(
            ism = request.POST.get("ismi"),
            tel_raqam = request.POST.get("tel_raqami"),
            manzil = request.POST.get("manzili"),
            yonalish=Yonalish.objects.get(id=request.POST.get("yonalish"))
        )
        return redirect('/ustoz/')
    context = {
        "ustoz":Ustoz.objects.get(id=pk),
        "yonalish": Yonalish.objects.all()
    }
    return render(request,"ustoz_update.html",context)

def guruh_update(request,pk):
    if request.method == "POST":
        Guruh.objects.filter(id=pk).update(
            nom = request.POST.get("nomi"),
            vaqt = request.POST.get("vaqti"),
            xona = Xona.objects.get(id=request.POST.get("xona")),
            yonalish = Yonalish.objects.get(id=request.POST.get("yonalish")),
            ustoz = Ustoz.objects.get(id=request.POST.get("ustoz"))
        )
        return redirect('/guruh/')
    context = {
        "guruh": Guruh.objects.get(id=pk),
        "xona": Xona.objects.all(),
        "yonalish": Yonalish.objects.all(),
        "ustoz": Ustoz.objects.all()
    }
    return render(request,"guruh_update.html",context)


def talaba_update(request,pk):
    if request.method == "POST":
        Talaba.objects.filter(id=pk).update(
            ism = request.POST.get("ismi"),
            tel_raqam = request.POST.get("tel_raqami"),
            manzil = request.POST.get("manzili"),
            guruh=Guruh.objects.get(id=request.POST.get("guruh")),
            yonalish=Yonalish.objects.get(id=request.POST.get("yonalish"))
        )
        return redirect('/ustoz/')
    context = {
        "talaba":Talaba.objects.get(id=pk),
        "guruh": Guruh.objects.all(),
        "yonalish": Yonalish.objects.all()
    }
    return render(request,"talaba_update.html",context)

def tolov_update(request,pk):
    if request.method == "POST":
        Tolov.objects.filter(id=pk).update(
            talaba=Talaba.objects.get(id=request.POST.get("talaba")),
            guruh=Guruh.objects.get(id=request.POST.get("guruh")),
            summa = request.POST.get("summa"),
            chegirma = request.POST.get("chegirma"),
            qarz = request.POST.get("qarz"),
        )
        return redirect('/tolov/')
    context = {
        "guruh": Guruh.objects.all(),
        "tolov": Tolov.objects.get(id=pk),
        "talaba": Talaba.objects.all()
    }
    return render(request,"tolov_update.html",context)