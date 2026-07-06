import asyncio
from pathlib import Path
import uuid

import edge_tts
import pygame


class Speaker:
    """
    Converts text into speech.
    """

    def __init__(
        self,
        voice="en-US-AriaNeural",
        rate="+0%"
    ):

        self.voice = voice
        self.rate = rate

        self.output_folder = Path("data/audio")
        self.output_folder.mkdir(parents=True, exist_ok=True)

        pygame.mixer.init()

    async def _generate(self, text, output_file):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.rate
        )

        await communicate.save(str(output_file))

    def speak(self, text):

        if not text:
            return

        # Generate a unique filename for every response
        output_file = self.output_folder / f"{uuid.uuid4()}.mp3"

        try:
            # Generate speech
            asyncio.run(
                self._generate(text, output_file)
            )

            # Play the audio
            pygame.mixer.music.load(str(output_file))
            pygame.mixer.music.play()

            # Wait until playback finishes
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        finally:
            # Release the file before deleting it
            try:
                pygame.mixer.music.unload()
            except Exception:
                pass

            # Delete the temporary audio file
            if output_file.exists():
                output_file.unlink()