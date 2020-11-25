import django_filters
from .models import OtherSites, Quote, Suscriptor, FriendSites


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


class FriendSitesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = FriendSites
        fields = ["name"]


class SuscriptorListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Suscriptor
        fields = ["email"]
