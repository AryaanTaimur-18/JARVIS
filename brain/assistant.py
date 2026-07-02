from audio.recorder import AudioRecorder
from audio.transcriber import AudioTranscriber
from audio.speaker import Speaker
from brain.llm import LLM
from memory.conversation import ConversationMemory


class JarvisAssistant:
    """
    Main controller of the assistant.
    """

    def __init__(self):

        print("Initializing JARVIS...\n")

        self.recorder = AudioRecorder()
        self.transcriber = AudioTranscriber()
        self.speaker = Speaker()
        self.llm = LLM()
        self.memory = ConversationMemory()

        print("JARVIS is ready!\n")

    def listen_once(self):

        input("Press Enter to start recording...")

        audio = self.recorder.record()

        text = self.transcriber.transcribe(audio)

        self.memory.add_user_message(text)

        print(f"\nYou said: {text}\n")

        print("Thinking...\n")

        response = self.llm.chat(
        self.memory.get_messages()
        )

        print(f"JARVIS: {response}\n")

        self.memory.add_assistant_message(response)

        self.speaker.speak(response)
    
    def run(self):

        print("JARVIS is now listening... (Press Ctrl+C to stop)\n")

        try:
            while True:
                self.listen_once()

        except KeyboardInterrupt:
            print("\n\nShutting down JARVIS...")