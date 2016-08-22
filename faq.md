# 常见问题
> 这里列举了在实际讲授过程中遇到的问题

# 基础环境

Mac 下直接用 iTerm2命令行
Windows下用cmder

Windows下找不到pip，是因为在c:/python27/script下
cd c:/python27/script
pip即可

pip install virtualenvwrapper-win 

pip install pyreadline



# 大项目用得到的库

pip install django -i http://pypi.douban.com/simple/ 

pip install beautifulsoup4

pip install djangorestframework 

pip install scrapy

pip install requests

pip install pandas

# 在服务器上安装下载好的包
python setup.py install


# 实例代码

https://github.com/suqi/web_data_factory/

# django项目演示

cd workspace/demo
django-admin startproject demo
django-admin startapp bank

cd demo

python manage.py runserver
python manage.py dbshell
python manage.py createsuperuser

python manage.py migrate
python manage.py makemigrations
