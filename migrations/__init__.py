import pkgutil


def migrate():
    __all__ = []
    query = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module
        if module_name != "schema":
            query.append(getattr(_module, module_name)
                         ().create(module_name.lower()))
    return query


def drop():
    __all__ = []
    query = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module
        if module_name != "schema":
            query.append(getattr(_module, module_name)
                         ().drop(module_name.lower()))
    return query


def fresh():
    query = {
        "drop": drop(),
        "migrate": migrate()
    }
    return query


def make_migration(file_name):
    with open('default/migration.py', 'r') as reader:
        with open(f'migrations/{file_name.capitalize()}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName(Schema):' in line:
                    line = line.replace('class ClassName(Schema):',
                                        f'class {file_name.capitalize()}(Schema):')
                writer.write(line)
