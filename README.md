# 简介

我的工具





上传步骤:
1.生成 dist 目录用于上传
python setup.py sdist bdist_wheel

2.上传包到私有 pypi 源
cat ~/.pypirc
[distutils]
index-servers =
  pypi
  local

[pypi]
username: 在pypi上的用户名
password: 在pypi上的密码

[local]
repository: http://localhost:8080
username: yehaiquan
password: 12345678

3.上传到 local 仓库
twine upload dist/* -r local

4.测试是否上传
访问 http://localhost:3141/simple/

5.安装
pip search -i http://localhost:3141 wivw_demo  #查找包
pip install -i http://localhost:3141/simple wivw_demo  #安装包
pip install -U -i http://localhost:3141/simple wivw_demo  #安装最新包

6.测试是否安装
import wivw_demo
from wivw_demo import mytool
wivw-demo.show()
mytool.mytest()

7.卸载包
pip uninstall  wivw-demo