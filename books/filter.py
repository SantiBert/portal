import django_filters
from .models import BookEntry


class BookdminListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = BookEntry
        fields = ["name"]
