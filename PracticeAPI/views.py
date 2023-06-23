from rest_framework.response import Response
from rest_framework.decorators import api_view
from Student.models import StudentClass
from Student.serializers import StudentSerializer
from rest_framework.views import APIView
from django.http import HttpResponse

@api_view(['GET'])
def checkdata(req):
    return Response({'status':200, 'payload':'hello'})

@api_view(['GET','POST'])
def allStudentData(req):
    if req.method == 'GET':
        query = StudentClass.objects.all()
        se = StudentSerializer(query,many = True)
        return Response({'status':200, 'payload':se.data})
    if req.method == 'POST':
        sc = StudentSerializer(data=req.data)
        if sc.is_valid():
            sc.save()
            return Response({'status':200, 'payload':'successfully saved'})
        return Response({'status':404, 'payload':'error......'})

# @api_view(['POST'])
# def StudentPost(req):
#     sc = StudentSerializer(data=req.data)
#     if sc.is_valid():
#         sc.save()
#         return Response({'status':200, 'payload':'successfully saved'})
#     return Response({'status':404, 'payload':'error......'})


@api_view(['GET','PATCH','PUT'])
def getAData(req,uid):
    if req.method == 'GET':
        try:
            query = StudentClass.objects.get(id = uid)
            sc = StudentSerializer(query, many = False)
            return Response({'status':200, 'payload':sc.data})
        except:
            return Response({'status':404, 'payload':'data not found'})
    if req.method == 'PATCH':
        query = StudentClass.objects.get(id = uid)
        sc = StudentSerializer(query,data=req.data,partial = True)
        if sc.is_valid():
            sc.save()
            return Response({'status':200, 'payload':'successfully saved'})
        return Response({'status':404, 'payload':'error......'})
    if req.method == 'PUT':
        query = StudentClass.objects.get(id = uid)
        sc = StudentSerializer(query,data=req.data)
        if sc.is_valid():
            sc.save()
            return Response({'status':200, 'payload':'successfully saved'})
        return Response({'status':404, 'payload':'error......'})
    

class student(APIView):   #API view
    def get(self,req):
        query = StudentClass.objects.all()
        se = StudentSerializer(query,many = True)
        return Response({'status':200, 'payload':se.data})
    
    def put(self,req):
        query = StudentClass.objects.get(id = req.data['id'])
        sc = StudentSerializer(query,data=req.data)
        if sc.is_valid():
            sc.save()
            return Response({'status':200, 'payload':'successfully saved'})
        return Response({'status':404, 'payload':'error......'})
    
    def delete(self,req):
        query = StudentClass.objects.get(id = req.data['id'])
        query.delete()
        return Response({'status':200})
    
def checkUpdate(req):
    return HttpResponse("ok")
    



        

