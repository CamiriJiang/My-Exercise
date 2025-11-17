#构建一个翻译器，实现英译汉
#之所以有消息模板类，是为了让用户更加精准的按照指定模板格式进行提问，可以实现模型的精准查找等...
from langchain_classic.chains.summarize.refine_prompts import prompt_template
from langchain_community.llms import Tongyi
import langchain
from langchain_core.prompts import ChatPromptTemplate
#ChatPromptTemplate是消息模板类，可以根据模板生成消息

#构建模型
llm = Tongyi(model = 'qwen-max')
#创建提示词模板
prompt = ChatPromptTemplate.from_messages(
    #system就是告诉大模型你的需求（它是谁它要做什么）
    [('system','你是一位专业的翻译，能够将{input_language}翻译成{output_language}并且输出文本会根据用户要求的任何语言风格进行调整。请输出翻译后的文本，不要有任何其他内容。'),
     #human就是用户会干嘛
    ('human','文本：{text}\n语言风格：{style}')]
    #还有个('ai','一些内容')表示人工智能输出的内容
)
#传入指定参数，获取到具体的(提示词，消息内容)，这里的参数就是prompt里面用到的参数，都是可以随意更改的
text = input('请输入要翻译的文本内容')
prompt_value = prompt.invoke(
    {'input_language':'英语','output_language':'中文',
     'text':text, #由于整体是个字典的数据类型，因此在value位置可以直接写变量，不需要加{}
     'style':'文言文'
    }
)
#调用模板，获取结果
result = llm.invoke(prompt_value)
print(result)
#以上代码相当于是直接定义如下prompt,然后invoke模型获取结果
prompt_2 = '''
你是一位专业的翻译，能够将 英语 翻译成 汉语，并且输出文本会根据用户要求的任何语言风格进行调整。请输出翻译后的文本，不要有任何其他内容。
文本：'...'
语言风格：'文言文'
'''

#如果不用ChatPromptTemplate来接收提示词：
# 若只用prompt='要翻译的内容'->result = prompt.invoke(prompt)会让大语言模型无法准确理解你的意思，是要翻译还是补长还是什么其他功能