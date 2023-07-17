#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 sakakibara <sakakibara@dyana>
#
# Distributed under terms of the MIT license.
import os
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools


with open('prompt', 'r') as f:
    prompt = f.read()

print(prompt)

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=api_key, temperature=0.9)

tools = load_tools(["serpapi"], llm=llm)
agent = initialize_agent(
    tools, llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run(prompt)
