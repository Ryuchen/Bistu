<h1 align="center">Welcome to Bistu-backend</h1>
<p align="center">
  <img src="https://img.shields.io/badge/version-v1.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/language-python3-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/platform-macos-blue.svg?cacheSeconds=2592000" />
  <a href="http://www.gnu.org/licenses/gpl-3.0.html">
    <img alt="License: GPL" src="https://img.shields.io/badge/License-GPL-yellow.svg" target="_blank" />
  </a>
</p>

### 🏠 [个人小栈](https://ryuchen.github.io/)

    > 未来更新的说明会刊登在这里，并且会不定时分享部分内容和心得


### 📎 项目说明:
    > 这是在学校接的一个小项目，构建个管理系统，一个小系统，鉴于学习角度，正好配合 django-simpleui 构建了个管理后台，顺手学下 vue 该怎么写，深入的学习会单独再开一个项目
    > 这个项目需要配合我 fork 的 django-simpleui 修订版本进行运行，然后将会后续搭配一个前端，将由 ant-design-pro 构建，顺手也学下 react 该怎么写。
    
### 📖 安装说明:

```
安装依赖
   pip install -r requirements.txt

然后需要 fork 我的 simpleui 项目源码
   ln -s simpleui(fork 的源码) venv/lib/site-packages/simpleui/(这是你的 pip 安装后的 simpleui 源码路径)
   
生成数据库
   rm -rf db.sqlite3
   python manage.py makemigrations && python manage.py migrate && python manage.py migrate --run-syncdb
   
生成假数据
   python manage.py fake_data
   
运行 demo
   python manage.py runserver 0:9377
```
 > 查看 demo 地址: [http://127.0.0.1:9377](http://127.0.0.1:9377)
 > 账户信息: admin&ant.design(账户&密码)

### 👤 作者介绍:

Ryuchen ( 陈 浩 )

* Github: [https://github.com/Ryuchen](https://github.com/Ryuchen)
* Email: [chenhaom1993@hotmail.com](chenhaom1993@hotmail.com)
* QQ: 455480366
* 微信: Chen_laws

Nameplace ( 虚位以待 )

### 🤝 贡献源码:

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Ryuchen/Bistu/issues).
