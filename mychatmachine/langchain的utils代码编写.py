#写核心业务逻辑：接收用户录入的prompt、调用模型、获取结果
import os
from langchain_community.llms import Tongyi
from langchain_classic.chains import  ConversationChain  #导入会话链类：llm模型+记忆体
from langchain_core.prompts import  ChatPromptTemplate #提示词模板类
from langchain_classic.memory import ConversationBufferMemory #会话记忆体

def get_response(prompt,memory,api_key = ''):
    """
用于根据用户录入的提示词，调用模型，获取结果
    :param prompt:提示词
    :param memory:记忆体
    :param api_key:调用接口的api,也可以不写
    :return: 结果
    """
    if prompt is None:
        prompt = ''
    if api_key == '':
        api_key = os.environ.get('DASHSCOPE_API_KEY')
    else:
        api_key = api_key
    llm = Tongyi(model = 'qwen-max',dashscope_api_key = api_key)
    #创建会话链
    chain = ConversationChain(llm = llm,memory = memory)
    response = chain.invoke({'input':prompt}) #会话链这个类就是要用键值对传参
    # return  response #如果这样写会返回所有结果，包括：提示词，模型返回的结果和历史会话记录
    return response['response'] #返回模型返回的结果

if __name__ == '__main__':
    prompt = '世界上的最高峰是哪座？'
    memory = ConversationBufferMemory(return_messages= True)
    result = get_response(prompt,memory)
    print(result,type(result))