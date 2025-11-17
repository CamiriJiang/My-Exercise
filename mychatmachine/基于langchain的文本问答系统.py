#需求：实现文本问答，Prompt:世界上最高的山峰是哪一座？

from langchain_community.llms import Tongyi
#创建模型
llm = Tongyi(model = 'qwen-max')

#用while死循环达到问答效果
while True:
    prompt = input('请输入您的问题:')

    result = llm.invoke(prompt) #向llm模型发起请求，获取响应结果

    print(f'结果：{result}')