
from django.urls import re_path, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .endpoints import board, task, team, todo, worker

schema_view = get_schema_view(
   openapi.Info(
      title="Trello API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('task-list/', task.get_task_list),
    path('task-detail/<str:pk>/', task.get_task_detail),
    path('task-create/', task.post_task_create),
    path('task-update/<str:pk>', task.post_task_update),
    path('task-delete/<str:pk>', task.delete_task_delete),

    path('todo-list/', todo.get_todo_list),
    path('todo-detail/<str:pk>/', todo.get_todo_detail),
    path('todo-create/', todo.post_todo_create),
    path('todo-update/<str:pk>', todo.post_todo_update),
    path('todo-delete/<str:pk>', todo.delete_todo_delete),

    path('team-list/', team.get_team_list),
    path('team-detail/<str:pk>/', team.get_team_detail),
    path('team-create/', team.post_team_create),
    path('team-update/<str:pk>', team.post_team_update),
    path('team-delete/<str:pk>', team.delete_team_delete),

    path('worker-list/', worker.get_worker_list),
    path('worker-detail/<str:pk>/', worker.get_worker_detail),
    path('worker-create/', worker.post_worker_create),
    path('worker-update/<str:pk>', worker.post_worker_update),
    path('worker-delete/<str:pk>', worker.delete_worker_delete),

    path("postallboards/", board.post_all_boards),
    path("posttaskaddteam/<str:pk>/", task.post_task_add_team),
]