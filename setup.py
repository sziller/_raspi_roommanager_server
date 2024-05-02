#!/usr/bin/python3.10
"""
setup function to be run when creating packages for ChainRecorder Engine
command to be typed in:
python setup.py sdist # bdist_wheel
"""

from setuptools import setup


NAME = "RaspiRoommanager"

PROJECT_PATH = "Projects/"
GEN_PACKAGES_PATH = PROJECT_PATH + "001_GeneralAssistance/GeneralCoding/Python/general_package_development"
HAT_PACKAGES_PATH = PROJECT_PATH + "900_Raspberry/_general_packages/SenseHat"

INSTALL_REQUIRES = [
    "pytest",
    "sqlalchemy",
    "pyaml"
    "uvicorn"
    "fastapi"
    "raspiroommanage @ http://sziller.eu/{}/sensehat_led_clock/dist/sensehat_led_clock-0.0.0-py3-none-any.whl"
    .format(HAT_PACKAGES_PATH)]

# 'ExampleRepo @ git+ssh://git@github.com/example_org/ExampleRepo.git'

print("--" + "-"*30 + "--",)
print("- {:^30} -".format(NAME))
print("--" + "-"*30 + "--",)
print("- {:^30} -".format("INSTALL_REQUIRES"))
print("--" + "-"*30 + "--",)
for _ in INSTALL_REQUIRES:
    print(_)
print("--" + "-"*30 + "--")


setup(
    name='room_server',  # package name, used at pip or tar.
    version='0.0.0',  # version Nr.... whatever
    packages=["shmc_routers"],  # string list of packages to be translated
    include_package_data=True,
    url='',  # if url is used at all
    license='',  # ...
    author='sziller',  # well obvious
    author_email='szillerke@gmail.com',  # well obvious
    description='ServerPackage Room',  # well obvious
    install_requires=[], # ATTENTION! Wheel file needed, depending on environment
    dependency_links=[],  # if dependent on external projects
)
