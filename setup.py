import dataset

if __name__ == "__main__":
    taskbook_db = dataset.connect('sqlite:///taskbook.db')  
    task_table = taskbook_db.get_table('task')
    task_table.drop()
    task_table = taskbook_db.create_table('task')
    task_table.insert_many([
        {"date":"1/31/22", "description":"Do something useful", "completed":True},
        {"date":"1/31/22", "description":"Do something fantastic", "completed":False},
        {"date":"1/31/22", "description":"Do something remarkable",  "completed":False},
        {"date":"1/31/22", "description":"Do something unusual",  "completed":True}
    ])
    # this will have user's credentials for login
    user_cred_table = taskbook_db.create_table('user_cred')
     
