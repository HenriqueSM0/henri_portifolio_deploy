from django.db import connection

class Habilidade :
    
    def create_tab_habs () :
         with connection.cursor() as cursor :
            cursor.execute('''CREATE TABLE IF NOT EXISTS habs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name varchar(60) UNIQUE,
                    level VARCHAR(15) 
                )''')
    
    def create_hab (name, level) :
        with connection.cursor() as cursor :
            cursor.execute(f'''
                INSERT INTO habs (name, level) VALUES ('{name}', '{level}')
        ''')
    
    def get_habs () :
        with connection.cursor() as cursor :
            cursor.execute('''SELECT * FROM habs''')
            return cursor.fetchall()
    
    def remove_hab (id) :
        with connection.cursor() as cursor :
            cursor.execute(f'''DELETE FROM habs WHERE id = {id}''')

class Projeto :

    def create_tab_projs () :
         with connection.cursor() as cursor :
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name varchar(60) UNIQUE,
                    description TEXT,
                    link_rep VARCHAR(300),
                    link_you VARCHAR(300)
                )
            ''')

    def create_proj (name, description, link_rep, link_you) :
        with connection.cursor() as cursor :
            if (link_you == '') :
                cursor.execute(f'''
                    INSERT INTO projs (name, description, link_rep) VALUES ('{name}', '{description}', '{link_rep}')
                ''')
            else :
                cursor.execute(f'''
                    INSERT INTO projs (name, description, link_rep, link_you) 
                               VALUES ('{name}', '{description}', '{link_rep}', '{link_you}')
                ''')
    
    def get_projs () :
        with connection.cursor() as cursor :
            cursor.execute(''' SELECT * FROM projs''')
            return cursor.fetchall()
