import json
import os

from grazie.api.client.gateway import AuthType, GrazieApiGatewayClient, GrazieHeaders
from grazie.api.client.chat.prompt import ChatPrompt
from grazie.api.client.endpoints import GrazieApiGatewayUrls
from grazie.api.client.profiles import Profile

def get_client():
    """
    Returns a client for the Grazie API Gateway.
    """
    token = os.getenv("GRAZIE_JWT_TOKEN")

    client = GrazieApiGatewayClient(
        url=GrazieApiGatewayUrls.STAGING,
        grazie_jwt_token=token,
        auth_type=AuthType.APPLICATION,
    )
    return client


def get_completion(system_prompt: str, input: str):
    """
    Returns a completion from the LLM for the given input.
    params:
    system_prompt: The system prompt
    input: The input
    returns:
    str: The completion
    """
    client = get_client()
    client_ip = "127.0.0.1"

    chat = ChatPrompt().add_system(system_prompt).add_user(input)
    response = client.chat(
        chat=chat,
        profile=Profile.OPENAI_GPT_4,
        headers={
            GrazieHeaders.ORIGINAL_USER_IP: client_ip,
        }
    )
    return response.content

def retry(func, *args, **kwargs):
    """
    Retries a function until it returns a result.
    params:
    func: The function to retry
    args: The arguments to pass to the function
    kwargs: The keyword arguments to pass to the function
    returns:
    The result of the function
    """
    number_of_tries = 3
    for i in range(number_of_tries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            if i == number_of_tries - 1:
                raise e