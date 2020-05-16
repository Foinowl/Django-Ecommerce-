from django_filters import CharFilter
import django_filters


from .models import *


class ItemsFilter(django_filters.FilterSet):

    # note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Item
        fields = '__all__'
        exclude = [ 'discount_price', 'slug', 'description', 'image']


