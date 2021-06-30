import dataset

if __name__ == "__main__":
    todo_list_db = dataset.connect('sqlite:///todo_list.db')
    todo_table = todo_list_db.get_table('todo')
    

    