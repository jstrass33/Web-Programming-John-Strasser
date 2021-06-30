import dataset

if __name__ == "__main__":
    todo_list_db = dataset.connect('sqlite:///todo_list_john.db')
    todo_table = todo_list_db.get_table('todo')
    todo_table.drop()
    todo_table = todo_list_db.create_table('todo')
    todo_table.insert_many([
         {'task':'Figure out how to write Python with database','done': 0},
            {'task':'Practice the syntax for this','done': 0},
          {'task':'Continue to work on this stupid database stuff','done': 0},

    ])