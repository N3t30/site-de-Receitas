from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            # total de paginas que tem disponivel
            page_range=list(range(1, 21)),
            qtd_paginas=4,  # quantidades de paginas que serão mostradas ao usuario # noqa: E501
            current_page=1,  # Em qual pagina o usuario estar
        )
        # Lista nova dentro do pagination, será retornado o range de 4pags
        self.assertEqual([1, 2, 3, 4], pagination)
