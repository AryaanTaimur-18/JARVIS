import inspect

from tools.registry import registry


def tool(
    name,
    description,
    direct_response=False
):

    def decorator(func):

        signature = inspect.signature(func)

        parameters = {}

        for parameter in signature.parameters.values():
            parameters[parameter.name] = "string"

        registry.register(
            {
                "name": name,
                "description": description,
                "function": func,
                "parameters": parameters,
                "direct_response": direct_response,
            }
        )

        return func

    return decorator