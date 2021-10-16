from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size =3,
    #replace page param with our custom query
    page_query_param='p'
    # its for client selection its for 'on selected page how many reocrds u display'
    #?p=3 &orders=10
    page_size_query_param='reocrds'
    # even though u specified 10 but it shows only 7 because of max page 
    max_page_size =5
    
  