import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zeus-mcmc",
    version="0.6",
    author="Minas Karamanis",
    author_email="minaskar@gmail.com",
    description="zeus: The Python general-purpose MCMC sampler based on Ensemble Slice Sampling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/minaskar/zeus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'scipy', 'tqdm'],
    python_requires='>=3.6',
)