from django.contrib.auth.models import User
from rest_framework import serializers
from project_nicolas.app_bookmarks.models import Bookmark, TYPE_CHOICES



class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff',)


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):

    site_link = serializers.CharField()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    last_active = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    last_check = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    type_name = serializers.ChoiceField(source='get_type_display', choices=TYPE_CHOICES, read_only=True)

    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'site_link', 'type', 'type_name', 'description', 'created', 'last_active', 'last_check', )
