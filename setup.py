"""The setup script."""

from setuptools import setup, find_packages

with open('README.md',encoding='UTF-8') as readme_file:
    readme = readme_file.read()

with open('requirements.txt',encoding='UTF-8') as f:
    requirements = f.read().splitlines()


setup_requirements = [ ]
__version__='0.1.0'

test_requirements = ['pytest','pytest-mock','pytest-cov' ]

if __name__ == "__main__":
    setup(
        description='El objetivo es la intervención del proceso de control a la valoración de las unidades de fondos  enfocado en la generación',
        author='ERAMIREG',
        author_email='eramirez@3htp.com',
        classifiers=[
            'Development Status :: Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.9',
        ],
        install_requires=requirements,
        license='BSD-3-Clause',
        long_description=readme,
        include_package_data=True,
        keywords='ci-345_controles-valores-de-unidad-de-fondo',
        name='ci-345_controles-valores-de-unidad-de-fondo',
        packages=find_packages(where='src'),
        package_dir={"": "src"},
        setup_requires=setup_requirements,
        test_suite='pytest',
        extras_require={
            "tests": test_requirements,
        },
        url='',
        version=__version__,
        zip_safe=False,
)

