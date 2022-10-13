post_person = {
    'type': 'object',
    'properties': {
        'firstName': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255
        },
        'lastName': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255
        },
    },
    'required': ['firstName', 'lastName']
}

put_person = {
    'type': 'object',
    'properties': {
        'firstName': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255
        },
        'lastName': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255
        },
    },
    'required': ['firstName', 'lastName']
}

post_car = {
    'type': 'object',
    'properties': {
        'color': {
            'type': 'string',
            'enum': [
                'Yellow',
                'Blue',
                'Gray'
            ]
        },
        'model': {
            'type': 'string',
            'enum': [
                'Hatch',
                'Sedan',
                'Convertible'
            ]
        },
        'person': {
            'type': 'number',
            'minimum': 0,
            'maximum': 100
        }
    },
    'required': ['color', 'model', 'person']
}

put_car = {
    'type': 'object',
    'properties': {
        'color': {
            'type': 'string',
            'enum': [
                'Yellow',
                'Blue',
                'Gray'
            ]
        },
        'model': {
            'type': 'string',
            'enum': [
                'Hatch',
                'Sedan',
                'Convertible'
            ]
        },
        'person': {
            'type': 'number',
            'minimum': 0,
            'maximum': 100
        }
    },
    'required': ['color', 'model', 'person']
}