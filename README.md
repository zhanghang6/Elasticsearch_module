aaaasfai# 软件测试与维护大作业

# 前端配置

## 进入项目目录

cd template

## 安装依赖(node版本请使用12.17.0，否则可能会出现问题)

npm install

## 建议不要直接使用 cnpm 安装以来，会有各种诡异的 bug。可以通过如下操作解决 npm 下载速度慢的问题

npm install --registry=[https://registry.npm.taobao.org](https://registry.npm.taobao.org)

## 如遇报错，多半因为node，npm版本有问题可参考下面文章，选择12-17版本（推荐node为12.17.0）

[https://blog.csdn.net/weixin_44582077/article/details/110237056](https://blog.csdn.net/weixin_44582077/article/details/110237056)

## 启动服务

npm run dev

# 后端配置

## 进入后端目录

cd api

## 进入虚拟环境

## 虚拟环境不通用，因此下载后请删除venv重新配置后端虚拟环境

venv\Scripts\activate
deactivate(退出虚拟环境)

## 如遇禁止运行脚本，请参考[https://blog.csdn.net/l_x_cser/article/details/104956657](https://blog.csdn.net/l_x_cser/article/details/104956657)

## 后端依赖

pip install Flask
pip install -U flask-cors
pip install openpyxl
pip install pandas

## 开启后端

flask run

