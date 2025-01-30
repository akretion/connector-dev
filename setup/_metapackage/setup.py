import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-akretion-connector-dev",
    description="Meta package for akretion-connector-dev Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-connector_dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
