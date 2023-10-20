from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=1,  # Em qual pagina o usuario estar
        )['pagination']
        # Lista nova dentro do pagination, será retornado o range de 4pags
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501
        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=1,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=2,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        # Aqui o intervalo deve mudar

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=3,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

    def test_make_sure_middle_ranges_are_correct(self):  # noqa: E501

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=10,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=12,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=18,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=19,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=20,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501

        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_pages=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=21,  # Em qual pagina o usuario estar
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)  # Lista nova dentro do pagination, será retornado o range de 4pags # noqa: E501
