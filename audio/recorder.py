import sounddevice as sd
import soundfile as sf
from pathlib import Path


class AudioRecorder:
    """
    Handles microphone recording.
    """

    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

        self.output_folder = Path("data/recordings")
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def record(self, duration=5, filename="recording.wav"):
        print(f"\n🎤 Recording for {duration} seconds...")
        print("Speak now...\n")

        recording = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        file_path = self.output_folder / filename

        sf.write(file_path, recording, self.sample_rate)

        print("✅ Recording saved!")

        return file_path