import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-product-attribute",
    description="Meta package for sygel-technology-sy-product-attribute Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-product_lst_price_calculate>=15.0dev,<15.1dev',
        'odoo-addon-product_name_with_attributes>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
