def stream_user_data(connection):
    """
    Generator that yields user data one row at a time.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()
