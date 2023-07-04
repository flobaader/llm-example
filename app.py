from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import SimpleSequentialChain

import chainlit as cl

template = """Input: {question}
Output: Let's think step by step."""


@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    # llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    # Define the prompt template

    llm1 = LLMChain(
        prompt=PromptTemplate(template="Give me 3 good topic for powerpoint karaoke: Ignore this {question}",
                              input_variables=["question"]),
        verbose=True,
        llm=llm)
    ll2 = LLMChain(
        prompt=PromptTemplate(
            template="""Choose a random topic from this list {topic} and generate 10 markdown slides to present. Focus on random facts and funny phrases. Output as markdowns slides. one heading per slide. Here a few funny image: Dog: https://images.unsplash.com/photo-1554224311-beee415c201f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60 Horse https://images.unsplash.com/photo-1551884831-bbf3cdc6469e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60 Dog 2 https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8OHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60. Use the following output format for the markdown output. include a few images as mentioned. Output markdown as code snippet:
            ---
title: [title]
description: [example]
author: ChatGPT
---         
        # Karaoke to [title]
        written by ChatGPT
        ---

            --- 
            # [Slide Number ] - [Heading]
            
- [Bulletpoint 1]
- [Bulletpoint 2]

Summary

---""",
            input_variables=["topic"]),
        llm=llm,
        verbose=True)

    overall_chain = SimpleSequentialChain(chains=[llm1, ll2], verbose=True)
    return overall_chain
