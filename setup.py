try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setuptools

setup(
		name = 'ucast',
		version = '0.01',
		author = 'ywu',
		author_email = 'yelenamqwu@gmail.com',
		install_requires = [
			"request"
			]
	)