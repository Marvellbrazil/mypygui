import connection as conpy

def create(name, age, email):
    conn = conpy.get_connection()
    if conn is None:
        return
    
    cur = conn.cursor()
    
    query = "INSERT INTO user (name, age, email) VALUES (?, ?, ?)"
    params = [name, age, email]
    cur.execute(query, params)

    conn.commit()
    cur.close()
    conn.close()

def read():
    conn = conpy.get_connection()
    if conn is None:
        return []
    
    cur = conn.cursor()
    
    query = "SELECT * FROM user"
    cur.execute(query)
    
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return rows

def update(id, name, age, email):
    conn = conpy.get_connection()
    
    if conn is None:
        return
    
    cur = conn.cursor()
    
    query = """
        UPDATE user
        SET name = ?, age = ?, email = ?
        WHERE id = ?
    """
    params = [name, age, email, id]
    cur.execute(query, params)
    
    conn.commit()
    cur.close()
    conn.close()

def delete(id):
    conn = conpy.get_connection()
    if conn is None:
        return
    
    cur = conn.cursor()
    
    query = "DELETE FROM user WHERE id = ?"
    param = [id]
    cur.execute(query, param)
    
    conn.commit()
    cur.close()
    conn.close()

def get(id):
    conn = conpy.get_connection()
    if conn is None:
        return []
    
    cur = conn.cursor()
    
    query = "SELECT * FROM user WHERE id = ?"
    param = [id]
    
    cur.execute(query, param)
    
    res = cur.fetchone
    
    if res is None:
        return
    
    cur.close()
    conn.close()
    return res
