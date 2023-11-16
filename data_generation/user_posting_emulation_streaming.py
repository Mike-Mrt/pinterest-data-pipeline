# Importing the necessory python script:
from user_posting_emulation import *

# Initialising the AWSDBConnector Class:
new_connector = AWSDBConnector()

random.seed(100)


def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            # Send data to my Kinesis streams using the API Invoke URL:
            # Data from the 3 tables should be sent their corresponding Kinesis stream:
            # Using the Python requests library for sending the data messages to an AWS API Gateway using the invoke URL:
            # Introducing the headers variable:
            headers = {'Content-Type': 'application/json'}
            # user data:
            # To send JSON messages:
            payload_user = json.dumps(
                {"StreamName": "streaming-0e1f6d6285c1-user",
                "Data": {
                        #Data should be send as pairs of column_name:value, with different columns separated by commas      
                        "ind": user_result["ind"], "first_name": user_result["first_name"], "last_name": user_result["last_name"], "age": user_result["age"], "date_joined": user_result["date_joined"].isoformat()
                        },
                "PartitionKey": "user_partition"}
            )
            response_user = requests.request("PUT", "https://ke1nd2q27d.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0e1f6d6285c1-user/record", headers=headers, data=payload_user)
            
            # geo data:
            # To send JSON messages:
            payload_geo = json.dumps(
                {"StreamName": "streaming-0e1f6d6285c1-geo",
                "Data": {
                        #Data should be send as pairs of column_name:value, with different columns separated by commas      
                        "ind": geo_result["ind"], "timestamp": geo_result["timestamp"].isoformat(), "latitude": geo_result["latitude"], "longitude": geo_result["longitude"],"country": geo_result["country"]
                        },
                "PartitionKey": "geo_partition"}
            )
            response_geo = requests.request("PUT", "https://ke1nd2q27d.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0e1f6d6285c1-geo/record", headers=headers, data=payload_geo)

            # pin data:
            # To send JSON messages
            payload_pin = json.dumps(
                {"StreamName": "streaming-0e1f6d6285c1-pin",
                "Data": {
                        #Data should be send as pairs of column_name:value, with different columns separated by commas      
                        "index": pin_result["index"], "unique_id": pin_result["unique_id"], "title": pin_result["title"], "description": pin_result["description"],"poster_name": pin_result["poster_name"],"follower_count": pin_result["follower_count"],"tag_list": pin_result["tag_list"],"is_image_or_video": pin_result["is_image_or_video"],"image_src": pin_result["image_src"],"downloaded": pin_result["downloaded"],"save_location": pin_result["save_location"],"category": pin_result["category"]
                        },
                "PartitionKey": "pin_partition"}
            )
            response_pin = requests.request("PUT", "https://ke1nd2q27d.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0e1f6d6285c1-pin/record", headers=headers, data=payload_pin)


            if response_user.status_code == 200 and response_geo.status_code == 200 and response_pin.status_code == 200:
                print("Data sent to Kinesis streams.")
            else:
                print("Failed to sent data to Kinesis streams")


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


