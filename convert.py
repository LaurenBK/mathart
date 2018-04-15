import re
import argparse

def convert_R_to_python(name, location = 'R/'):
    if '.R' in name:
        path = f'{name}'
        name = path.split('.')[0]
    else:
        path = f'{location}{name}.R'
    with open(path,'r') as r_file:
        text_pieces = r_file.read()

    final_text = 'import numpy as np\n\n'


    text_pieces = text_pieces.split('%>%')

    text = text_pieces[0]
    numbers = re.findall(r'\d+', text)
    n = text.find('n =')
    text = text.replace(text[:n], f'def {name}(')
    text = text.replace(') {', '):')
    if 'k = 1:n)' in text:
        text = text.replace('data.frame(', '  k = np.arange(')
        text = text.replace('k = 1:n)', f'1,{numbers[0]})\n')
        text += '   data = [[]] * len(k)'
    elif 'seq' in text:
        text = text.replace('data.frame(t = seq(', '  t = np.arange(')
        text = text.replace(f'pi', f'np.pi')
        text = text = text[:-2]

    final_text += text

    text = text_pieces[1]
    text = text[2:]
    for i in ['dplyr::mutate(', ',']:
        text = text.replace(f'{i}', '')
    for i in ['cos', 'sin', 'pi', 'exp']:
        text = text.replace(f'{i}', f'np.{i}')
    for i in ['x', 'y', 'r']:
        text = text.replace(f'  {i}', f'{i}')
    for i in range(10):
        text = text.replace(f'{i}/', f'{i}.0/')
    text = text.replace('^', '**')
    text = text[:-2]

    final_text += text
    if 'r =' in final_text:
        final_text += 'data =  [x, y, r]\n'
    elif 'x_end =' in final_text:
        final_text += 'data =  [x, y, x_end, y_end]\n'
    else:
        final_text += 'data =  [x, y]\n'
    final_text += '    data = np.array(data).T\n'
    final_text += '    return(data)\n'

    path = f'python_functions/{name}.py'
    with open(path, 'w') as p_file:
        p_file.write(final_text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='Name of file to convert to python')
    args = parser.parse_args()

    convert_R_to_python(args.filename)
