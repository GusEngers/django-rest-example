from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

