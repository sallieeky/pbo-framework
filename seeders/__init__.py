import pkgutil
import re


def seed():
    __all__ = []
    query = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module
        getattr(_module, module_name)().seed()


def make_seeder(file_name):
    if "seeder" not in file_name.capitalize():
        file_name = file_name.capitalize() + "Seeder"
    model = re.split('seeder', file_name.capitalize())[0]

    with open('default/seeder.py', 'r') as reader:
        with open(f'seeders/{file_name}.py', 'w') as writer:
            for line in reader:
                if 'from models.ClassName import ClassName' in line:
                    line = line.replace('from models.ClassName import ClassName',
                                        f'from models.{model} import {model}')
                if 'class ClassName:' in line:
                    line = line.replace('class ClassName:',
                                        f'class {file_name}:')
                if 'self.model = ClassName()' in line:
                    line = line.replace('self.model = ClassName()',
                                        f'self.model = {model}()')

                writer.write(line)
