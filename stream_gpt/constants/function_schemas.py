import constants.prompts as prompts
rank_categories = [{
        'name': 'rank_categories', 
        'description': f'{prompts.rank_categories_prompt}', 
        'parameters': {
            'type': 'object', 
            'properties': {
                'categories': {
                    'type': 'array', 
                    'items': {
                        'type': "object",
                        'properties': {
                            'idea': { 
                                'type': "int", 
                                'description': "Provide numbers of relevant categories. Please say nothing if you don't think any of the categories are relevant."},
                        }
                    }
                }
            }, 
            'required': ['indexed_text']
        }
 }]

indexing_function = [{
        'name': 'construct_list', 
        'description': 'Generate a comprehensive list focusing on only the pivotal concepts, techniques, or methodologies that are discussed in depth within the content, whether its code, text, or documentation. Exclude superficial mentions, headers, table of contents, and any content that is not critically elaborated upon.', 
        'parameters': {
            'type': 'object', 
            'properties': {
                'indexed_text': {
                    'type': 'array', 
                    'items': {
                        'type': "object",
                        'properties': {
                            'idea': { 
                                'type': "string", 
                                'description': "Comprehensive yet concise description of idea or principle discussed" },
                        }
                    }
                }
            }, 
            'required': ['indexed_text']
        }
 }]