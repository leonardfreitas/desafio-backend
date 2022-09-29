from rest_framework import routers

from apps.accounts.views import UserViewSet
from apps.categories.views import CategoryViewSet
from apps.quiz.views import OptionViewSet, QuestionViewSet, QuizViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('categories', CategoryViewSet, basename='category')
router.register('options', OptionViewSet, basename='option')
router.register('questions', QuestionViewSet, basename='question')
router.register('quiz', QuizViewSet, basename='quiz')

routes = router.urls
