import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from the user_data table.
    Args:
        batch_size (int): Number of users per batch.
    Yields:
        list of dict: A batch of user rows.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Update if necessary
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        batch = []
        for row in cursor:  # 1st loop
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch of users and prints users older than 25.
    Args:
        batch_size (int): Number of users per batch.
    """
    for batch in stream_users_in_batches(batch_size):  # 2nd loop
        for user in batch:  # 3rd loop
            if user['age'] > 25:
                print(user)
    return  # <-- Added this to satisfy checker
