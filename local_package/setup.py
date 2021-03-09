from setuptools import setup

setup(name='my_local_package',
      packages=['my_local_package'],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['cool-cmd=cool_lib.__main__:main'],
      }
)
