from setuptools import setup, find_packages

setup(
    name='easy_spider_tool',
    version='1.0.07',
    packages=find_packages(),
    license='MIT',
    author='hanxinkong',
    author_email='xinkonghan@gmail.com',
    description='简易、好用的爬虫工具,减少重复代码与文件冗余',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        # List your package's dependencies here
        "dateparser>=1.1.3",
        "jsonpath>=0.82",
        "pytz>=2023.3"
    ],
)
