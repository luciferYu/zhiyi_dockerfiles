
from rest_framework.pagination import PageNumberPagination

#自定义分页类
class MyPageNumberPagination(PageNumberPagination):
    def __init__(self, page_size=10):
        # 每页显示多少个
        self.page_size = page_size
        # 默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
        self.page_size_query_param = "size"
        # 获取页码数的
        self.page_query_param = "page"
