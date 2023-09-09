from os import path as os_path

from setuptools import setup, find_packages

from easy_spider_tool import __version__

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


if __name__ == '__main__':
    setup(
        name='easy_spider_tool',  # 包名
        python_requires='>=3.6.8',  # python环境
        version=__version__,  # 包的版本
        description="简易、好用的爬虫工具,减少重复代码与文件冗余",  # 包简介，显示在PyPI上
        long_description=read_file('README.md'),  # 读取的Readme文档内容
        long_description_content_type="text/markdown",  # 指定包文档格式为markdown
        author="hanxinkong",  # 作者相关信息
        author_email='xinkonghan@gmail.com',
        url='https://easy-spider-tool.xink.top/',
        packages=find_packages(),
        install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
        license="MIT",
        keywords=['easy', 'spider', 'tool'],
    )
