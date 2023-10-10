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