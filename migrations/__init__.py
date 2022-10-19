import pkgutil
import re


def migrate():
    __all__ = []
    query = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module
        if module_name != "schema":
            className = re.split('_', module_name)
            query.append(getattr(_module, f"{className[0].capitalize()}{className[1].capitalize()}{className[2].capitalize()}")
                         ().create(className[1].lower()))
    return query


def drop():
    __all__ = []
    query = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module
        if module_name != "schema":
            className = re.split('_', module_name)
            query.append(getattr(_module, f"{className[0].capitalize()}{className[1].capitalize()}{className[2].capitalize()}")
                         ().drop(className[1].lower()))
    return query


def fresh():
    query = {
        "drop": drop(),
        "migrate": migrate()
    }
    return query


def make_migration(file_name):
    if "migration" not in file_name.capitalize():
        file_name = "create_" + file_name.lower() + "_table"
    className = re.split('_', file_name)
    with open('default/migration.py', 'r') as reader:
        with open(f'migrations/{file_name}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName(Schema):' in line:
                    line = line.replace('class ClassName(Schema):',
                                        f'class {className[0].capitalize()}{className[1].capitalize()}{className[2].capitalize()}(Schema):')
                writer.write(line)
