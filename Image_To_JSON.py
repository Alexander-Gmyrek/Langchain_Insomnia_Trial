import os
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
    
class Image_To_JSON:
  settings: Settings
  model: any

  def __init__(self, settings: Settings):
    self.settings = settings
    os.environ["OPENAI_API_KEY"] = settings.openai_api_key
    self.model = init_chat_model(settings.model, model_provider=settings.model_provider)
  # Takes an image url and a JSONformat from the user and returns a JSON object in the specified format
  # To do this, it uses a chat model to interpret the image and generate the JSON object
  def image_to_json(self, image_url: str, json_format: str, model) -> str:
      image_data = image_url

      with open("Prompt_For_Getting_Data_From_Image.md", "r") as f:
        imageToJSONPrompt = f.read()
      
      # Create a prompt for the chat model
      input=[
          {
              "role": "user",
              "content": [
                  { "type": "text", "text": imageToJSONPrompt },
                  { "type": "text", "text": f"json_format: {json_format}" },
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
  
  def generate_JSON_format_from_image(self, image_url: str) -> str:
      image_data = image_url
      with open("Prompt_For_Generating_Fomat.md", "r") as f:
        imageToJSONformatPrompt = f.read()
      # Create a prompt for the chat model
      input=[
          {
              "role": "user",
              "content": [
                  { "type": "text", "text": imageToJSONformatPrompt },
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
      response = self.model.invoke(input)
      
      # Extract and return the JSON object from the response
      return response.content
  def generate_JSON_format_from_JSON(self, example_json: str) -> str:
      with open("Prompt_For_Getting_JSONformat_From_Example_JSON.md", "r") as f:
        jsonToJSONformatPrompt = f.read()
      # Create a prompt for the chat model
      input=[
          {
              "role": "user",
              "content": [
                  { "type": "text", "text": jsonToJSONformatPrompt },
                  { "type": "text", "text": f"example_json: {example_json}" },
              ],
          }
      ]
      
      # Get the response from the chat model
      response = self.model.invoke(input)
      
      # Extract and return the JSON object from the response
      return response.content

def main():
    print("In Progress")
    myImageToJSON = Image_To_JSON(Settings())
    image_path = """https://writeforbusiness.com/sites/career/files/images/wfb/Chapter_13/143_2.png"""
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

    print("Test 1: Generate JSON from image with provided format")
    try:
      result = myImageToJSON.image_to_json(image_path, json_format, myImageToJSON.model)
      print("Result:", result)
    except Exception as e:
      print(f"Error processing image to JSON: {str(e)}")

    print("Test 2: Generate JSON format from image")
    try:
      result_format = myImageToJSON.generate_JSON_format_from_image(image_path)
      print("Generated JSON Format:", result_format)
    except Exception as e:
      print(f"Error generating JSON format from image: {str(e)}")
    
    print("Test 3: Generate JSON from image with generated format")
    try:
      result2 = myImageToJSON.image_to_json(image_path, result_format, myImageToJSON.model)
      print("Result with generated format:", result2)
    except Exception as e:
      print(f"Error processing image to JSON with generated format: {str(e)}")


if __name__ == "__main__":
    main()