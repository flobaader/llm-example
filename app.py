from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

import chainlit as cl

template = """Input: {question}
Output: Let's think step by step."""


@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)
    return llm_chain
