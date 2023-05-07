import DBInfo
import pymysql
def pull_data():
    class QueryClass:
        Table = "Order"

    query = "SELECT * FROM `Order` ORDER BY RAND() LIMIT 2"

    # Class that stores the creds to connect
    db_info = DBInfo.DB()

    # Open database connection
    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database,
                             port=3316) as db:
            cursor = db.cursor()
            cursor.execute(query)

            # Fetch all the rows
            rows = cursor.fetchall()
            api_key_objects = []

            # Process the rows
            for row in rows:
                api_key_object = row[1], row[2], row[4], row[3]
                api_key_objects.append(api_key_object)

            return api_key_objects
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}")