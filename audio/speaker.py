import asyncio
from pathlib import Path

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

        output_file = self.output_folder / "speech.mp3"

        asyncio.run(
            self._generate(text, output_file)
        )

        pygame.mixer.music.load(str(output_file))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)