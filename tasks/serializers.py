from taskP.tasks.models import Task

from rest_framework.serializers import ModelSerializer


class TaskSerializer(ModelSerializer):


    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
        )
