from rest_framework.pagination import PageNumberPagination

class TodoViewPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 5