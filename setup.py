from setuptools import setup
from setuptools import find_packages


setup(name='KnowledgeBasedRanking',
      version='0.00',
      description='knowledge based ranking',
      author='Chenyan Xiong',
      install_requires=['scikit-learn', 'sklearn', 'numpy', 'scipy', 'traitlets', 'six',
                        'google-api-python-client', 'elasticsearch', 'nltk', 'keras',
                        'gensim',
                        ],
      packages=find_packages()
      )