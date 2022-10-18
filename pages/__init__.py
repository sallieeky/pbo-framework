import re


def make_page(file_name):
    if "page" not in file_name.capitalize():
        file_name = file_name.capitalize() + "Page"
    with open('default/page.py', 'r') as reader:
        with open(f'pages/{file_name}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName(Page):' in line:
                    line = line.replace('class ClassName(Page):',
                                        f'class {file_name}(Page):')
                writer.write(line)
