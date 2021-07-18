import dataset

if __name__ == "__main__":
    todo_list_db = dataset.connect('sqlite:///hobby_list.db')
    todo_table = todo_list_db.get_table('hobby')
    todo_table.drop()
    hobby_table = todo_list_db.create_table('hobby')
    hobby_table.insert_many([
        { 'hobby' : 'Hiking', 'years' : 5 },
        { 'hobby' : 'Working out', 'years' : 12 },
        { 'hobby' : 'Playing guitar', 'years' : 8 },
        { 'hobby' : 'Playing drums', 'years' : 4 },
    ])