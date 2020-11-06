import django_filters
from .models import OtherSites, Quote


class OtherSitesListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = OtherSites
        fields = ["name"]


class QuoteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Quote
        fields = ["autor"]
