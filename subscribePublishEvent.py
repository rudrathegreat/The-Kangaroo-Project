def save_data(eventName, eventData, coreid, published_at, ttl ):
    import psycopg2 as psycopg2
    from psycopg2._psycopg import cursor, connection
    try:
        connection = psycopg2.connect(host="localhost", database="particle_electron", user="username",
                                      password="password")
        cursor = connection.cursor()
        insert_query = "INSERT INTO SUBSCRIBED_EVENTS (COREID, EVENT_NAME, EVENT_DATA, PUBLISHED_AT, TTL) VALUES ('" + coreid + "' ,'" + eventName + "' , '" + eventData + "', '" + published_at + "', '" + ttl + "')"
        # print(insert_query)
        cursor.execute(insert_query)
        connection.commit()
        print("Record inserted successfully into SUBSCRIBED_EVENTS table")
    except psycopg2.DatabaseError as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into SUBSCRIBED_EVENTS table {}".format(error))
    finally:
        # closing database connection.
        cursor.close()
        connection.close()
        print("Database connection is closed")


import simplejson as json
from sseclient import SSEClient

messages = SSEClient('https://api.particle.io/v1/devices/events/event-name?access_token=YourAuthToken')

for msg in messages:
    eventName = str(msg.event)#.encode('utf-8')
    data = str(msg.data)#.encode('utf-8')
    # print(event)
    # print(data)
    if data:
        dataJson = json.loads(data)
        print(dataJson)
        eventData = dataJson["data"]
        coreid = dataJson["coreid"]
        published_at = dataJson["published_at"]
        ttl = str(dataJson["ttl"])
        save_data(eventName, eventData, coreid, published_at, ttl)