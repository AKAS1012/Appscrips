from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .models import Name, Cricketer, Color
from .serializers import NameSerializer, CricketerSerializer, ColorSerializer


class NameListAV(APIView):
	def get(self, request):
		name = Name.objects.all()
		serializer = NameSerializer(name, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = NameSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class NameDetail(APIView):
	def get(self, request, pk):
		try:
			name = Name.objects.get(pk=pk)
		except Name.DoesNotExist:
			return Response({'error': 'Name Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = NameSerializer(name)
		return Response(serializer.data)

	def put(self, request, pk):
		name = Name.objects.get(pk=pk)
		serializer = NameSerializer(name, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		name = Name.objects.get(pk=pk)
		name.delete()
		return Response(status=HTTP_204_NO_CONTENT)


class CricketerListAV(APIView):

	def get(self, request):
		cricketer = Cricketer.objects.all()
		serializer = CricketerSerializer(cricketer, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CricketerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class CricketerDetail(APIView):

	def get(self, request, pk):
		try:
			cricketer = Cricketer.objects.get(pk=pk)
		except Cricketer.DoesNotExist:
			return Response({'error': 'Cricketer  Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = CricketerSerializer(cricketer)
		return Response(serializer.data)

	def put(self, request, pk):
		cricketer = Cricketer.objects.get(pk=pk)
		serializer = CricketerSerializer(cricketer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		cricketer = Cricketer.objects.get(pk=pk)
		cricketer.delete()
		return Response(status=HTTP_204_NO_CONTENT)


class ColorListAV(APIView):

	def get(self, request):
		color = Color.objects.all()
		serializer = ColorSerializer(color, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ColorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class ColorDetailAV(APIView):
	def get(self, request, pk):
		try:
			color = Color.objects.get(pk=pk)
		except Color.DoesNotExist:
			return Response({'error': 'color Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = ColorSerializer(color)
		return Response(serializer.data)

	def put(self, request, pk):
		color = Color.objects.get(pk=pk)
		serializer = ColorSerializer(color, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		color = Color.objects.get(pk=pk)
		color.delete()
		return Response(status=HTTP_204_NO_CONTENT)
