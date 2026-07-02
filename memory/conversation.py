class ConversationMemory:
    """
    Stores the current conversation history.
    """

    def __init__(self):

        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are JARVIS, a helpful AI assistant. "
                    "Be friendly, concise, and conversational."
                ),
            }
        ]

    def add_user_message(self, message):

        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_assistant_message(self, message):

        self.messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def get_messages(self):

        return self.messages

    def clear(self):

        self.messages = self.messages[:1]