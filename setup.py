from setuptools import setup, find_packages


version = '0.1.dev0'

setup(
    name='collective.jquery.backstretch',
    version=version,
    description='',

    author='Franklin Kingma <franklin@fourdigits.nl>',
    author_email='franklin@fourdigits.nl',

    license='GPL',
    url='https://github.com/kingel/collective.jquery.backstretch/',
    keywords='plone jquery backstretch',
    classifiers=[],
    namespace_packages=['collective', 'collective.jquery'],
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'distribute',
        ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
