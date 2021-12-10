import dataset

if __name__ == "__main__":
    taskbook_db = dataset.connect('sqlite:///taskbook.db')  
    task_table = taskbook_db.get_table('task')
    task_table.drop()
    task_table = taskbook_db.create_table('task')
    task_table.insert_many([
        # yyyy-mm-dd is what the datepicker gives so I had to change the date format. We have to keep consistent
        {"date":"2022-01-15", "description":"Do something useful", "completed":True},
        {"date":"2022-01-15", "description":"Do something fantastic", "completed":False},
        {"date":"2022-01-15", "description":"Do something remarkable",  "completed":False},
        {"date":"2022-01-15", "description":"Do something unusual",  "completed":True}
    ])
    # this will have user's credentials for login
    user_cred_table = taskbook_db.create_table('user_cred')
     
