from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=1,  # Em qual pagina o usuario estar
        )
        # Lista nova dentro do pagination, será retornado o range de 4pags
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501
        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=1,  # Em qual pagina o usuario estar
        )
        self.assertEqual([1, 2, 3, 4], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=2,  # Em qual pagina o usuario estar
        )
        self.assertEqual([1, 2, 3, 4], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        # Aqui o intervalo deve mudar

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=3,  # Em qual pagina o usuario estar
        )
        self.assertEqual([2, 3, 4, 5], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501
