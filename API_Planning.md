# API Plan #  
The goal of this API is to make it as easy as possible to get the data 
from an image to a JSON for use in other areas
### Setup ###  
The API is split into three parts:  
1. Getting the data from an image.  
2. Generating a JSONformat.  
3. Storing the JSONformat. (Later)  

### Getting the Data ###  
This should just be a simple POST request that takes an image and a JSONformat and returns a JSON  
#### Responses: ####  
- 200: OK  
- 220: Please Review Output
- 400: Improperly formated Request  
- 413: Content Too Large  
- 415: Unsuported Media Type, please only use jpg png or pdf for images  
- 500: Internal Server Error Catch-All, please check error message  
- 508: Failed to Extract Data After Multiple Attempts

### Generating a JSONformat ###  