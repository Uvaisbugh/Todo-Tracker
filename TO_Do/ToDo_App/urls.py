from django.urls import path, include

from ToDo_App import views

urlpatterns = [
    path('',views.index,name="index"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:taskid>/',views.update,name="update"),
    # path('details',views.details,name="details")
    path('vHome/',views.ListTask.as_view(),name='vHome'),
    path('vDetails/<int:pk>/',views.ShowDetails.as_view(),name='vDetails'),
    path('vUpdate/<int:pk>/',views.TaskUpdate.as_view(),name='vUpdate'),
    path('vDelete/<int:pk>/',views.TaskDelete.as_view(),name='vDelete'),
]
