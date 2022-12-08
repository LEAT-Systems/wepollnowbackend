from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utilities.models import Lga, State
from utilities.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from user.permissions import IsAdmin, IsSuperAdmin
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.request import Request


@api_view(['GET', 'POST'])
def states(request):
    if request.method == 'GET':
        state_data = State.objects.all()
        serialized_data = StateSerializer(state_data, many=True)
        return Response(serialized_data.data)

    if request.method == 'POST': 
        serialized_data = StateSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])
def states_by_id(request, pk):
    state_data = State.objects.get(pk=pk)
    if request.method == 'GET':
        serialized_data = StateSerializer(state_data)
        return Response(serialized_data.data)

    if request.method == 'PUT':
        serialized_data = StateSerializer(state_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

    if request.method == 'DELETE':
        state_data.delete() 
        return Response()

#LGA APIs

@api_view(['GET','POST'])
def lga(request):
        if request.method == 'GET':
            lga_data = Lga.objects.all()
            serialized_data = LgaSerializer(lga_data, many=True)
            return Response(serialized_data.data)

        if request.method == 'POST': 
            serialized_data = LgaSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data)
            else:
                return Response(serialized_data.errors)

@api_view(['GET'])
def lga_by_state(request, state_id):
    if request.method == 'GET':
        data = Lga.objects.all().filter(state_id = state_id)
        serialized_data = LgaSerializer(data, many='True')
        return Response(serialized_data.data)

@api_view(['GET'])
def lga_by_senatorial(request, senatorial_id):
    if request.method == 'GET':
        data = Lga.objects.all().filter(senatorial_id = senatorial_id)
        serialized_data = LgaSerializer(data, many='True')
        return Response(serialized_data.data)

@api_view(['GET', 'POST'])
def senatorial(request):
    if request.method == 'POST':
        serialized_data = SenatorialSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    if request.method == 'GET':
        senatorial_data = Senatorial.objects.all()
        serialized_data = StateSerializer(senatorial_data, many=True)
        return Response(serialized_data.data)

@api_view(['GET', 'UPDATE', 'DELETE'])
def senatorial_by_state(request, state_id):
    if request.method == 'GET':
        data = Senatorial.objects.all().filter(state_id = state_id)
        serialized_data = SenatorialSerializer(data, many='True')
        return Response(serialized_data.data)

@api_view(['GET', 'POST'])
def candidates(request):
    if request.method == 'POST':
        serialized_data = CandidateSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    if request.method == 'GET':
        data = Candidate.objects.all()
        serialized_data = CandidateSerializer(data, many='True')
        return Response(serialized_data.data)

class CandidateRetrieveUpdateDelete(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
class CreateContact(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    
class ListContact(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    #permission_classes = [IsAdmin]
    
    
@api_view(['GET', 'POST'])
def subscriber(request):
    if request.method == 'POST':
        serialized_data = SubscriberSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    if request.method == 'GET':
        data = Subscriber.objects.all()
        serialized_data = SubscriberSerializer(data, many='True')
        return Response(serialized_data.data)

class PartyList(ListAPIView):
    serializer_class = PartySerializer
    queryset = Party.objects.all()



