from django.contrib import admin

from .models import Cafes, CafePromo, CafeReview

class CafesAdmin(admin.ModelAdmin):
    exclude = ("created_at", "updated_at",)
    list_display = ("name", "rating", "distance", "is_open_24h")

admin.site.register(Cafes, CafesAdmin)
admin.site.register(CafePromo)
admin.site.register(CafeReview)
