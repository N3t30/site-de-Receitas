import math

from django.core.paginator import Paginator


def make_pagination_range(
        page_range,
        qtd_pages,
        current_page,
):
    middle_range = math.ceil(qtd_pages / 2)  # meio das pages ranges
    start_range = current_page - middle_range  # Começa dois numeros antes da middle_range # noqa: E501
    stop_range = current_page + middle_range  # para dois numeros depois do middle page # noqa: E501
    total_pages = len(page_range)
    # "abs" tira o sinal de negativo,
    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range: stop_range]
    return {
        'pagination': pagination,
        'page_range': page_range,
        'stop_range': stop_range,
        'qtd_pages': qtd_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        # se a primeira pagina esta sendo exibida,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }


def make_pagination(request, queryset, per_page, qtd_pages=4):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        qtd_pages,
        current_page,
    )

    return page_obj, pagination_range
