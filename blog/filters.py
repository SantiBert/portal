import django_filters

from .models import BlogEntry, BlogCategory


class BlogAdminListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    user__username = django_filters.CharFilter(lookup_expr="icontains")
    user__first_name = django_filters.CharFilter(lookup_expr="icontains")
    user__last_name = django_filters.CharFilter(lookup_expr="icontains")
    category__name = django_filters.CharFilter(lookup_expr="icontains")
    date = django_filters.DateFilter()

    class Meta:
        model = BlogEntry
        fields = ["name", "user__username", "user__first_name",
                  "user__last_name", "category__name", "active", "date"]
