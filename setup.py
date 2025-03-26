from setuptools import setup, Extension, find_packages

# Define the C extension
guidedlda_extension = Extension(
    'guidedlda._guidedlda',
    sources=[
        'guidedlda/_guidedlda.c',
        'guidedlda/gamma.c',
    ]
)

# Setup function
setup(
    name='guidedlda',
    version='2.0',
    description='Topic modeling with Guided latent Dirichlet allocation',
    long_description=open('README.rst').read(),
    author='Vikash Singh',
    author_email='vikash.duliajan@gmail.com',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
    ],
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    ext_modules=[guidedlda_extension],
    setup_requires=['setuptools>=61.0', 'wheel'],
)