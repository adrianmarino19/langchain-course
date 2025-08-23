import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

breed = 'Border Collie'


def main():
    print("Hello from langchain-course!!!")

    template = '''
    Please invent a cool name for a female dog which is a {breed}.
    '''

    prompt = PromptTemplate(input_variables=['breed'],
                            template=template)

    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.75)

    chain = prompt | llm  # remember it as I want to pass the prompt -> the LLM!

    res = chain.invoke(breed)

    print(res.content)



if __name__ == "__main__":
    main()
