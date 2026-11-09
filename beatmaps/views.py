from pathlib import Path

from django.shortcuts import render, redirect
from .models import Beatmap

from django.conf import settings
from django.http import FileResponse, Http404


# Display beatmaps on the homepage
def home(request):
    beatmaps = Beatmap.objects.all()

    return render(request, "index.html", {
        "beatmaps": beatmaps
    })


# Display the upload page and process uploads
def upload(request):

    if request.method == "POST":

        # Get information from the HTML form
        title = request.POST.get("title", "").strip()
        artist = request.POST.get("artist", "").strip()
        instrument = request.POST.get("instrument", "")
        difficulty = request.POST.get("difficulty", "")
        file = request.FILES.get("beatmap_file")

        # Require all necessary fields
        if not all([title, artist, instrument, difficulty, file]):
            return render(request, "upload.html", {
                "error": "Please complete all required fields."
            })

        # Check file extension and size
        extension = Path(file.name).suffix.lower()
        allowed_formats = {
            ".mid": "MIDI",
            ".midi": "MIDI",
            ".xml": "MusicXML",
            ".musicxml": "MusicXML",
        }

        if extension not in allowed_formats or file.size > 10 * 1024 * 1024:
            return render(request, "upload.html", {
                "error": "Upload a MIDI or MusicXML file under 10 MB."
            })

        if instrument not in ["piano", "guitar", "drums", "violin", "other"]:
            return render(request, "upload.html", {
                "error": "Invalid instrument."
            })

        if difficulty not in ["1", "2", "3", "4", "5"]:
            return render(request, "upload.html", {
                "error": "Invalid difficulty."
            })

        # Save beatmap information and the uploaded file
        Beatmap.objects.create(
            title=title,
            artist=artist,
            instrument=instrument,
            file_format=allowed_formats[extension],
            difficulty=int(difficulty),
            file=file
        )

        # Return to homepage after successful upload
        return redirect("home")

    return render(request, "upload.html")

# Display the download page
def download(request):
    return render(request, "download.html")


# Download the Mediverse game
def download_game(request):
    game_path = settings.BASE_DIR / "game_files" / "Mediverse.zip"

    if not game_path.is_file():
        raise Http404("Game file not found.")

    return FileResponse(
        open(game_path, "rb"),
        as_attachment=True,
        filename="Mediverse.zip"
    )