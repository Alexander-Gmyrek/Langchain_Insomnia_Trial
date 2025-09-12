Extract data from the provided image using the JSON format specified in the 'json_format' template.
'''
- Only enter data that is directly and clearly visible in the image. Do not invent, guess, or assume values.
- If a field from the 'json_format' is missing or unclear in the image, do not include it in the output JSON.
- If the template contains an element like {"element": "date", "type": "string"}, only include "date": "date you see" in the output JSON.
- If no fields can be filled, return an empty JSON object: {}.
'''
Output a single JSON object with keys and value types matching the 'json_format' template. Only include keys for which you can extract valid, clearly visible data from the image. Exclude all fields that are missing or illegible.