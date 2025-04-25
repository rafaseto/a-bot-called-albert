#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate


# ### Load OpenAI's API key

# In[2]:


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# ### Configure the LLM

# In[3]:


llm = OpenAI(temperature=0.2, openai_api_key=api_key)


# In[4]:


llm.model_name


# ### Prompt template to summarize the text

# In[5]:


template = PromptTemplate(
    input_variables=["text"],
    template="Summarize this text in three words:\n\n{text}"
)


# ### Chain

# In[6]:


chain = template | llm