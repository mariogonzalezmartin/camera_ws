from setuptools import find_packages, setup

package_name = 'opencv_tools'

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
    maintainer='desktop',
    maintainer_email='desktop@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = opencv_tools.webcam_pub:main',
      'img_subscriber = opencv_tools.webcam_sub:main',
        ],
    },
)
