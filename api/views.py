from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def home(request: Request) -> Response:
    if request.method == 'GET':
        print(request.query_params)

        return Response({"name": request.query_params['name']})

    elif request.method =='POST':
        return Response({"name": request.data['name']})

