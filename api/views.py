from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def home(request: Request) -> Response:
    if request.method == 'GET':
        params = request.query_params
        a = params['a']
        b = params['b']

        return Response(
            data={'message': int(a) + int(b)}, 
            status=status.HTTP_200_OK
        )

    elif request.method == 'POST':
        data = request.data
        a = data['a']
        b = data['b']

        return Response(
            data={'data': int(a) + int(b)}, 
            status=status.HTTP_201_CREATED
        )
