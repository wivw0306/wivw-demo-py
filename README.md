# 简介

我的工具

# 一.上传步骤:
## 1.生成 dist 目录用于上传 
```shell
python setup.py sdist bdist_wheel
```

## 2.上传包到私有 pypi 源 
```shell
cat ~/.pypirc
[distutils]
index-servers = pypi local

[pypi]
repository: https://www.python.org/pypi
username = __token__
password = 'xxxxxxxxxxx'

[local]
repository: http://localhost:3141
username: yehaiquan password: 12345678
```

## 3.上传到 local 仓库 
```shell
twine upload dist/* -r local
```

## 4.测试是否上传 
访问 http://localhost:3141/simple/

## 5.安装 
```shell
pip search -i http://localhost:3141 wivw_demo #查找包 
pip install -i http://localhost:3141/simple wivw_demo #安装包 pip
install -U -i http://localhost:3141/simple wivw_demo #安装最新包
```

## 6.测试是否安装 
```python
import wivw_demo 
from wivw_demo import mytool 
wivw_demo.show()
mytool.mytest()
```

## 7.卸载包 
```shell
pip uninstall wivw-demo
```

# 二.上传到 pypi 仓库 
## 1.登陆个人pypi后台(如没有账号需要先注册)
https://pypi.org/manage/projects/

## 2.创建token.
登陆https://pypi.org/manage/account/,找到api token,添加一个新的token

## 3.配置token 
```shell
cat ~/.pypirc
[pypi]
username: __token__
password: pypi-AgEIcHlwaS5vcmcCYxxzI0WuBg-zgyXxBO1r4ZW6hX450jdsw
```

> 用户名和密码也可以用自己的个人登陆账号,但不推荐,推荐用token方式验证.

## 4.上传包到pypi
```shell
twine check dist/*
twine upload dist/*
```

## 5.安装
```shell
pip install wivw-demo
```

## 6.测试是否安装 
```python
import wivw_demo 
from wivw_demo import mytool 

wivw_demo.show()
mytool.mytest()
```

## 7.卸载包 
```shell
pip uninstall wivw-demo
```

## 完毕!