This is a place for me to learn langchain and insomnia api development.
My initial goal is to design an API that can take an image and convert the
information to a JSON format.

The API should be simple. Users can send an image URL with a specified JSONformat and 
will receive a JSON with the data from the image.

To set up a JSONformat the users can submit a name and an example JSON or a premade JSONformat and 
will receive a confirmation.

Users can also submit an image url or example JSON to recieve a premade JSONformat.

If you are running this locally, you will need to create your own .env file. It should be formatted as such:
OPENAI_API_KEY=[Your OpenAI API Key]
MODEL=gpt-5-nano
MODEL_PROVIDER=openai
