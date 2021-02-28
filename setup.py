import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='spens',
    version='1.0.0',
    packages=setuptools.find_packages(),
    license='MIT',
    description='Load an ascii .spe file as a numpy array.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy'],
    python_requires='>=3.6',
    url='https://github.com/agdelma/spe',
    author='Adrian Del Maestro',
    author_email='adrian@delmaestro.org',
    classifiers=[
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3.6',
   'Programming Language :: Python :: 3.7',
   'Topic :: Scientific/Engineering :: Physics']
)
