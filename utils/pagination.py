from django.core.paginator import Paginator


def get_paginated(request, query, items_number=5, page_query='page'):
    paginator = Paginator(query, items_number)
    page = request.GET.get(page_query, 1)
    items = paginator.get_page(page)
    return items
