import inspect

from tools.registry import registry


def tool(
    name,
    description,
    parameters=None
):

    def decorator(func):

        detected_parameters = parameters

        if detected_parameters is None:

            signature = inspect.signature(func)

            detected_parameters = {}

            for parameter in signature.parameters.values():

                detected_parameters[parameter.name] = "string"

        registry.register(
            name=name,
            description=description,
            function=func,
            parameters=detected_parameters
        )

        return func

    return decorator