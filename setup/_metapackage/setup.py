import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-product-attribute",
    description="Meta package for sygel-technology-sy-product-attribute Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-product_name_with_country',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
