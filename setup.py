from pathlib import Path
from setuptools import setup, find_packages


with open('./README.md', 'r') as ff:
    readme_text = ff.read()

# Parse version
init = Path(__file__).parent / "sphinx_toggleprompt" / "__init__.py"
version = None
for line in init.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break
if version is None:
    raise ValueError('No version found')

setup(
    name='sphinx-toggleprompt',
    version=version,
    description="Add a python prompt toggle to each code cell.",
    long_description=readme_text,
    long_description_content_type='text/markdown',
    author='Michael Jurasovic',
    url="https://github.com/jurasofish/sphinx-toggleprompt",
    license='MIT License',
    packages=find_packages(),
    package_data={'sphinx_toggleprompt': ['_static/toggleprompt.js_t']},
    classifiers=["License :: OSI Approved :: MIT License"],
    install_requires=[
        "sphinx>=1.8"
    ]
)
