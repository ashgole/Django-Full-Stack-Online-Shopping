from django.template import context


products= [{'id': '1',
                'add': 'https://source.unsplash.com/random/1600x900?macbook',
                'title': 'MacBook',
                'price':'100',
                'desc': 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'
                },
                {'id': '2',
                'add': 'https://source.unsplash.com/random/1600x900?iphone',
                'title': 'Iphone',
                'price':'200',
                'desc': 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'
                },
                {'id': '3',
                'add': 'https://source.unsplash.com/random/1600x900?headphone',
                'title': 'Headphone',
                'price':'300',
                'desc': 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'
                },
                ],

productsContext={
'products': [{'id': '1',
                'add': 'https://source.unsplash.com/random/1600x900?macbook',
                'title': 'MacBook',
                'price':100,
                'desc': 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'
                },
                {'id': '2',
                'add': 'https://source.unsplash.com/random/1600x900?iphone',
                'title': 'Iphone',
                'price':'200',
                'desc': 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'
                },
                {'id': '3',
                'add': 'https://source.unsplash.com/random/1600x900?headphone',
                'title': 'Headphone',
                'price':'300',
                'desc': 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'
                },
                ]}                