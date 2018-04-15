import os
from pathlib import Path
from convert import convert_R_to_python
from plot_mathart import plot

def run_all():
    pathlist = Path('R').glob('**/*.R')
    for path in pathlist:
        try:
            filename = str(path)[2:]
            if filename in ['utils.R']:
                pass
            else:
                function = filename.split('.')[0]
                convert_R_to_python(function)
                if 'butterfly' in function:
                    plot(function, circles=False)
                elif function in ['stork', 'parrot', 'magpie']:
                    plot(function, circles=False)
                else:
                    plot(function)
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    run_all()