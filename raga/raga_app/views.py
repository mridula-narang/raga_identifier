from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Audio

# Create your views here.
class IndexView(View):
    def get(self, request):
        audio = Audio.objects.order_by("-uploaded_date")
        return render(
            request,
            "raga_app/index.html",
            {
                "audio":audio,
            }
        )
    
# class AudioDetailView(View):
#     def get(self, request, audio_id):
#         audio = get_object_or_404(Audio, pk=audio_id)
#         return render(
#             request,
#             "raga_app/audio.html",
#             {
#                 "audio": audio,
#             }
#         )