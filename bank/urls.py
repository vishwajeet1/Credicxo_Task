from django.urls import path
from .views import branchDetail, allBranch
urlpatterns = [
    path('', branchDetail, name="branchDetails"),
    path('list', allBranch, name="branchList"),
]
