indexing_system_message = 'Create a comprehensive list describing all specific ideas in the text. '
indexing_system_message2 = 'Generate a comprehensive list focusing on only the pivotal concepts, techniques, or methodologies that are discussed in depth within the content, whether its code, text, or documentation. Exclude superficial mentions, headers, table of contents, and any content that is not critically elaborated upon.'
indexing_system_message3 = 'Provide a list summarizing the specific, nuanced ideas and principles that are discussed in this text. Each item should be sufficiently detailed to encapsulate the core point of its corresponding section. Avoid including superficial mentions, generic topics, and anything that is not deeply elaborated upon.'

summarization_system_message = 'Summarize all the main ideas in this text.'
concise_summarization_system_message = 'Summarize the main ideas more compactly.'
summarization_system_message2 = 'Summarize all the main ideas in 2 sentences'


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

indexing_function2 = [{
        'name': 'construct_list', 
        'description': 'Concisely describe ideas, compress this text.', 
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

indexing_function3 = [{
        'name': 'summarize', 
        'description': 'Write as few sentences possible summarizing the text', 
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
                                'description': "Concise description of idea discussed" },
                        }
                    }
                }
            }, 
            'required': ['indexed_text']
        }
 }]


indexing_function_sentence = [{
        'name': 'summarize', 
        'description': 'Summarize the text in 2 sentences', 
        'parameters': {
            'type': 'object', 
            'properties': {
                'idea1': {
                    'type': 'string', 
                    'description': '1st main idea'
                },
                'idea2': {
                    'type': 'string', 
                    'description': '2nd main idea'
                }
            }, 
            'required': ['idea1', 'idea2']
        }
 }]





