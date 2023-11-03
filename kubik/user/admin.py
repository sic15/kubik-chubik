from django.contrib import admin

from .models import User

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name',
              'middle_name', 'last_name', 'type', 'password']
    list_display = ['first_name', 'last_name', 'type']

"""
@admin.register(User)
class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('sudscriptions',)
    fields = ['author', 'name', 'text',
              'cooking_time', 'image', 'tags', 'sudscriptions']
    list_display = ['name', 'author']
    list_filter = ['author', 'name', 'tags']

    def sudscriptions(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['name', 'color']


@admin.register(AmountIngredient)
class AmountIngredientAdmin(admin.ModelAdmin):
    readonly_fields = ('measurement_unit', )
    fields = ['recipe', 'ingredient', ('amount', 'measurement_unit')]

    def measurement_unit(self, obj):
        return obj.ingredient.measurement_unit
    measurement_unit.short_descripti
    """