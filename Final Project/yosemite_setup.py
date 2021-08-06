import dataset

if __name__ == "__main__":
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    yosemite_table = nationalpark_db.get_table('olympic')
    yosemite_table.drop()
    yosemite_table = nationalpark_db.create_table('olympic')
    yosemite_table.insert_many([

        {'username' : 'jstrasse', 'comment' : 'This is a random comment','date' : 'Test Date',}
        
        
    ])