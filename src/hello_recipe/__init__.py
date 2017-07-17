#coding: utf-8
import os
import sys
from pprint import pprint

class Recipe:
    """Hello Buildout Recipe

    This recipe will write arguments that passed to this recipe to a file. Search
    parts directory for the result, usually it's path will be parts/hello_recipe.
    """

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options
        options['path'] = os.path.join(buildout['buildout']['parts-directory'], name)

    def install(self):
        self.options.created(self.options['path'])
        with open(self.options['path'], 'w') as f:
            pprint('buildout'.center(20, '='), stream=f)
            pprint(self.buildout, stream=f)
            pprint('name'.center(20, '='), stream=f)
            pprint(self.name, stream=f)
            pprint('options'.center(20, '='), stream=f)
            pprint(self.options, stream=f)
            pprint('sys.argv'.center(20, '='), stream=f)
            pprint(sys.argv, stream=f)
        return self.options.created()

    update = install
