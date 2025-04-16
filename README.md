# Ersilia Metadata Annotation
Metadata annotation pipelines for the Ersilia Model Hub

summarizer.py

includes a function that takes in a text as a parameter and uses the open ai api key to get a response from openai that summarizes the text. Then, returns the text content of the response given by openAI. The API for OpenAI is stored in .env, which is listed in the .gitignore files, meaning that .env is not pushed to the remote repository.