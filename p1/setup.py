from setuptools import find_packages, setup

package_name = 'p1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shanmu',
    maintainer_email='shanmu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "test_node = p1.1:main",
            "draw_circle = p1.circle:main",
            "posesub=p1.sub:main",
            "tctrl=p1.tctrl:main"
        ],
    },
)
