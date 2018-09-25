from django.contrib import admin
from . models import *
# Register your models here.


''' для объедениения полей в админке'''
#class NoneInline(admin.TabularInline):
      #model = None
      #extra = 0

class time_acceptance_periodAdmin (admin.ModelAdmin):
      list_display = [field.name for field in time_acceptance_period._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = time_acceptance_period

admin.site.register(time_acceptance_period, time_acceptance_periodAdmin )


''' для объедениения полей в админке'''
#class user_infoInline(admin.TabularInline):
      #model = user_info
      #extra = 0

class time_acceptanceAdmin (admin.ModelAdmin):
      list_display = [field.name for field in time_acceptance._meta.fields]
      #searh_fields = ['is_active']
      #inlines = [user_infoInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      
      class Meta:
        model = time_acceptance

admin.site.register(time_acceptance, time_acceptanceAdmin )






class slideAdmin (admin.ModelAdmin):
      list_display = [field.name for field in slide._meta.fields]
      #inlines = [user_infoInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = slide

admin.site.register(slide, slideAdmin)




class settingAdmin (admin.ModelAdmin):
      list_display = [field.name for field in setting._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = setting

admin.site.register(setting, settingAdmin )

class about_usAdmin (admin.ModelAdmin):
      list_display = [field.name for field in about_us._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = about_us

admin.site.register(about_us, about_usAdmin )




class useful_little_thingsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in useful_little_things._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = useful_little_things

admin.site.register(useful_little_things, useful_little_thingsAdmin )


"""  Модель Posts """
class PostsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in Posts._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = Posts
admin.site.register(Posts, PostsAdmin )
""" конец модели Posts"""


"""  Модель sertification """


class sertificationAdmin (admin.ModelAdmin):
      list_display = [field.name for field in sertification._meta.fields]
      #inlines = []
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = sertification
admin.site.register(sertification, sertificationAdmin )
""" конец модели sertification"""