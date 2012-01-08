from distutils.core import setup

setup(
    name='django-amf-mediagate',
    version='0.1.0',
    author='Mike Robinson',
    author_email='mike.robinson.81@gmail.com',
    packages=['mediagate',],
    url='http://github.com/mike360/django-amf-mediagate/',
    license='BSD',
    description='A wrapper app for PyAMF to provide a gateway for sending media files to Flash apps.',
    long_description=open('README').read(),
    install_requires=[
        "Django >= 1.2",
        "PyAMF == 0.6.1",
    ],
)