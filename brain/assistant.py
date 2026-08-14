from audio.recorder import AudioRecorder
from audio.transcriber import AudioTranscriber
from audio.speaker import Speaker
from brain.llm import LLM
from memory.conversation import ConversationMemory
from tools.manager import ToolManager
from tools.loader import ToolLoader
from events.event_bus import event_bus

class Assistant:
    """
    Main controller of the assistant.
    """

    def __init__(self):

        print("Initializing JARVIS...\n")

        self.recorder = AudioRecorder()
        self.transcriber = AudioTranscriber()
        self.speaker = Speaker()
        from brain.agent import Agent
        self.agent = Agent()
        self.memory = ConversationMemory()
            
        print("Loading skills...")

        self.loader = ToolLoader()
        self.loader.load()

        self.tool_manager = ToolManager()

        print("All skills loaded.")

        from tools.registry import registry

        print("\nRegistered Tools:\n")

        for tool in registry.all().values():

            print(tool["name"])

        print("JARVIS is ready!\n")

    def process(self, text):

        self.memory.add_user_message(text)

        response = self.agent.chat(
            self.memory.get_messages()
        )

        self.memory.add_assistant_message(response)

        return response
    
    def listen_once(self):

        input("Press Enter to start recording...")

        audio = self.recorder.record()

        text = self.transcriber.transcribe(audio)

        print(f"\nYou said: {text}\n")

        print("Thinking...\n")

        response = self.process(text)

        print(f"JARVIS: {response}\n")

        self.speaker.speak(response)
    
    def run(self):

        print("JARVIS is now listening... (Press Ctrl+C to stop)\n")

        try:
            while True:
                self.listen_once()

        except KeyboardInterrupt:
            print("\n\nShutting down JARVIS...")                    