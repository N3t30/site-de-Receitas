import math


def make_pagination_range(
        page_range,
        qtd_pages,
        current_page,
):
    middle_range = math.ceil(qtd_pages / 2)  # meio das pages ranges
    start_range = current_page - middle_range  # Começa dois numeros antes da middle_range # noqa: E501
    stop_range = current_page + middle_range  # para dois numeros do middle page # noqa: E501

    # "abs" tira o sinal de negativo,
    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    return page_range[start_range: stop_range]
