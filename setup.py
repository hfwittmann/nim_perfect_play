from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
            return f.read()

setup(name='nim_perfect_play',
      version='0.0.1',
      description='Perfect play for the game of nim',
      long_description=readme(),
      install_requires=['markdown'],
      packages=find_packages(),
      license='MIT',
      author='H. Felix Wittmann',
      author_email='hfwittmann@gmail.com',
      test_suite='nose.collector',
      tests_require='nose',
      entry_points={
        'console_scripts': ['nim-game=nim_perfect_play.command_line:main']
      })
