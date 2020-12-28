from .base import *

env = os.getenv('ENV')

if env == 'local':
    from .local import *
else:
    from .prod import *
