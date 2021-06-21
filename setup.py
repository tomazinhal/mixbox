import setuptools

setuptools.setup(
    name='mixbox',
    packages=setuptools.find_packages(exclude=['tests*']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mixbox = mixbox:code',
        ],
    }
)
