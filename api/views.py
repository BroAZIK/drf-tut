from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class HomeView(APIView):
    def get(self, request: Request) -> Response:
        params = request.query_params
        a = params['a']
        b = params['b']

        return Response(
            data={'message': int(a) + int(b)}, 
            status=status.HTTP_200_OK
        )

    def post(self, request: Request) -> Response:
        data = request.data
        a = data['a']
        b = data['b']

        return Response(
            data={'data': int(a) + int(b)}, 
            status=status.HTTP_201_CREATED
        )
