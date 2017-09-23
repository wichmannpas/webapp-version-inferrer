from backends.software_package import SoftwarePackage
from definitions.definition import SoftwareDefinition
from providers.git import GitTagProvider


class Magento(SoftwareDefinition):
    software_package = SoftwarePackage(
        name='Magento Open Source',
        vendor='Magento Inc.')
    provider = GitTagProvider(
        software_package=software_package,
        url='https://github.com/magento/magento2.git'
    )
    path_map = {
        '/': '/',
    }
    ignore_paths = None