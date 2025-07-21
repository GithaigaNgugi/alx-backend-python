seed = __import__('seed')


def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age
    connection.close()


def compute_average_age():
    """
    Uses the generator to compute the average age of users
    without loading the full dataset into memory.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    average = total_age / count if count else 0
    print(f"Average age of users: {average:.2f}")


if __name__ == "__main__":
    compute_average_age()
