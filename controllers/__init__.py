import pkgutil
import re


def controller(controller, method, data={}):
    __all__ = []
    result = False
    try:
        for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
            _module = loader.find_module(controller).load_module(controller)
            globals()[controller] = _module
            className = getattr(_module, f"{controller}")
            for func in dir(className):
                if '__' not in func:
                    result = getattr(className(), method)(data)
    except:
        print("Nama controller dan method harus sesuai")
    return result


def make_controller(file_name):
    if "controller" not in file_name.capitalize():
        file_name = file_name.capitalize() + "Controller"
    with open('default/controller.py', 'r') as reader:
        with open(f'controllers/{file_name}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName:' in line:
                    line = line.replace('class ClassName:',
                                        f'class {file_name}:')
                writer.write(line)
