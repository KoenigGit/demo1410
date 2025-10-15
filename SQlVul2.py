def secure_login(username, password):
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()

    # ✅ SAFE: Use parameterized queries
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cur.execute(query, (username, password))

    result = cur.fetchone()
    conn.close()
    return result
