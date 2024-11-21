from rest_framework import serializers
from songs.models import Songs, Playlist, Download


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'
        read_only_fields = ('id',)


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = '__all__'
        read_only_fields = ('id',)

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        # read_only_fields = ('id',)
