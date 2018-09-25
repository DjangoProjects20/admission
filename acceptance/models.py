from django.db import models
from tinymce import HTMLField



class time_acceptance_period(models.Model):
      name = models.CharField(max_length = 164, blank=True,   null=True, default='None', verbose_name= 'название периода можно не заполнять' )
      time_lable_one = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name= 'время начала приемов ' )
      time_lable_two = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name= ' время окончания приемов' )
      ot = models.DecimalField(max_digits=10, decimal_places=0, default=0 , verbose_name= 'час начало приемов: написать 9 если с  09:00, 10 если с 10:00')
      do = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name= 'час окончаиния приемов: написать 18 если с  18:00, 19 если с 19:00')
      obed_one = models.DecimalField(max_digits=10, decimal_places=0, default=0 , verbose_name= 'час начала обеда')
      obed_two = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name= 'час окончаиния обеда')
      holiday1 = models.CharField(max_length = 25, blank=True,   null=True, default='None', verbose_name= 'первый выходной писать цифрой (дни недели понедельник это 0, вторник это 1 и т.д.) Внимание если вы работаете и по выходным вписать 7' )
      holiday2 = models.CharField(max_length = 25, blank=True,   null=True, default='None', verbose_name= 'второй выходной писать цифрой (дни недели понедельник это 0, вторник это 1 и т.д.) Внимание если вы работаете и по выходным вписать 7'  )
      period = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name= 'период дробление времени одного приема, писать в секундах 3600 = 1 час, 1800 = 0.5 часа ' )
      is_active = models.BooleanField(default='True', verbose_name= 'включить этот генератор? внимание после окончания генерирования выключить эту галку ' )
      is_active2 = models.BooleanField(default='True', verbose_name= 'включить две метки на главную страницу? ' ) 
      def __str__(self):
       return "генератор приемов: %s" % (self.name)
      class Meta:
        verbose_name = 'генератор приемов'
        verbose_name_plural = 'генератор приемов'

class time_acceptance(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default='None', verbose_name= ' примечание ' )
      label_time = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name= 'время начала приемов ')
      is_active = models.BooleanField(default='True', verbose_name= 'включить этот прием для генерирования времен приема? ' )
      FIO = models.CharField(      max_length = 64, blank=True,   null=True, default='None', verbose_name= ' ФИО клиента ' )
      email = models.CharField(      max_length = 64, blank=True,   null=True, default='None', verbose_name= ' эл почта ' )
      tel = models.CharField(      max_length = 64, blank=True,   null=True, default='None', verbose_name= 'контактный тел. ' )
      def __str__(self):
       return "время приема: %s" % (self.name)
      class Meta:
        verbose_name = 'время приема'
        verbose_name_plural = 'время приемов'
        
class slide(models.Model):
    name = models.CharField(max_length = 128, blank=True, null=True, default=None, verbose_name='имя')
    image = models.ImageField(blank = True, upload_to='sliders_images/', help_text = 'выберите картинку для слайда', verbose_name='картинка слайда')
    description = models.CharField(max_length = 128, blank=True, null=True, default=None, verbose_name='содержание слайда')
    link = models.CharField(max_length = 128, blank=True, null=True, default='#featured-services', verbose_name='ссылка если нужна')
    is_active = models.BooleanField(default = True ,verbose_name='добавить для вывода на основной странице?') 
    active_slide = models.CharField(max_length = 128, blank=True, null=True, default=None, verbose_name='активный ли это слайд (внимание написать active только для первого слайда в остальных случаях пустое значение)')
    button_text = models.CharField(max_length = 128, blank=True, null=True, default='посмотреть сайт', verbose_name='текст кнопки в слайдере')
   
    #кастомизация названий в категориях 
    def __str__(self):
        return "слайд: %s" % (self.name)   
    #кастомизация во множественом и в единственном числе    
    class Meta:
       verbose_name = 'слайд'
       verbose_name_plural = 'слайды'
       
class setting(models.Model):
    name = models.CharField(max_length = 1028, blank=True, null=True, default=None, verbose_name='имя услуги')
    description = HTMLField(blank=True, null=True, default=None, verbose_name='описание')
    icon = models.CharField(max_length = 2046, blank=True, null=True, default=None, verbose_name='иконка с fontawesome.com например <i class="fas fa-briefcase-medical"></i>')
    is_active = models.BooleanField(default = False, verbose_name='добавить на главную?') 
    #кастомизация названий в категориях 
    def __str__(self):
        return "Услуга: %s" % (self.name)
        
    
    #кастомизация во множественом и в единственном числе    
    class Meta:
       verbose_name = 'услуга'
       verbose_name_plural = 'услуги'
       
class about_us(models.Model):
    name = models.CharField(max_length = 1028, blank=True, null=True, default=None, verbose_name='имя услуги')
    image = models.ImageField(blank = True, upload_to='sliders_images/', help_text = 'выберите картинку для слайда', verbose_name='картинка для информации о нас')
    description = HTMLField(blank=True, null=True, default=None, verbose_name='описание')
    icon = models.CharField(max_length = 2046, blank=True, null=True, default=None, verbose_name='иконка с fontawesome.com например <i class="fas fa-briefcase-medical"></i>')
    is_active = models.BooleanField(default = False, verbose_name='добавить на главную?') 
    #кастомизация названий в категориях 
    def __str__(self):
        return "Услуга: %s" % (self.name)
        
    
    #кастомизация во множественом и в единственном числе    
    class Meta:
       verbose_name = 'информация о нас'
       verbose_name_plural = 'информации о нас'  
      
class useful_little_things(models.Model):
    name = models.CharField(max_length = 1028, blank=True, null=True, default=None, verbose_name='имя мелочи')
    name_english = models.CharField(max_length = 1028, blank=True, null=True, default=None, verbose_name='имя мелочи на английском для фильтра')
    descrip= models.CharField(max_length = 1028, blank=True, null=True, default=None, verbose_name='описание обычным текстом')
    description = HTMLField(blank=True, null=True, default=None, verbose_name='описание позволяющие наполнять HTML разметку')
    icon = models.CharField(max_length = 2046, blank=True, null=True, default=None, verbose_name='иконка с fontawesome.com например <i class="fas fa-briefcase-medical"></i>')
    is_active = models.BooleanField(default = False, verbose_name='добавить на главную?') 
    #кастомизация названий в категориях 
    def __str__(self):
        return "Услуга: %s" % (self.name)
        
    
    #кастомизация во множественом и в единственном числе    
    class Meta:
       verbose_name = 'полезная мелочь на сайте'
       verbose_name_plural = 'полезные мелочи на сайте' 
       
       
""" начало модели Posts """
class Posts(models.Model):
      name = models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'имя статьи кратко это будет в меню навигации')
      description = HTMLField(  blank=True,  null=True, default='', verbose_name= ' все описание статьи можно вставлять код html целиком')
      is_active = models.BooleanField(      default='True', verbose_name= ' выложить статью на сайт ')
      def __str__(self):
        return "Статья: %s" % (self.name)
      class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
               
""" начало модели sertification"""
class sertification(models.Model):
      name = models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'название серитфиката')
      image = models.ImageField(blank = True, upload_to='sertification_images/', help_text = 'выберите картинку для сертификата', verbose_name='картинка слайда')
      is_active = models.BooleanField(      default='True', verbose_name= ' выложить сертификат на сайт ')
      def __str__(self):
        return "Сертификат: %s" % (self.name)
      class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"        