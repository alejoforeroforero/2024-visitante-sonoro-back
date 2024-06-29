import os
from django.core.exceptions import ValidationError
from mutagen import File as MutagenFile
from mutagen.wave import WAVE

def validate_audio_file(value):
    # Validate the file extension
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.wav', '.mp3', '.ogg', '.flac']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported file extension.')

    # Validate the file content
    try:
        audio = MutagenFile(value)
        if audio is None:
            raise ValidationError('File is not a valid audio file.')
    except Exception as e:
        raise ValidationError('Error occurred while validating the audio file: ' + str(e))
