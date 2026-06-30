from faster_whisper import WhisperModel
from pathlib import Path


class AudioTranscriber:
    """
    Converts speech into text using Faster Whisper.
    """

    def __init__(self, model_size="base"):
        print("Loading Whisper model... (first time may take a few minutes)")

        self.model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )

        print("Whisper model loaded successfully!")

    def transcribe(self, audio_path: Path):

        segments, info = self.model.transcribe(
            str(audio_path),
            beam_size=5
        )

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()