import inspect

from tools.registry import registry


def tool(
    name,
    description,
    parameters=None,
    direct_response=False
):

    def decorator(func):

        detected_parameters = parameters

        if detected_parameters is None:

            signature = inspect.signature(func)

            detected_parameters = {}

            for parameter in signature.parameters.values():

                if parameter.name == "self":
                    continue

                detected_parameters[parameter.name] = {
                    "type": "string"
                }

        registry.register(
            {
                "name": name,
                "description": description,
                "function": func,
                "parameters": detected_parameters,
                "direct_response": direct_response
            }
        )
        return func

    return decorator