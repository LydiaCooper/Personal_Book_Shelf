import json
books_dict = {
    '1984': {
        'author': 'George Orwell',
        'goodreads_rating': 4.19,
        'read_status': 'read',
        'personal_rating': 'tbc',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    'Harry Potter and the Philosophers Stone': {
        'author': 'J.K. Rowling',
        'goodreads_rating': 4.47,
        'read_status': 'read',
        'personal_rating': 4.5,
        'publication_year': 1997,
        'genre': 'Fantasy'
    },
    'Venomous Lumpsucker': {
        'author': 'Ned Beauman',
        'goodreads_rating': 3.83,
        'read_status': 'read',
        'personal_rating': 3.0,
        'publication_year': 2022,
        'genre': 'Science Fiction'
    },
    'Writers & Lovers': {
        'author': 'Lily King',
        'goodreads_rating': 4.03,
        'read_status': 'read',
        'personal_rating': 'tbc',
        'publication_year': 2020,
        'genre': 'Literary Fiction'
    },
    'Everything I Know About Love': {
        'author': 'Dolly Alderton',
        'goodreads_rating': 4.05,
        'read_status': 'read',
        'personal_rating': 3.5,
        'publication_year': 2018,
        'genre': 'Memoir'
    },
    'Im Thinking Of Ending Things': {
        'author': 'Iain Reid',
        'goodreads_rating': 3.57,
        'read_status': 'read',
        'personal_rating': 4.00,
        'publication_year': 2016,
        'genre': 'Psychological Thriller'
    },
    'The Ends': {
        'author': 'James Smythe',
        'goodreads_rating': 4.09,
        'read_status': 'read',
        'personal_rating': 4.5,
        'publication_year': 2015,
        'genre': 'Science Fiction'
    },
    'Pew': {
        'author': 'Catherine Lacey',
        'goodreads_rating': 3.70,
        'read_status': 'not read',
        'personal_rating': 'tbc',
        'publication_year': 2020,
        'genre': 'Literary Fiction'
    },
    'Tomorrow, and Tomorrow, and Tomorrow': {
        'author': 'Gabriella Zevin',
        'goodreads_rating': 4.20,
        'read_status': 'read',
        'personal_rating': 5.0,
        'publication_year': 2022,
        'genre': 'Literary Fiction'
    },
    'Cleopatra and Frankenstein': {
        'author': 'Coco Mellors',
        'goodreads_rating': 3.38,
        'read_status': 'read',
        'personal_rating': 3.5,
        'publication_year': 2022,
        'genre': 'Contemporary'
    },
    'Stoner': {
        'author': 'John Williams',
        'goodreads_rating': 4.33,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 1965,
        'genre': 'Classics'
    },
    'Project Hail Mary': {
        'author': 'Andy Weir',
        'goodreads_rating': 4.51,
        'read_status': 'read',
        'personal_rating': 5.0,
        'publication_year': 2021,
        'genre': 'Science Fiction'
    },
    'The Marriage Portrait': {
        'author': 'Maggie OFarrell',
        'goodreads_rating': 4.02,
        'read_status': 'read',
        'personal_rating': 3.0,
        'publication_year': 2022,
        'genre': 'Historical Fiction'
    },
    'I Who Have Never Known Men': {
        'author': 'Jacqueline Harpman',
        'goodreads_rating': 4.24,
        'read_status': 'not read',
        'personal_rating': 'tbc',
        'publication_year': 1998,
        'genre': 'Dystopian Fiction'
    },
    'Big Swiss': {
        'author': 'Jen Beagin',
        'goodreads_rating': 4.70,
        'read_status': 'not read',
        'personal_rating': 'tbc',
        'publication_year': 2023,
        'genre': 'Contemporary'
    },
    'Yellowface': {
        'author': 'R.F Kuang',
        'goodreads_rating': 3.86,
        'read_status': 'read',
        'personal_rating': 3.0,
        'publication_year': 2023,
        'genre': 'Contemporary'
    },
    'Bright Young Women': {
        'author': 'Jessica Knoll',
        'goodreads_rating': 4.06,
        'read_status': 'not read',
        'personal_rating': 'tbc',
        'publication_year': 2023,
        'genre': 'Thriller'
    },
    'Lessons In Chemistry': {
        'author': 'Bonnie Garmus',
        'goodreads_rating': 4.31,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2022,
        'genre': 'Historical Fiction'
    },
    'Remarkably Bright Creatures': {
        'author': 'Shelby Van Pelt',
        'goodreads_rating': 4.41,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2022,
        'genre': 'Contemporary'
    },
    'Telephone': {
        'author': 'Percival Everett',
        'goodreads_rating': 3.97,
        'read_status': 'read',
        'personal_rating': 3.5,
        'publication_year': 2020,
        'genre': 'Contemporary'
    },
    'Annihilation': {
        'author': 'Jeff Vandermeer',
        'goodreads_rating': 3.76,
        'read_status': 'read',
        'personal_rating': 4.5,
        'publication_year': 2014,
        'genre': 'Science Fiction'
    },
    'Freshwater': {
        'author': 'Akwaeke Emezi',
        'goodreads_rating': 4.03,
        'read_status': 'read',
        'personal_rating': 3,
        'publication_year': 2020,
        'genre': 'Magical Realism'
    },
    'The Strange': {
        'author': 'Nathan Ballingrud',
        'goodreads_rating': 3.88,
        'read_status': 'read',
        'personal_rating': 3.5,
        'publication_year': 2023,
        'genre': 'Science Fiction'
    },
    'Daisy Jones And The Six': {
        'author': 'Taylor Jenkins Reid',
        'goodreads_rating': 4.22,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2019,
        'genre': 'Historical Fiction'
    },
    'Taste: My Life Through Food': {
        'author': 'Stanley Tucci',
        'goodreads_rating': 4.21,
        'read_status': 'read',
        'personal_rating': 4.5,
        'publication_year': 2021,
        'genre': 'Non Fiction'
    },
    'Rivers Of London (Rivers Of London, #1)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 3.86,
        'read_status': 'read',
        'personal_rating': 3.5,
        'publication_year': 2011,
        'genre': 'Urban Fantasy'
    },
    'Moon Over Soho (Rivers Of London, #2)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.09,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2011,
        'genre': 'Urban Fantasy'
    },
    'Whispers Underground (Rivers Of London, #3)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.15,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2012,
        'genre': 'Urban Fantasy'
    },
    'Broken Homes (Rivers Of London, #4)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.17,
        'read_status': 'read',
        'personal_rating': 4.5,
        'publication_year': 2013,
        'genre': 'Urban Fantasy'
    },
    'Foxglove Summer (Rivers Of London, #5)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.20,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2014,
        'genre': 'Urban Fantasy'
    },
    'The Hanging Tree (Rivers Of London, #6)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.22,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2016,
        'genre': 'Urban Fantasy'
    },
    'Lies Sleeping (Rivers Of London, #7)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.24,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2018,
        'genre': 'Urban Fantasy'
    },
    'False Value (Rivers Of London, #8)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.10,
        'read_status': 'read',
        'personal_rating': 4.0,
        'publication_year': 2020,
        'genre': 'Urban Fantasy'
    },
    'The Furthest Station (Rivers Of London, #5.5)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.10,
        'read_status': 'read',
        'personal_rating': 3.5,
        'publication_year': 2017,
        'genre': 'Urban Fantasy'
    },
    'Amongsr Our Weapons (Rivers Of London, #9)': {
        'author': 'Ben Aaronovitch',
        'goodreads_rating': 4.33,
        'read_status': 'read',
        'personal_rating': 4,
        'publication_year': 2022,
        'genre': 'Urban Fantasy'
    },
    'Red Rising (Red Rising Saga #1)': {
        'author': 'Pierce Brown',
        'goodreads_rating': 4.27,
        'read_status': 'read',
        'personal_rating': 4.5,
        'publication_year': 2014,
        'genre': 'Science Fiction'
    },
    'Golden Son (Red Rising Saga #2)': {
        'author': 'Pierce Brown',
        'goodreads_rating': 4.46,
        'read_status': 'read',
        'personal_rating': 4.5,
        'publication_year': 2015,
        'genre': 'Science Fiction'
    },
    'Morning Star (Red Rising Saga #3)': {
        'author': 'Pierce Brown',
        'goodreads_rating': 4.5,
        'read_status': 'not read',
        'personal_rating': 'tbc',
        'publication_year': 2016,
        'genre': 'Science Fiction'
    },
    'Iron Gold (Red Rising Saga #4)': {
        'author': 'Pierce Brown',
        'goodreads_rating': 4.24,
        'read_status': 'not read',
        'personal_rating': 'tbc',
        'publication_year': 2018,
        'genre': 'Science Fiction'
    },
    'Dark Age (Red Rising Saga #5)': {
        'author': 'Pierce Brown',
        'goodreads_rating': 4.46,
        'read_status': 'not read',
        'personal_rating': 'tbc',
        'publication_year': 2019,
        'genre': 'Science Fiction'
    }
}

with open('bookshelf.json', 'w') as json_file:
    json.dump(books_dict, json_file)
