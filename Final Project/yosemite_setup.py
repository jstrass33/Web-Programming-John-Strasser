import dataset

if __name__ == "__main__":
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    yosemite_table = nationalpark_db.get_table('yosemite')
    yosemite_table.drop()
    yosemite_table = nationalpark_db.create_table('yosemite')
    yosemite_table.insert_many([

        {'username' : 'jstrasse', 'comment' : 'This is a random comment',}
        
        
    ])