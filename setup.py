import dataset

if __name__ == "__main__":
    taskbook_db = dataset.connect('sqlite:///taskbook.db')  
    task_table = taskbook_db.get_table('task')
    task_table.drop()
    task_table = taskbook_db.create_table('task')
    task_table.insert_many([
        # yyyy-mm-dd is what the datepicker gives so I had to change the date format. We have to keep consistent
        {"email":"default@gmail.com", "date":"2022-01-15", "time":"bhu765rfghu76" , "description":"Do something useful", "completed":True},
        {"email":"default@gmail.com", "date":"2022-01-15", "time":"bhu765rfghu76" , "description":"Do something fantastic", "completed":False},
        {"email":"default@gmail.com", "date":"2022-01-15", "time":"bhu765rfghu76" , "description":"Do something remarkable",  "completed":False},
        {"email":"default@gmail.com", "date":"2022-01-15", "time":"bhu765rfghu76" , "description":"Do something unusual",  "completed":True}
    ])
    # this will have user's credentials for login
    user_cred_table = taskbook_db.get_table('user_cred')
    user_cred_table.drop()
    user_cred_table = taskbook_db.create_table('user_cred')
    user_cred_table.insert_many([
        {"email": "default@gmail.com", "password": "sha256$MWSvDicsNpLC4mKz$767f39b1d4304c4e8d4c23a98b1d4a114c787aedfa6a9debd1cf91149e501c96", "view": "calendar"},
        {"email": "admin@gmail.com", "password": "sha256$e4KT8L8fawrboJm9$6aaffaf92b606400df0109d34c417d5dd9e588991487e0912a4cc28f73a0fd87", "view": "weekly"}
    ])
     
