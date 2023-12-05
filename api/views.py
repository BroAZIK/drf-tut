from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def home(request: Request) -> Response:
    if request.method == 'GET':
        params = request.query_params
        print(params)
        
        return Response({'message': 'get'})

    elif request.method == 'POST':
        print(request.data)

        return Response({'data': 'post'})
