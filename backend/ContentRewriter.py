# ContentRewriter.py - ./backend/ContentRewriter.py
# This module contains the implementation of a content rewriter that removes plagiarism using the OpenAI API.
# It requires an API key to be set as an environment variable before running.
# The rewriter can process individual files or an entire directory of files.

# ContentRewriter.py

import openai_secret_manager
import openai
import re

# authenticate with OpenAI API using the API key stored in the secret manager
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

# regex pattern for matching urls in the text
URL_PATTERN = r"http\S+"

# function to rewrite content using the OpenAI GPT-3 API
def rewrite_content(text):
    # remove urls from the text
    text = re.sub(URL_PATTERN, "", text)
    
    # use the OpenAI API to generate new text based on the input
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=text,
      temperature=0.5,
      max_tokens=1024,
      n = 1,
      stop = "\n"
    )

    # return the first generated text as the rewritten content
    return response.choices[0].text.strip()

# test cases for rewrite_content function
def test_rewrite_content():
    text = "This is a sample text that needs to be rewritten."
    expected_output = "This is a new text that has been rewritten."
    assert rewrite_content(text) != text
    assert rewrite_content(text) != expected_output

    text = "Hello, how are you today? I am doing well, thank you for asking."
    expected_output = "Hi, how are you feeling today? I'm doing fine, thanks for asking."
    assert rewrite_content(text) != text
    assert rewrite_content(text) != expected_output

    text = "The quick brown fox jumps over the lazy dog."
    expected_output = "The fast brown fox leaps over the tired dog."
    assert rewrite_content(text) != text
    assert rewrite_content(text) != expected_output

# if this file is being run directly, run the test cases
if __name__ == "__main__":
    test_rewrite_content()

    ...
