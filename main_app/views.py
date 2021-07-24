from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
import redis, json
from time import time


# Connect to Redis
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


class LinksView(APIView):
    """GET visited domanins"""
    def get(self, request):
        time_from = self.request.query_params.get('from')
        time_to = self.request.query_params.get('to')

        if time_from and time_to:
            resp = {'domains': []}

            for key in redis_instance.keys():
                # check time
                if int(time_from) <= int(key) <= int(time_to):
                    data_redis = redis_instance.get(key)
                    for i in json.loads(data_redis):
                        # check uniqueness for domains
                        if i not in resp['domains']:
                            resp['domains'].append(i)
            return Response(resp, status=200)
        else:
            response_error = {
                'msg': f"incorrect or missing parametrs <from> or <to>"
            }
            return Response(response_error, 400)


class AddLinksView(APIView):
    """POST Links"""
    def post(self, request):
        response_error = {
            'msg': """incorrect reauest, POST method, request body {"links": ["www.somedomain.ru", "http://somedomain2.com"]}"""
        }

        curr_time = int(time())
        # 1st check json
        try:
            item = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return Response(response_error, 400)
        key = list(item.keys())[0]
        if key.lower() != 'links':
            return Response(response_error, 400)
        value = item[key]
        # 2nd check json for correct
        if type(value) is not list:
            return Response(response_error, 400)

        redis_instance.set(curr_time, json.dumps(value))
        response = {
            'msg': f"{curr_time} successfully set to {value}"
        }
        return Response(response, 201)
