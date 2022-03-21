from setuptools import setup, find_packages
def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='simple_rest',
      version='1.0',
      description='a simple rest app to return value for a requested key',
      packages=find_packages(),
      long_description = readme(),
      classifiers = [
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux'
      ],
      url='https://github.com/Fonseca-Rafael/simple_rest.git',
      author='Rafael da Fonseca',
      author_email='rafaelmfonseca@gmail.com',
      install_requires = ['fastapi', 
                          'typing', 
                          'uvicorn', 
                          'starlette'],
      test_suite='nose.collector',
      tests_require=['nose-py3'],
      zip_safe=False,
      include_package_data=True)
