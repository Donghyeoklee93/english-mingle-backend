from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.viewsets import ModelViewSet


class SubjectViewSet(ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
