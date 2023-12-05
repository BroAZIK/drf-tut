# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class HomeView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        return Response(data={"name": request.query_params['name']}, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        return Response(data={"name": request.data['name']}, status=status.HTTP_201_CREATED)
