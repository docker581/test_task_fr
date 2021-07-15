from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer
from .permissions import IsNotAdmin

from datetime import date


def get_session_id(request):
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key  # getting session_key
    session_id = int.from_bytes(
        session_key.encode('utf-8'),
        byteorder='big',
    )  # encoding
    return session_id


@permission_classes([IsNotAdmin, IsAdminUser])
class PollModelViewSet(ModelViewSet):
    serializer_class = PollSerializer

    def get_queryset(self):
        today = date.today()
        queryset = Poll.objects.filter(date_end__gte=today)  # active polls
        return queryset

    def perform_create(self, serializer):
        session_id = get_session_id(self.request)
        serializer.save(session_id=session_id)


@permission_classes([IsNotAdmin, IsAdminUser])
class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
