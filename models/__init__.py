def make_model(file_name):
    with open('default/model.py', 'r') as reader:
        with open(f'models/{file_name.capitalize()}.py', 'w') as writer:
            for line in reader:
                if 'class ClassName(Model):' in line:
                    line = line.replace('class ClassName(Model):',
                                        f'class {file_name.capitalize()}(Model):')
                writer.write(line)
