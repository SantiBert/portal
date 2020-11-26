import django_filters
from .models import Link


class LinkListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Link
        fields = ["name"]
