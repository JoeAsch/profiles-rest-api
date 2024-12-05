from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""


    def get(self, request, format=None):
        """returns a list of api view features"""
        an_apiview = [
        'Uses HTTP methods (put,delete,patch,put,get)',
        'is similar to a tradtional django view',
        'Gives you the most control over your app logic',
        'is mapped manually to urls',
        ]

        return Response({'message':'Hello!', 'an api_view':an_apiview})


# Create your views here.
