# JSON format #  
JSONformats are simple explenations of how a JSON should be formated. 
Each entry should contain the element, the type of element, 
description of the element, and notes.    


### Element ###  
This should just be the name of the element. E.g firstName, date, or fileFormat. 
The element name should be simple, explanitory, and camel cased if nessicary.  


### Type ###
This is the datatype of the element and should be taken from a standard list of types.  
##### Types: #####  
###### Basic Types: ######  
- String: A basic string  
- Int: A basic integer  
- Float: All non integer number values  
- Boolean: True or False, 1 or 0  
###### Class Types: ######  
- Category: A class of element that can only have set values (category(string))  
- Array: An unlabeled list of elements with a specified type (array(int))  
- Object: An element with subelements inside it.


### Description ###
A brief description of the element.  


### Notes ###  
Contain infromation on formating, gathering, identifying, or location if absolutely nessicary.
Also where information on possible values for categorys and higher and lower bounds of values are stored.   


### Template ###
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
    "type": "Object",
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
    "type": "Array({{subtype}})",
    "description": "{{brief description of the array}}",
    "notes": ""
  },
  {
    "element": "{{categoryElement}}",
    "type": "Category({{subtype}})",
    "description": "{{brief description of the category element}}",
    "notes": "Possible values: {{list of allowed values}}"
  }
]

### Example ###  
[
  {
    "element": "firstName",
    "type": "String",
    "description": "The given name of the user.",
    "notes": "Should be properly capitalized. Example: 'John'."
  },
  {
    "element": "age",
    "type": "Int",
    "description": "The age of the user in years.",
    "notes": ""
  },
  {
    "element": "emailAddress",
    "type": "String",
    "description": "The primary contact email for the user.",
    "notes": "email format (e.g., name@example.com)."
  },
  {
    "element": "accountType",
    "type": "Category(String)",
    "description": "The type of account the user holds.",
    "notes": "Possible values: 'free', 'premium', 'enterprise'."
  },
  {
    "element": "hobbies",
    "type": "Array(String)",
    "description": "A list of hobbies the user enjoys.",
    "notes": ""
  },
  {
    "element": "address",
    "type": "Object",
    "description": "The user's primary mailing address.",
    "notes": "All sub-elements are required.",
    "subElements": [
      {
        "element": "street",
        "type": "String",
        "description": "Street name and number.",
        "notes": ""
      },
      {
        "element": "city",
        "type": "String",
        "description": "City of residence.",
        "notes": ""
      },
      {
        "element": "postalCode",
        "type": "String",
        "description": "Postal or ZIP code.",
        "notes": "Format depends on country."
      }
    ]
  }
]