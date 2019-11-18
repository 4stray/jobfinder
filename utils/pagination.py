from django.core.paginator import Paginator


def get_paginated(request, model, items_number=5, page_query='page'):
    items = model.objects.all()
    paginator = Paginator(items, items_number)
    page = request.GET.get(page_query, 1)
    items = paginator.get_page(page)
    return items
