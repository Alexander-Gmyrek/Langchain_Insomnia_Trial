import getpass
import os
import json
import base64
from langchain.chat_models import init_chat_model # type: ignore
from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
    openai_api_key: str
    model: str = "gpt-5-nano"
    model_provider: str = "openai"

    class Config:
        env_file = ".env"

def encode_image(image_path):
    try:
      with open(image_path, "rb") as image_file:
          return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
      raise Exception(f"Image file not found: {image_path}")
    except Exception as e:
      raise Exception(f"Error encoding image: {str(e)}")
    


# Takes an image and a JSONformat from the user and returns a JSON object in the specified format
# To do this, it uses a chat model to interpret the image and generate the JSON object
def image_to_json(image_path: str, json_format: str, model) -> str:
    # Load and preprocess the image
    image_data = "https://writeforbusiness.com/sites/career/files/images/wfb/Chapter_13/143_2.png"
    
    
    # Create a prompt for the chat model
    input=[
        {
            "role": "user",
            "content": [
                { "type": "text", "text": "Gather data from this image based off the JSON format provided. Do not holucinate or make up data." },
                { "type": "text", "text": f"Return the result in a JSON created from objects in this format: {json_format}" },
                { "type": "text", "text": """Example: if you see {"element": "date", "type": "string"...} then just include "date": "date you see" in the json""" },
                {
                    "type": "image_url",
                    "image_url": {
                      "url": image_data
                    },
                },
            ],
        }
    ]
    
    
    # Get the response from the chat model
    response = model.invoke(input)
    
    # Extract and return the JSON object from the response
    return response.content

def main():
    print("In Progress")
    try:
      settings = Settings()
    except Exception as e:
      print(f"Error loading settings: {str(e)}")
      return
    os.environ["OPENAI_API_KEY"] = settings.openai_api_key
    model = init_chat_model(settings.model, model_provider=settings.model_provider)
    image_path = """TestSamples/example_filled_out_form.png"""
    json_format = """TestSamples/testJSONformat.json"""
    # Read the JSON format from the file
    try:
      with open(json_format, "r") as f:
          json_format = f.read()
    except FileNotFoundError:
      print(f"JSON format file not found: {json_format}")
      return
    except Exception as e:
      print(f"Error reading JSON format file: {str(e)}")
      return  

    try:
      result = image_to_json(image_path, json_format, model)
      print("Result:", result)
    except Exception as e:
      print(f"Error processing image to JSON: {str(e)}")

    


if __name__ == "__main__":
    main()