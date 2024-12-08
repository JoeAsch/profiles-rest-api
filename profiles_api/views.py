from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from profiles_api import serializers


class HelloApiView(APIView):
    """test api view"""

    serializer_class = serializers.HelloSerializer



    def get(self, request, format=None):
        """returns a list of api view features"""
        an_apiview = [
        'Uses HTTP methods (put,delete,patch,put,get)',
        'is similar to a tradtional django view',
        'Gives you the most control over your app logic',
        'is mapped manually to urls',
        ]

        return Response({'message':'Hello!', 'an api_view':an_apiview})

    def post(self, request):
        """create a post hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handles update to an object"""

        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """handles partial update to an object"""

        return Response({ 'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handles removing an object"""

        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSets"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
        'uses actions (retrieve, list, create, update, partial update)',
        'automatically maps to urls using routers',
        'provides more functionality with less code',
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})



# Create your views here.
