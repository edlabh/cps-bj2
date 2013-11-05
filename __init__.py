from .main import BJ2

def start():
    return BJ2()

config = [{
    'name': 'bj2me',
    'groups': [
        {
            'tab': 'searcher',
            'subtab': 'providers',
            'list': 'torrent_providers',
            'name': 'BJ2',
            'description': 'See <a href="http://www.bj2.me">bj2.me 2.0</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
