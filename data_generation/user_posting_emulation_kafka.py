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
            
            # Send data to my Kafka topics using the API Invoke URL:
            # Data from the 3 tables should be sent their corresponding Kafka topic:
            # Using the Python requests library for sending the data messages to an AWS API Gateway using the invoke URL:
            # pin data:
            payload_pin = json.dumps({
                "records": [
                    {
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": {"index": pin_result["index"], "unique_id": pin_result["unique_id"], "title": pin_result["title"], "description": pin_result["description"],"poster_name": pin_result["poster_name"],"follower_count": pin_result["follower_count"],"tag_list": pin_result["tag_list"],"is_image_or_video": pin_result["is_image_or_video"],"image_src": pin_result["image_src"],"downloaded": pin_result["downloaded"],"save_location": pin_result["save_location"],"category": pin_result["category"]}
                    }
                ]
            })
            headers_1 = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            response_pin = requests.request("POST", "https://ke1nd2q27d.execute-api.us-east-1.amazonaws.com/dev/topics/0e1f6d6285c1.pin", headers=headers_1, data=payload_pin)

            # geo data:

            payload_geo = json.dumps({
                "records": [
                    {
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": {"ind": geo_result["ind"], "timestamp": geo_result["timestamp"].isoformat(), "latitude": geo_result["latitude"], "longitude": geo_result["longitude"],"country": geo_result["country"]}
                    }
                ]
            })
            headers_2 = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            response_geo = requests.request("POST", "https://ke1nd2q27d.execute-api.us-east-1.amazonaws.com/dev/topics/0e1f6d6285c1.geo", headers=headers_2, data=payload_geo)

            # user data:

            payload_user = json.dumps({
                "records": [
                    {
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": {"ind": user_result["ind"], "first_name": user_result["first_name"], "last_name": user_result["last_name"], "age": user_result["age"],"date_joined": user_result["date_joined"].isoformat()}
                    }
                ]
            })
            headers_3 = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            response_user = requests.request("POST", "https://ke1nd2q27d.execute-api.us-east-1.amazonaws.com/dev/topics/0e1f6d6285c1.user", headers=headers_3, data=payload_user)

            # checking to see if successfully sent data or not:
            if response_pin.status_code == 200 and response_geo.status_code == 200 and response_user.status_code == 200:
                print("Data sent to Kafka topic successfully.")
            else:
                print("Failed to send data to Kafka topic")


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


