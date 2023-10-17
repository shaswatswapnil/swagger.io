from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from json.decoder import JSONDecodeError
from .googlesheets import get_google_sheet_data
from .serializers import GoogleSheetDataSerializer
from rest_framework.decorators import api_view
from rest_framework import status


class GoogleSheetDataAPIView(APIView):

    def get(self, request, format=None):
        data = get_google_sheet_data()
        serializer = GoogleSheetDataSerializer(data, many=True)  # Use many=True if data is a list

        if not data:
            return Response({"message": "No data available from Google Sheets"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)  # Use serializer.data to get the serialized data

        
        # serialized_data = []
        # try:
        #     for item in data:
        #         if isinstance(item, dict): 
        #             serializer = GoogleSheetDataSerializer(data=item)
        #             if serializer.is_valid():
        #                 serialized_data.append(serializer.validated_data)
        #             else:
        #                 return Response(serializer.errors, status=400)
        #         else:
        #             return Response({"message": "Invalid data format. Expected a dictionary."}, status=400)
        #     return JsonResponse(serialized_data , safe=False)
        # except JSONDecodeError as e:
        #     return Response({"message": "Invalid JSON data from Google Sheets"}, status=500)