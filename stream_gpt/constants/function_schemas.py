import stream_gpt.constants.prompts as prompts

                ################################
                #                              #
                #    Knowledge Tree Schemas    #
                #                              #
                ################################
                
RANK_CATEGORIES_FUNCTION_SCHEMA = [{
        'name': 'rank_categories', 
        'description': f'{prompts.RANK_CATEGORIES}', 
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


                ################################
                #                              #
                #     Data Scraper Schemas     #
                #                              #
                ################################
                
CHOOSE_BEST_SCRAPED_TEXT_FUNCTION_SCHEMA = [{
        'name': 'choose_best_scraped_text',
        'description': prompts.CHOOSE_BEST_SCRAPED_TEXT, 
        'parameters': {
            'type': 'object', 
            'properties': {
                'indexed_text': {
                    'type': 'int', 
                    'description': 'Provide the number of the best text. Please say nothing if you think none of the texts are relevant.'
                }
            }, 
            'required': ['indexed_text']
        }
 }]