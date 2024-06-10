from django.contrib import admin
from .models import Autor, Categoria, Artigo, Comentario, Avaliacao

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao

class ArtigoAdmin(admin.ModelAdmin):
    inlines = [
        AvaliacaoInline,
    ]

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['artigo', 'autor', 'rating']
    list_filter = ['rating']
    search_fields = ['artigo__titulo', 'autor__username']

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario)
admin.site.register(Avaliacao, AvaliacaoAdmin)


