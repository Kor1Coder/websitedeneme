from django.shortcuts import render,redirect
from .forms import nameform
from .models import *
from datetime import datetime
from django.contrib import messages
from itertools import chain
from operator import attrgetter
def index(request):
    global context
    one= graphe.objects.all()
    two=gamedevelope.objects.all()
    three=matlabe.objects.all()
    four=pythone.objects.all()
    five=solide.objects.all()
    six=siemene.objects.all()
    seven=guie.objects.all()
    eight=ansyse.objects.all()
    ten=chain(one, two,three,five,four,six,seven,eight)
    result=sorted(ten,key=attrgetter('date')) [-3:]
    context={'dataset':result}
    form = nameform(request.POST)
    if request.method=="POST" and form.is_valid():
            name=form.cleaned_data.get("name")
            soyad = form.cleaned_data.get("surname")
            email = form.cleaned_data.get("email")
            textarea = form.cleaned_data.get("textarea")
            radiooption = form.cleaned_data.get("inlineRadioOptions")
            if name != '' and soyad != '' and email!='':
                Form.objects.create(name=name,surname=soyad,email=email,date=datetime.now() ,testarea=textarea,option=radiooption)
                # message_body=f'Kim tarafından:{name} {soyad}'+'\n'+  textarea+'\n'+ f'mail atan kişininin adresi{email}'
                # EmailMessage("form submission confirmation",message_body,to=['hubahuba06@gmail.com'])
                # email.send()
                messages.warning(request,"Mesajınız başarıyla gönderildi.")
                return redirect('/index',context=context)

    else:
        form = nameform()
    return render(request, "index.html",context=context)
def solidworks(request):
    context=dict()
    context['dataset']=solide.objects.all()
    context['nameofprogram']="solidworks çalışmalarım"
    context['description']="Solidworks alanında 2D ve 3D çizimler yapmaktayım. Unsurlar, çizim, saç levha ve montaj alanlarını biliyorum." \
                           "Bu kısımda neler yapabildiğimi sizlerle paylaşacağım. "
    return render(request,"soldiplusnx.html",context=context)

def siemennx(request):
    context = dict()
    context['dataset'] = siemene.objects.all()
    context['nameofprogram'] = "Sıemen NX11 çalışmalarım"
    context[
        'description'] = " Başlangıç eğitimimi ODTÜ 1.sınıf 2. dönemde Niyazi Ersan Gürkan'dan aldım." \
                         "Eğitim sürecinde 2 ve 3 boyutlu parçaları tasarladım. Eğitimde montaj ve saç levha kısmından da " \
                         "bahsedildi. Sonrasında kendim CAM kısmını öğrenmeye çalıştım. "
    return render(request, "soldiplusnx.html", context=context)

def matlab(request):
    context = dict()
    context['dataset'] = matlabe.objects.all()
    context['nameofprogram'] = "Matlab çalışmalarım"
    context[
        'description'] = "2023 yılında aldığım me 210 kodlu uygulamalı matematik dersinde " \
                         "Ahmet Buğra Koku'nun önerileriyle matlabi araştırmaya başladım. " \
                         "Makine öğrenmesi, veri işleme ve simülasyon kısmıyla ilgileniyorum. Zaman " \
                         "içinde yaptığım çalışmaları burda paylaşmayı düşünüyorum.    "
    return render(request, "ortak.html", context=context)
def pythondef(request):
    context = dict()
    context['dataset'] = pythone.objects.all()
    context['nameofprogram'] = "Python çalışmalarım"
    context['description'] = " Python'a Ceng 240 dersi ile başladım. Sonrasında ilgimi çekti ve araştırma" \
                         "yaparak öğrenmeye çalıştım. Oyun geliştirme, görüntü işleme, gui, veri işleme " \
                         "alanlarını araştırarak işleme mantıklarını anladım. "
    return render(request, "ortak.html", context=context)
