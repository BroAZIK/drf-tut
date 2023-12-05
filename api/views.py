from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def home(request: Request) -> Response:
    if request.method == 'GET':
        return Response({'message': 'get'})

    elif request.method == 'POST':
        return Response({'message': 'post'})
