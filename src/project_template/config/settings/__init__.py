try:
    from .general import *  # noqa: F403
except ImportError:
    raise ImportError("A general settings file is required to run this project")

try:
    from .local import *  # noqa: F403
except ImportError:
    raise ImportError("A local settings file is required to run this project")
