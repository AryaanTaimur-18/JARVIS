from openai import OpenAI


class LLM:
    """
    Handles communication with the local language model.
    """

    def __init__(self):

        self.client = OpenAI(
            base_url="http://127.0.0.1:1234/v1",
            api_key="lm-studio"
        )

        self.model = "qwen2.5-7b-instruct"

    def chat(self, messages):

        response = self.client.chat.completions.create(
        model=self.model,
        messages=messages,
        temperature=0.7,
        )

        return response.choices[0].message.content