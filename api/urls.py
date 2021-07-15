from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    PollModelViewSet,
    QuestionModelViewSet,
)

router = DefaultRouter()
router.register(
    r'polls/(?P<post_id>\d+)/questions',
    QuestionModelViewSet,
    basename='questions',
 )
router.register(r'polls', PollModelViewSet, basename='polls')

urlpatterns = [
    path('', include(router.urls)),
]
