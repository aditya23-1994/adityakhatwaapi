from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Project, Resume
from .serializers import ProjectSerializers, ResumeSerializers


@csrf_exempt
def project_list(request):
    """
            List all the Projects or create a new Project.
    """
    if request.method == "GET":
        projects = Project.objects.all()
        serializers = ProjectSerializers(projects, many=True)
        return JsonResponse(serializers.data, safe=False, status=200)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializers = ProjectSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)

@csrf_exempt
def project_detail(request, pk):

    try:
        project = Project.objects.get(pk=pk)
    except project.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ProjectSerializers(project)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializers = ProjectSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)

    elif request.method == "DELETE":
        project.delete()
        return HttpResponse(status=204)

@csrf_exempt
def resume_list(request):
    if request.method == "GET":
        resume = Resume.objects.all()
        serializers = ResumeSerializers(resume, many=True)
        return JsonResponse(serializers.data,safe=False, status=200)