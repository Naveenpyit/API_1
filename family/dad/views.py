from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import clgstudent,clgcourses
from .serializer import clgserializer,courseserializer
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser



@csrf_exempt
def capi_view(request,id=0):
    if request.method=='GET':
        return cget_view(request)
    elif request.method=='POST':
        return cpost_view(request)
    elif request.method=='PUT':
        return cput_view(request,id)
    elif request.method=='DELETE':
        return cdel_view(request,id)


def cget_view(request):
    stud_id=request.GET.get('id',None)
    if stud_id:
        try:
            studs=clgstudent.objects.get(student_id=stud_id)
            studs_serial=clgserializer(studs)
            return JsonResponse(studs_serial.data,safe=False)
        except clgstudent.DoesNotExist:
            return JsonResponse({"message":"Student doesn't Exist.."},status=404)
    else:
        studs=clgstudent.objects.all()
        studs_serial=clgserializer(studs,many=True)
        return JsonResponse(studs_serial.data,safe=False)
    
def cpost_view(request):
    stud=JSONParser().parse(request)
    studs=clgserializer(data=stud)
    if studs.is_valid():
        studs.save()
        return JsonResponse({"message":"Created Successfully","data":studs.data},status=200)
    return JsonResponse({"message":"Can't create student","data":studs.errors},status=404)
  

def cput_view(request,id):
    stud=JSONParser().parse(request)
    try:
        studs=clgstudent.objects.get(student_id=id)
        stud_serial=clgserializer(studs,data=stud)
        if stud_serial.is_valid():
            stud_serial.save()
            return JsonResponse({"message":"Updated Successfully","data":stud_serial.data},status=201)
        return JsonResponse({"message":"Failed to update","data":stud_serial.errors},status=404)
    except clgstudent.DoesNotExist:
        return JsonResponse({"message":"Student does not Exists"},safe=False)
    
def cdel_view(request,id):
    try:
        stud=clgstudent.objects.get(student_id=id)
        stud.delete()
        return JsonResponse({"message":"Deleted Successfully"},status=200)   
    except clgstudent.DoesNotExist:
        return JsonResponse({"message":"Failed to Delete"},status=404)
    



@csrf_exempt
def api_view(request,id=0):
    if request.method=='GET':
        return get_view(request)
    elif request.method=='POST':
        return post_view(request)
    elif request.method=='PUT':
        return put_view(request,id)
    elif request.method=='DELETE':
        return del_view(request,id)


def get_view(request):
    cour_id=request.GET.get('id',None)
    if cour_id:
        try:
            cour=clgcourses.objects.get(course_id=cour_id)
            cour_serial=courseserializer(cour)
            return JsonResponse(cour_serial.data,safe=False)
        except clgcourses.DoesNotExist:
            return JsonResponse({"Course doesn't Exists"},status=404)
    else:
        cour=clgcourses.objects.all()
        cour_serial=courseserializer(cour,many=True)
        return JsonResponse(cour_serial.data,safe=False)

def post_view(request):
    cour=JSONParser().parse(request)
    cour_serial=courseserializer(data=cour)
    if cour_serial.is_valid():
        cour_serial.save()
        return JsonResponse({"message":"Created Successfully..","data":cour_serial.data},status=201)
    return JsonResponse({"message":"Failed to Create","data":cour_serial.errors},status=404)

def put_view(request,id):
    cour=JSONParser().parse(request)
    try:
        cours=clgcourses.objects.get(course_id=id)
        cour_serial=courseserializer(cours,data=cour)
        if cour_serial.is_valid():
            cour_serial.save()
            return JsonResponse({"message":"Updated Successfully..","data":cour_serial.data},status=201)
        return JsonResponse({"message":"Failed to update","data":cour_serial.errors},status=404)
    except clgcourses.DoesNotExist:
        return JsonResponse({"message":"Courses doesn't Exists"},safe=False,status=400)
    

def del_view(request,id):
    try:
        cour=clgcourses.objects.get(course_id=id)
        cour.delete()
        return JsonResponse({"message":"Deleted Successfully.."},status=201)
    except clgcourses.DoesNotExist:
        return JsonResponse({"message":"Course doesn't Exists"},status=404)






# from django.http import JsonResponse
# from .models import clgcourses
# from .serializers import courseserializer

# def get_view(request):
#     # Get the 'Authorization' token from the request headers
#     auth_header = request.headers.get('Authorization', None)

#     if not auth_header:
#         # If the Authorization token is missing, return a 401 Unauthorized response
#         return JsonResponse({"message": "Authorization token is missing"}, status=401)
    
#     # Try to extract the token part from the Authorization header (Bearer <token>)
#     try:
#         token = auth_header.split(' ')[1]  
#         # Optionally, here you can validate the token (for example, using JWT or other methods)
#         # For now, we'll just check if the token is not empty.
#         if token == "your_valid_token_here":  # Replace with your actual validation logic
#             pass  # Token is valid, proceed with the request
#         else:
#             # If the token is invalid, return a 401 Unauthorized response
#             return JsonResponse({"message": "Invalid or expired token"}, status=401)
#     except IndexError:
#         # If the format is incorrect (e.g., no space after 'Bearer'), return 401
#         return JsonResponse({"message": "Invalid Authorization format"}, status=401)
    
#     # Now, proceed with the rest of your logic for fetching the courses
#     cour_id = request.GET.get('id', None)
#     if cour_id:
#         try:
#             cour = clgcourses.objects.get(course_id=cour_id)
#             cour_serial = courseserializer(cour)
#             return JsonResponse(cour_serial.data, safe=False)
#         except clgcourses.DoesNotExist:
#             return JsonResponse({"message": "Course doesn't exist"}, status=404)
#     else:
#         cour = clgcourses.objects.all()
#         cour_serial = courseserializer(cour, many=True)
#         return JsonResponse(cour_serial.data, safe=False)
