from django.contrib import admin
from .models import Festival
from .models import Banda
from .models import Localizacao

admin.site.register(Festival)
admin.site.register(Banda)
admin.site.register(Localizacao)
