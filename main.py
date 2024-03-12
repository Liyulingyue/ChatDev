import os

# 配置环境变量
os.environ['ernie_token'] = '**********'
os.environ['openai_new_api'] = "0" # 1为新版，0为旧版

# 最好使用英文，因为所有的Prompts都是英文的
os.system('python run.py '
          '--task "Develop a basic Gomoku game." '
          '--name "Gomoku"')