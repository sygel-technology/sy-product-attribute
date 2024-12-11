import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-product-attribute",
    description="Meta package for sygel-technology-sy-product-attribute Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-product_name_with_attributes>=16.0dev,<16.1dev',
        'odoo-addon-product_old_migration_fields>=16.0dev,<16.1dev',
        'odoo-addon-product_search_category_attribute>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
