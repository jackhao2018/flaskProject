import os

# 绑定监听ip和端口号
bind='0.0.0.0:80'

# 同时执行的进程数，推荐为当前CPU个数*2+1
workers=3

# 等待服务客户的数量，最大为2048，即最大挂起的连接数
backlog=2048

# sync, gevent,meinheld  工作模式选择，默认为sync，这里设定为gevent异步
worker_class="gevent"

# 默认的最大客户端并发数量
max_requests=1000

# 是否后台运行
daemon=True

# 当代码有修改时，自动重启workers。适用于开发环境。
reload=True

# 设置pid文件的文件名
pidfile='./gunicore.pid'

# debug error warning error critical
loglevel='debug'

# 设置访问日志
accesslog='logs/log_files/gunicorn.log'

# 设置问题记录日志
errorlog='logs/log_files/gunicorn.err.log'
