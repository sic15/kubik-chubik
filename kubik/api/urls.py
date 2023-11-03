from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register('teachers', views.TeacherViewSet)
router.register('users', views.UserViewSet)
router.register('students', views.StudentViewSet)
router.register('courses', views.CourseViewSet)

#router.register('ingredients', views.IngredientViewSet, basename='ingredients')
#router.register('users', views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),

]