def ansysdef(request):
    context = dict()
    context['dataset'] = ansyse.objects.all()
    context['nameofprogram'] = "ANSYS çalışmalarım"
    context[
        'description'] =" ANSYS 'in varlığından Türk Traktörde staj yaparken haberdar oldum." \
                        "Üniversitede ANSYS adına herhangi bir ders almadım. ANSYS tutorial " \
                        "(https://www.ansys.com/academic/learning-resources) sayfasından kavram ve uygulamalı" \
                        "eğitimle öğrenmeye çalıştım. Çok büyük bir kütüphaneye sahip olan bu uygulamayı " \
                        "biliyorum diyemem fakat güzel bir noktaya geldiğimi düşünüyorum. "
    return render(request, "ortak.html", context=context)
def guidef(request):
    context = dict()
    context['dataset'] = guie.objects.all()
    context['nameofprogram'] = "GUI çalışmalarım"
    context[
        'description'] = " GUI' yi pyqt5 ve pysimplegui ile keşfettim. Bu kısımda beni heycanlandıran şey" \
                         "msn gibi bir platform kurabilme fikri. Ayrıca zaman zaman kendi işimi kolaylaştırabilmek" \
                         "için küçük çaplı programlara ihtiyaç duyuyorum. Bunları sizinle paylaşacağım."
    return render(request, "ortak.html", context=context)
def gamedevelopdef(request):
    context = dict()
    context['dataset'] = gamedevelope.objects.all()
    context['nameofprogram'] = "Oyun Geliştirme Çalışmalarım"
    context[
        'description'] = "Oyun tasarımı için pygame'i kullanıyorum. Yani 2D oyun tasarlayabiliyorum" \
                         "2000 lerin oyunlarına yoğunlaştım. Bu oyunlar bana kodlamanın mantığını gösteriyor." \
                         "2024' te GOOGLE 'ın başlattığı oyun ve uygulama akademisine başvurdum. Kabül gördüğüm" \
                         "taktirde 9 aylık eğitim sürecinin ardından C++,C hakkında bilgim olacak. Bu sayede UNITY motorunda" \
                         "3D oyun tasarımına başlamayı düşünüyorum. "
    return render(request, "ortak.html", context=context)
def graphic(request):
    context = dict()
    context['dataset'] = graphe.objects.all()
    context['nameofprogram'] = "Grafik Tasarım Çalışmalarım"
    context[
        'description'] = " Bu alanda çok az bir bilgim var. Bu alan hedeflerimin arasında. Oyun geliştirme" \
                         "kısmında bahsettiğim gibi oyun yapımı sırasında çok fazla görsel zorluk" \
                         "yaşıyorum. Bu zorlukları pillow ve opencv ile gidermeye çalışsam da " \
                         "kendime özgü karakter ve çizimlerle tasarım yapmak istiyorum. 2024 yılı için " \
                         " hedeflerimden biri blender, adobe photoshop ve illustrator alanlarında belli bir " \
                         "seviyeye gelebilmek.  "
    return render(request, "ortak.html", context=context)
def latest(request,slug,id):
    print(slug,id)
    one = graphe.objects.all()
    two = gamedevelope.objects.all()
    three = matlabe.objects.all()
    four = pythone.objects.all()
    five = solide.objects.all()
    six = siemene.objects.all()
    seven = guie.objects.all()
    eight = ansyse.objects.all()
    ten = chain(one, two, three, five, four, six, seven, eight)
    result = sorted(ten, key=attrgetter('date'))[-3:]
    context = {}
    for i in result:
        print(i.slug,i.id)
        if i.slug==slug and i.id==id:
            context['dataset']=i
            print(i.img)
            if i.slug in ['python','matlab','gamedevelop','gui']:
                return render(request,'inceleçizim.html',context=context)
            elif i.slug in ['ansys','matlab','solid']:
                return render(request, 'inceleyazılım.html', context=context)