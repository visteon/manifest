
from openai import OpenAI

client = OpenAI()

def review_code(source_code, language="Python"):

    prompt = f"""
    You are an expert software engineer and code reviewer.

    Review the following {language} code.

    Find:
    1. Bugs and logical errors
    2. Syntax errors
    3. Security vulnerabilities
    4. Performance issues
    5. Code quality problems

    For every issue provide:
    - Issue description
    - Line number (if identifiable)
    - Severity (Critical, High, Medium, Low)
    - Why it is a problem
    - Suggested solution

    Also provide corrected code.

    Source code:
    {source_code}
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":

    code = """
    def divide(a, b):
        return a / b

    print(divide(10, 0))
    """

    result = review_code(code)

    print("\n===== AI CODE REVIEW RESULTS =====\n")
    print(result)
