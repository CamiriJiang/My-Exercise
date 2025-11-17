#需求：基于langchain调用通义，实现文本生成，提示词：从前有一个美丽的小村庄，那里的人们过着宁静的生活
from langchain_community.llms import Tongyi

#创建提示词
prompt = "从前有一个美丽小村庄，那里的人们过着宁静的生活"
#创建大模型
llm = Tongyi(
    model = 'qwen-max', #模型名称
    #dashscope_api_key = 'YOUR_API_KEY' 因为我已经配置了环境变量，因此这个参数我可以不写
)

#调用接口，生成文本。发起请求给模型，获取响应
result = llm.invoke(prompt)
print(f'提示词：{prompt}')
print(f'结果：{result}')

