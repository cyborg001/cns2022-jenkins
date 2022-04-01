from .base import *

env_name = os.getenv('ENV_NAME', 'production')

if env_name == 'production':
    print('production******************************')
    from .production import *
elif env_name == 'stage':
    from .stage import *
else:
    print('local***************************')
    from .local import *