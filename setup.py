from setuptools import setup, find_packages

setup(
    name = 'qtheory',
    version = '1.0.0',
    author = 'Joao Ricardo Core Dutra',
    author_email = 'jrdutra.com.br@gmail.com',
    packages = find_packages(),
    install_requires=[
          'numpy',
          'scipy',
          'pandas',
      ],
    description = 'Library for queuing theory calculation',
    long_description = 'It is a Python library implementing the Queueing theory calculations. '
    + 'As my term paper, I am developing a library, '
    + 'implementing the calculus of queuing theory. '
    + 'This library has the objective of characterising some queuing theory params '
    + 'as the queue arrival rate of clients, attendance rate and others... '
    + 'Implementing in python, this library receives a input file '
    + 'with queue data and gives the output answers. For the undergraduate thesis, '
    + 'I had toke some datas in a real queue and submited to the library as a input, '
    + 'to validate this project.',
    url = 'https://github.com/jrdutra/qtheory',
    project_urls = {
        'Código fonte': 'https://github.com/jrdutra/qtheory',
        'Download': 'https://github.com/jrdutra/qtheory'
    },
    license = 'MIT',
    keywords = 'queue queueing theory',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Mathematics'
    ]
)