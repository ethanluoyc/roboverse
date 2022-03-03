import fnmatch
import os
from setuptools import setup, find_packages


def find_data_files(package_dir, patterns, excludes=()):
    """Recursively finds files whose names match the given shell patterns."""
    paths = set()

    def is_excluded(s):
        for exclude in excludes:
            if fnmatch.fnmatch(s, exclude):
                return True
        return False

    for directory, _, filenames in os.walk(package_dir):
        if is_excluded(directory):
            continue
        for pattern in patterns:
            for filename in fnmatch.filter(filenames, pattern):
                # NB: paths must be relative to the package directory.
                relative_dirpath = os.path.relpath(directory, package_dir)
                full_path = os.path.join(relative_dirpath, filename)
                if not is_excluded(full_path):
                    paths.add(full_path)
    return list(paths)


setup(
    name='roboverse',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'roboverse': find_data_files(
            'roboverse', ['*.xacro', '*.png', '*.urdf', '*.stl', '*.xml', "assets/**/*.py", "*.bullet", "metadata.py", "*.obj", "*.txt", "*.jpg", "*.mtl", "*.mrl", "*.binvox", "*.json", "*.wrl"]
        )
    },
)
