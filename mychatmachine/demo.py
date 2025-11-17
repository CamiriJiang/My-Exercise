#绘制wb网页
import streamlit as st
from langchain_classic.memory import ConversationBufferMemory
from langchain的utils代码编写 import get_response
#写标题
st.title('Camiri的通义聊天机器人')
# st.markdown('#Camiri的通义聊天机器人') #md写法
#写介绍
st.write('我是一个随便的介绍')
st.divider() #加一个分割线
#搭建左侧的导航栏
with st.sidebar:
    st.header('没想好标题') #侧边栏的题目
    user_api_key = st.text_input('请输入通义账号的API key',type='password')
    st.markdown('[获取通义账号的API Key](https://www.aliyun.com/product/bailian)')   #用markdown插入超链接:[链接名字](链接)
#创建会话记忆体，记录聊天记录
if 'memory' not in st.session_state: #判断有没有历史对话，没有历史对话说明是用户第一次问问题，需要创建记忆体并显示欢迎语
    #session_state是一个字典，用于存储会话数据
    st.session_state['memory'] = ConversationBufferMemory() #这个参数表示要保留历史对话
    st.session_state['messages'] = [{'role':'ai','content':'您好，有什么事呀？'}]
    # st.chat_message("assistant").write('您好，有什么事呀？') #简单版本

#创建消息区：遍历会话记忆体中的所有聊天记录，并打印出来形成消息区
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.write(message['content']) #打印消息内容

prompt = st.chat_input('请输入你的问题')
if prompt: #如果用户输入了内容，就把输入的内容显示在消息区
    # if not user_api_key: #如果用户没有输入API key，就提示用户输入API key,否则程序停止运行
    #     st.warning('请输入API key')
    #     st.stop()
    #把用户输入的信息加入到会话记忆体中
    st.session_state['messages'].append({'role':'human','content':prompt})
    #把用户输入的信息显示在消息区
    with st.chat_message("user"):
        st.write(prompt)

#在获得结果前显示一个加载动画
with st.spinner('我正在努力思考中...'):
    content = get_response(prompt,st.session_state['memory'])
#把模型响应结果加入到会话记忆体中,并打印到消息区
st.session_state['messages'].append({'role':'ai','content':content})
st.chat_message("assistant").write(content)





