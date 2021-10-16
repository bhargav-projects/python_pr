from django.core.serializers import serialize
from django.http import HttpResponse
import json
class SerializeMixin(object):
    def Serialize(self,qs):
        #json dat is getting all meta data using serilizer function
        json_data=serialize('json',qs)
       
        #now coverting json data to python data
        p_data =json.loads(json_data)
        
        final_list =[]
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return json_data
        # return HttpResponse(json_data,content_type='application/json',status=200)


class HttpResponseMixin(object):
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)