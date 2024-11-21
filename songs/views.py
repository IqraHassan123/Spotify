from rest_framework import filters
from .models import Songs, Playlist
from .serializers import SongsSerializer, PlayListSerializer
from django.http import Http404, FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Songs, Download
from django.contrib.auth.models import User
import os

class SongView(APIView):
    filter_backends = [filters.SearchFilter]
    field_search=['category']

    search_fields = ('title', 'artist')
    def get(self, request):
        song = Songs.objects.all()
        serializer = SongsSerializer(song, many=True)
        return Response(serializer.data)


    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [IsAuthenticated(), IsArtist(), IsDistributor(), IsRecordLabel()]
    #     elif self.request.method == 'GET':
    #         return [AllowAny()]
    #     return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class DownloadSongView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            # Get the song by primary key (UUID)
            song = Songs.objects.get(pk=pk)

            # Check if the song file exists
            file_path = song.audio.path
            if not os.path.exists(file_path):
                raise Http404("File not found")

            # Create a download record for the user (if authenticated)
            if request.user.is_authenticated:
                download_quality = request.GET.get('quality', 'medium')  # Default to 'medium'
                download_record = Download.objects.create(
                    user=request.user,
                    song=song,  # Set the song here directly
                    quality=download_quality
                )
                download_record.save()

            # Create a FileResponse to return the audio file
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Type'] = 'audio/mpeg'  # Adjust according to file type (e.g., .mp3)
            response['Content-Disposition'] = f'attachment; filename="{song.title}.mp3"'

            return response

        except Songs.DoesNotExist:
            return Response({'detail': 'Song not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class PlaylistListCreateAPIView(APIView):
    def get(self, request):
        playlists = Playlist.objects.all()
        serializer = PlayListSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
