from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent


bind = "0.0.0.0:8000"  # 绑定的地址和端口
workers = 1  # 工作进程的数量
timeout = 120  # 请求超时时间（以秒为单位）
errorlog = os.path.join(os.path.dirname(BASE_DIR),
                        'logs/error.log')  # 错误日志文件的路径
accesslog = os.path.join(os.path.dirname(
    BASE_DIR), 'logs/access.log')  # 访问日志文件的路径

# print(errorlog)
