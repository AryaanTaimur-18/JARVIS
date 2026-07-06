from tools.registry import registry


class OpenAIToolAdapter:
    """
    Converts our internal registry
    into the OpenAI/LM Studio tool format.
    """

    def export(self):

        tools = []

        for tool in registry.all().values():

            properties = {}
            required = []

            for parameter in tool["parameters"]:

                properties[parameter] = {
                    "type": "string"
                }

                required.append(parameter)

            tools.append({

                "type": "function",

                "function": {

                    "name": tool["name"],

                    "description": tool["description"],

                    "parameters": {

                        "type": "object",

                        "properties": properties,

                        "required": required

                    }

                }

            })

        return tools