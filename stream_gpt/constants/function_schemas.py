import stream_gpt.constants.prompts as prompts

                ################################
                #                              #
                #    Knowledge Tree Schemas    #
                #                              #
                ################################
                
RANK_CATEGORIES = [{
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
                
CHOOSE_BEST_SAMPLE = [{
        'name': 'choose_best_sample',
        'description': prompts.CHOOSE_BEST_SCRAPED_TEXT, 
        'parameters': {
            'type': 'object', 
            'properties': {
                'best_sample': {
                    'type': 'integer', 
                    'description': 'Provide the number of the sample that you think is best formatted. (No spacing errors, no missing characters, etc.)'
                }
            }, 
            'required': ['indexed_text']
        }
 }]