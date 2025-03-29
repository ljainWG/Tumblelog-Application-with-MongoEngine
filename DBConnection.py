from mongoengine import connect, disconnect

class MyMongoDB:
    def __init__(self, db_name, host="localhost", port=27017):
        self.db_name = db_name
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """Establish a connection to MongoDB."""
        try:
            self.connection = connect(db=self.db_name, host=self.host, port=self.port)
            print(f"Connected to MongoDB: {self.db_name}")
        except Exception as e:
            print(f"Connection failed: {e}")

    def disconnect(self):
        """Disconnect from MongoDB."""
        try:
            disconnect(alias="default")  # Close the default connection
            print("Disconnected from MongoDB.")
        except Exception as e:
            print(f"Disconnection failed: {e}")
