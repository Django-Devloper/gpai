from langchain_openai import ChatOpenAI
from langchain.prompts import  PromptTemplate ,ChatPromptTemplate ,HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import SystemMessage
from django.db import models
exclude_list =  ['id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted', 'is_updated']


def translate(input_language='en', output_language='hi', user_input=None):
    prompt_template = PromptTemplate(
        template="Act as expert Translator current language is {input_language} translate  the following text to {output_language}: {text} . Make sure 100% accuracy. "
    )
    llm = ChatOpenAI()
    translator_chain = LLMChain(llm=llm, prompt=prompt_template)
    result = translator_chain.invoke({"input_language": input_language, 'output_language':output_language,"text": user_input})
    return result['text']


def get_filtered_fields(model):
    field_list = []
    for field in model._meta.get_fields():
        if field.is_relation and field.related_model and not isinstance(field, models.ManyToManyField):
            related_model = field.related_model
            related_fields = [
                f.name for f in related_model._meta.get_fields()
                if not f.is_relation and f.name not in exclude_list
            ]
            field_list.extend(related_fields)

    return field_list

def queryformater(model,text):
    columns_list = get_filtered_fields(model)
    chat_templates = ChatPromptTemplate.from_messages([
        SystemMessage(content= f"""You are an expert Django ORM query generator.
                Columns: {columns_list} (list of all available column names).
                Objective: Generate a Django filter query based on a provided text input.
                Requirements:
                Handle Inaccuracies:
                The input text may include spelling mistakes (e.g., "abmin" instead of "admin" or "Bubai" instead of "Dubai").
                The text is not case-sensitive.
                Multiple Matches:
                A single input word can match multiple columns.
                Create filters for all relevant columns where a match is found.
                Generate Optimal Query:
                Use fuzzy matching or similar logic to select the most relevant matches for each column.
                Combine conditions using Q objects if necessary to ensure flexibility.
                
                Output: you are ony allow to return Django ORM Q objects query."""),
        HumanMessagePromptTemplate.from_template('text{message}')
        ]
    )
    messages = chat_templates.format_messages(message =text )
    llm = ChatOpenAI()
    output = llm.invoke(messages)
    return output.content
