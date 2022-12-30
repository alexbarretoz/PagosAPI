from rest_framework.pagination import  PageNumberPagination


class SimplePagination(PageNumberPagination):
    page_size = 100
    page_query_param= "page_zize"
    max_page_size =2000