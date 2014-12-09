import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


install_requires = [
    'Django==1.6.8',
    'raven==5.1.1',
    'six==1.8.0',
    'django-push==0.6.1',
    'Pillow==2.6.1',
    'South==1.0.1',
    'dj-database-url==0.3.0',
    'django-classy-tags==0.5.1',
    'django-cms==3.0.7',
    'django-debug-toolbar==1.2.2',
    'django-easyconfig==0.1',
    'django-mptt==0.6.1',
    'django-reversion==1.8.5',
    'django-sekizai==0.7',
    'djangocms-admin-style==0.2.4',
    'djangocms-column==1.5',
    'djangocms-file==0.1',
    'djangocms-flash==0.1',
    'djangocms-googlemap==0.2',
    'djangocms-inherit==0.1',
    'djangocms-installer==0.5.4',
    'djangocms-link==1.5',
    'djangocms-picture==0.1',
    'djangocms-style==1.5',
    'djangocms-teaser==0.1',
    'djangocms-text-ckeditor==2.4.1',
    'djangocms-video==0.1',
    'html5lib==1.0b3',
    'pytz==2014.10',
    'requests==2.5.0',
]

dev_requires = [
    'django-debug-toolbar==1.2.2',
]

tests_require = [
]


setup(
    name='djangofr',
    version='1.0.0',
    author='Xavier Ordoquy',
    url='http://www.django-fr.org/',
    packages=find_packages('.', exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
        'dev': install_requires + dev_requires,
    },
    tests_require=tests_require,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
    ],
)
