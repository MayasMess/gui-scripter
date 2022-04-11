import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gui-scripter",
    version="1.0.2",
    author="Amayas Messara",
    author_email="amayas.messara@gmail.com",
    description="Simple GUI for Python Scripts",
    install_requires=["altgraph", "macholib", "Pillow", "ttkthemes"],
    keywords=["gui", "scripts", "simple gui", "python gui"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MayasMess/gui-scripter/issues",
    project_urls={
        "Bug Tracker": "https://github.com/MayasMess/pandas-oop/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)