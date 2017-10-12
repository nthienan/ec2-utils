from pybuilder.core import use_plugin, task, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")
use_plugin("python.flake8")
use_plugin("python.pycharm")

name = "ec2-utils"
version = "1.0.0"
summary = "EC2 Utils"
authors = [
    Author("An Nguyen", "nthienan.it@gmail.com")
]

default_task = ["clean", "run_unit_tests", "analyze", "publish"]


@init
def initialize(project):
    # Also run flake8 on integrationtest and unittest sources
    project.set_property("flake8_include_test_sources", True)

    # Comma separated list of error messages to ignore. Example: "F403,W404,W801"
    project.set_property("flake8_ignore", "E402")

    # Display flake8 warnings and errors in command line output
    project.set_property("flake8_verbose_output", True)
