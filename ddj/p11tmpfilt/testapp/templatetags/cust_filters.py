from django import template
register=template.Library()


def truncate5(value):
    result=value[0:5]
    return result  #if u want all are ur name replace resut with 'bhargav'

#this is another method 
@register.filter('t_n')
def truncate_n(value,n):
    result=value[0:n]
    return result

register.filter('truncate5',truncate5)
