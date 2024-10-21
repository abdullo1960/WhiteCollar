from django.contrib import admin

from myapp.models import (Info, Contact, BlogModel, 
                          MessageModel, Testimonial, ExpertsModel, 
                          DataModel, EmailModel, LocationModel)

admin.site.register(Info)
admin.site.register(Contact)
admin.site.register(BlogModel)
admin.site.register(MessageModel)
admin.site.register(Testimonial)
admin.site.register(ExpertsModel)
admin.site.register(DataModel)
admin.site.register(EmailModel)
admin.site.register(LocationModel)