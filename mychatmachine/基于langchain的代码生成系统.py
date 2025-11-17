#需求：prompt:请为以下功能生成python代码，功能：计算两个数的最大公约数

from langchain_community.llms import Tongyi

llm = Tongyi(model = 'qwen-max')
prompt = '请为计算两个数最大公约数这个功能生成python代码'
result = llm.invoke(prompt)
print(f'代码生成如下：\n{result}')