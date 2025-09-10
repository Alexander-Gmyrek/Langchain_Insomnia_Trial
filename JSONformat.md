# JSON format #  
JSONformats are simple explanations of how a JSON should be formatted. 
Each entry should contain the element, the type of element, 
description of the element, and notes.    


### Element ###  
This should just be the name of the element. E.g firstName, date, or fileFormat. 
The element name should be simple, explanatory, and camel cased if necessary.  


### Type ###
This is the datatype of the element and should be taken from a standard list of types.  
##### Types: #####  
###### Basic Types: ######  
- string: A basic string  
- int: A basic integer  
- float: All non integer number values  
- boolean: True or False  
###### Class Types: ######  
- category: A class of element that can only have set values (category(string))  
- array: An unlabeled list of elements with a specified type (array(int))  
- object: An element with subelements inside it.


### Description ###
A brief description of the element.  


### Notes ###  
Contain information on formatting, gathering, identifying, or location if absolutely necessary.
Also where information on possible values for categories, regex patterns, allowed value ranges, reference links, etc.   


### Template ###
```json
[
  {
    "element": "{{elementName}}",
    "type": "{{type}}",
    "description": "{{brief description of the element}}",
    "notes": "{{constraints, formatting rules, possible values, or additional details}}"
  },
  {
    "element": "{{anotherElement}}",
    "type": "{{type}}",
    "description": "{{brief description of the element}}",
    "notes": "{{constraints, formatting rules, possible values, or additional details}}"
  },
  {
    "element": "{{objectElement}}",
    "type": "object",
    "description": "{{brief description of the object}}",
    "notes": "{{notes about the object and its purpose}}",
    "subElements": [
      {
        "element": "{{subElementName}}",
        "type": "{{type}}",
        "description": "{{brief description of the sub-element}}",
        "notes": "{{constraints or formatting rules}}"
      }
    ]
  },
  {
    "element": "{{arrayElement}}",
    "type": "array({{subtype}})",
    "description": "{{brief description of the array}}",
    "notes": ""
  },
  {
    "element": "{{categoryElement}}",
    "type": "category({{subtype}})",
    "description": "{{brief description of the category element}}",
    "notes": "Possible values: {{list of allowed values}}"
  }
]
```

### Example ###  
```json
[
  {
    "element": "firstName",
    "type": "string",
    "description": "The given name of the user.",
    "notes": "Should be properly capitalized. Example: 'John'."
  },
  {
    "element": "age",
    "type": "int",
    "description": "The age of the user in years.",
    "notes": ""
  },
  {
    "element": "emailAddress",
    "type": "string",
    "description": "The primary contact email for the user.",
    "notes": "email format (e.g., name@example.com)."
  },
  {
    "element": "accountType",
    "type": "category(string)",
    "description": "The type of account the user holds.",
    "notes": "Possible values: 'free', 'premium', 'enterprise'."
  },
  {
    "element": "hobbies",
    "type": "array(string)",
    "description": "A list of hobbies the user enjoys.",
    "notes": ""
  },
  {
    "element": "address",
    "type": "object",
    "description": "The user's primary mailing address.",
    "notes": "All sub-elements are required.",
    "subElements": [
      {
        "element": "street",
        "type": "string",
        "description": "Street name and number.",
        "notes": ""
      },
      {
        "element": "city",
        "type": "string",
        "description": "City of residence.",
        "notes": ""
      },
      {
        "element": "postalCode",
        "type": "string",
        "description": "Postal or ZIP code.",
        "notes": "Format depends on country."
      }
    ]
  }
]
```