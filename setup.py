from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="proxy-auto-config",
    version="1.0.0",
    author="MaiiNor",
    author_email="maiinor@users.noreply.github.com",
    description="智能代理自动检测和配置工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaiiNor/proxy-auto-config",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: Proxy Servers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8+",
    ],
    python_requires=">=3.8",
)
