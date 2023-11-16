from os import getcwd
from pathlib import Path
from setuptools import setup, find_packages

__version__ = '0.0.1'

def get_requirements(req_file):
    # print('--- executing setup.py ---')
    with open(req_file) as f:
        packages = []
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):  # ignore empty lines and comments
                continue
            elif '--extra-index-url' in line:
                continue
            elif line.startswith('-r'):
                new_req_file = line.split(' ')[1]
                _path = Path(req_file).parent
                if _path is None:
                    path = ''
                new_packages = get_requirements(Path(_path, new_req_file))
                packages += new_packages
            else:
                packages.append(line)
    return packages
setup(
    name='yolor_fork_paper',  # How you named your package folder (MyLib)
    packages=find_packages(),  # list all packages in setup, including subpackages
    version=__version__,  # Start with a small number and increase it with every change you make
    license='UNLICENSED',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    private=True,
    # package_data={
    #     'ab_autotagging_lanes': [
    #         'conf/*',
    #         'single_frame_model_assets/*'
    #     ]
    # },
    include_package_data=False,  # True,
    description='Yolor fork, paper branch',  # Give a short description about your library
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: None',
        'Topic :: Software Development :: AI',
        'Programming Language :: Python :: 3.10'
    ]
)
