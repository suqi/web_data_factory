# Windows搭建Python开发环境

## 命令行工具  
- 神器：cmder  （https://github.com/cmderdev/cmder/releases/download/v1.2.9/cmder.7z）
- 用不了的话，用 ConEmu
- 尽量不要使用自带命令行，体验不好

## 安装Python
- 下载2.7.11版本，注意不要下载3.5版本 (https://www.python.org/getit/)
- 环境变量设置：我的电脑-->属性-->高级-->环境变量-->用户变量 中添加PATH，设置值为PATH; c:\python27
- 环境变量设置好了，就可以在命令行cmder里，输入python即可打开python交互式解释器了，玩一玩吧
- python自带包管理工具，可以通过pip install下载各种包
- 安装重要的包： 
    - pip install virtualenvwrapper-win
    - pip install pyreadline
    - pip install ipython
- 现在你在cmder里输入ipython命令，绚烂的iPython交互式界面就在你的眼前，随便你玩吧

##  爬虫相关的包
- 需要安装VC++编译工具： http://www.microsoft.com/en-us/download/details.aspx?id=44266
- 先安装一个基础库
    - 下载 http://www.lfd.uci.edu/~gohlke/pythonlibs/3kgubn3j/lxml-3.5.0-cp27-none-win32.whl
    - 在命令行 用 `cd` 命令 切换到下载目录
    - 然后 pip install lxml-3.5.0-cp27-none-win32.whl
- 再安装一个基础库
    - 下载并运行（注意64位请选择amd64的版本） http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download
    - 提示：如果用了虚拟环境，请注意，要切换到下载目录，并easy_install这个exe，才行
- pip install scrapy
- pip install requests
- pip install BeautifulSoup4
- 现在你可以尝试玩一玩scrapy了，输入scrapy.exe的命令试试


## 开发工具
- PyCharm 集成开发工具
    - 这个开发工具无比强大
    - 下载Professional版本 http://www.jetbrains.com/pycharm/download/)  可以试用30天
- 代码编辑器
    - 偶尔想打开一个文件快速看看，就用一个轻量的编辑器
    - Sublime Text 3  (http://www.sublimetext.com/3) 非常轻巧快速，插件强大