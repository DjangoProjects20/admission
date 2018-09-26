from django.shortcuts import render
from django.http import HttpResponse
from . models import *
import datetime
import time


def index(request):
    posts = Posts.objects.filter(is_active=True)
    sertification_mass = sertification.objects.filter(is_active=True)
    time_acceptances = time_acceptance.objects.filter(is_active=True)
    time_acceptance_periods = time_acceptance_period.objects.filter(is_active2 = True)
    date_norm = time_acceptance_periods[0].time_lable_one
    date_two= time_acceptance_periods[0].time_lable_two
    sliders = slide.objects.filter(is_active=True)
    settings = setting.objects.filter(is_active=True)
    about = about_us.objects.filter(is_active=True)
    adress = useful_little_things.objects.get(name_english = 'adress' )
    telefon = useful_little_things.objects.get(name_english = 'telefon' )
    email = useful_little_things.objects.get(name_english = 'email' )
    name_site = useful_little_things.objects.get(name_english = 'name_site' )
    footer_descr = useful_little_things.objects.get(name_english = 'footer_descr' )
    about_us_descr = useful_little_things.objects.get(name_english = 'about_us_descr' )
    return render(request, 'index.html', locals())


def time_acceptance_period_page(request):
      time_acceptance_periods = time_acceptance_period.objects.filter(is_active = True)# выборка данных по генератору он тут один
      #print(time_acceptance_periods)
      # вывожу метки времени
      date_norm = time_acceptance_periods[0].time_lable_one
      #print('перввая метка ровна:')
      #print(date_norm)#проверка первой метки
      date_two= time_acceptance_periods[0].time_lable_two
      #print('вторая метка ровна:')
      #print(date_two)#проверка второй метки
      h1= time_acceptance_periods[0].holiday1
      #print('далее первый выходной')
      #print(h1)#проверка первого выходного
      h2= time_acceptance_periods[0].holiday2
      #print('далее второй выходной')
      #print(h2)#проверка второго выходного
      #нахожу разницу для расчетов
      one = int(datetime.datetime(date_norm.year,date_norm.month, date_norm.day, date_norm.hour, date_norm.minute).timestamp())
      two = int(datetime.datetime(date_two.year, date_two.month, date_two.day, date_two.hour, date_two.minute).timestamp())
      razn = two - one
      #print ('разница равна ' + str(razn))
      
      date_str = date_norm#[:19]
      #print ( 'вся строка ' + str(date_norm) )
      #print ( 'это год ' + str(date_norm.year) )
      #print ( 'это месяц ' + str(date_norm.month) )
      #print ( 'это день ' + str(date_norm.day) )
      #print ( 'это день ' + str(date_norm.hour) )
      #print ( 'это день ' + str(date_norm.minute))
      
      
      #print( 'это время ' + str(datetime.datetime(date_norm.year,date_norm.month, date_norm.day, date_norm.hour, date_norm.minute).timestamp()))
      ##print (time.mktime(date_str.timetuple()))
      # получаем unix time 
      datestring = int(datetime.datetime(date_norm.year,date_norm.month, date_norm.day, date_norm.hour, date_norm.minute).timestamp())
      dt = datetime.datetime.fromtimestamp(float(datestring))
      #print (dt)
      #создаем массив времен приема
      mass = list(range(datestring,datestring + int(razn), int(time_acceptance_periods[0].period)))
      ##print(mass)
      for label_time_priem in mass:
        #new_time_acceptance = time_acceptance( info = '' , label_time = datetime.datetime.fromtimestamp(float(period)))
        #new_time_acceptance.save()
        ##
        ## тут нужно вычленить только часы и если они равны 18 19 20 21 22 24 24 1 2 3 4 5 6 7 8  то приемы не добавлять
        ##
        #print ( 'метка времени' +  str(datetime.datetime.fromtimestamp(float(label_time_priem)))[10:13])
        #получаю часы метки [10:13] это срез 
        t = str(datetime.datetime.fromtimestamp(float(label_time_priem)))[10:13]
        #получаю день недели
        d = str(datetime.datetime.fromtimestamp(float(label_time_priem)).weekday())
        #print( 'день недели '+ d)
        tp = int(t)# перевод в целочисленный вид чтобы работал if
        di = int(d)# -//-
        H1i  = int(h1)#-//-
        H2i  = int(h2)#-//-
        ot = time_acceptance_periods[0].ot
        do = time_acceptance_periods[0].do
        obed_one = time_acceptance_periods[0].obed_one
        obed_two = time_acceptance_periods[0].obed_two
        #отсев по выходным
        if di!= H1i and di!=H2i:
            if tp < do and tp >= ot and tp != obed_one and tp != obed_two:
                new_time_acceptance = time_acceptance(name = '', label_time = datetime.datetime.fromtimestamp(float(label_time_priem)), is_active = 'True', FIO = '', email = '', tel = '')  
                #print( 'метка добавлена')
                new_time_acceptance.save()
                
           
        
       
      return render(request, 'time_acceptance_period_page.html', locals())
      
 # перевод даты в unix      
# date string to datetime object
#date_str = "2008-11-10 17:53:59"
#dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
##print repr(dt_obj)
# пример обрезки
#dt_string = '2011-07-15 13:00:00+00:00'
#    new_dt = dt_string[:19]
  #  dt = datetime.datetime.strptime(new_dt, '%Y-%m-%d %H:%M:%S')
  
def admission_one(request, admission_id):
    adress = useful_little_things.objects.get(name_english = 'adress' )
    telefon = useful_little_things.objects.get(name_english = 'telefon' )
    email = useful_little_things.objects.get(name_english = 'email' )
    time_acceptances = time_acceptance.objects.get(id = admission_id)
    return render(request, 'one.html', locals()) 
 
def priem(request):
    password_priem_from_bd = useful_little_things.objects.get(name_english = 'password_priem')
    pass_priem = int(password_priem_from_bd.descrip )*3 
    time_acceptances = time_acceptance.objects.filter(is_active=True)
    time_acceptance_periods = time_acceptance_period.objects.filter(is_active2 = True)
    date_norm = time_acceptance_periods[0].time_lable_one
    date_two= time_acceptance_periods[0].time_lable_two
    return render(request, 'index_priem.html', locals()) 
 

def post_one_page(request, post_id):
    post_text = Posts.objects.get(id = post_id)
    return render(request, 'one_post.html', locals()) 
''' 
def form_email(request):
    if request.method == "POST":
        data = request.POST
        name_from_form = data.get("name")
        mail_user = data.get("email")
        phone = data.get("phone")
        message_from_form = data.get("sms")
        time_acceptance.objects.filter(id = int(message_from_form)).update( name = 'Это время заняли',
        is_active = False, FIO = name_from_form, email = mail_user, tel = phone)
        return render(request, 'good_massege.html', locals())
       
      
  
'''
def form_email(request):
    if request.method == "POST":
        data = request.POST
        name_from_form = request.POST["name"]
        mail_user = request.POST["email"]
        phone = request.POST["subject"]
        message_from_form = request.POST["sms"]
        #print (message_from_form)
        time_acceptance.objects.filter(id = int(message_from_form)).update( name = 'Это время заняли',
        is_active = False, FIO = name_from_form, email = mail_user, tel = phone)
        return HttpResponse("Ваша заявка отправлена ")
             
   
        





  
