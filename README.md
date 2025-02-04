# TolltrafficKafka
# **Top Traffic Simulator**

## **Overview**
The Top Traffic Simulator simulates the passage of vehicles through toll plazas and streams the data to Kafka. The data consists of the timestamp, vehicle ID, vehicle type, and toll plaza ID. A Kafka consumer reads the data from Kafka and inserts it into a MySQL database for further analysis. The system is designed to demonstrate real-time data streaming from a producer to a consumer.

## **Kafka Producer - Data Streaming**

### **Functionality**
The producer generates simulated data for vehicles passing through toll plazas. It does so by creating random vehicle events with the following details:
- **Timestamp**: The exact time the vehicle passes the toll plaza.
- **Vehicle ID**: A unique identifier for each vehicle.
- **Vehicle Type**: The type of vehicle, which can be a car, truck, or van.
- **Toll Plaza ID**: An identifier for the toll plaza through which the vehicle passes.

The producer sends each generated vehicle event to the Kafka topic `toll`. These events are streamed continuously for a specified duration. Each event is printed for debugging purposes to indicate that the vehicle has passed through the toll plaza at the given timestamp.

---

## **Kafka Consumer - Data Processing**

### **Functionality**
The consumer listens to the `toll` Kafka topic for incoming messages. Each message contains information about a vehicle passing through a toll plaza. The consumer processes each message by:
- **Extracting Data**: The consumer extracts the timestamp, vehicle ID, vehicle type, and toll plaza ID from each Kafka message.
- **Timestamp Transformation**: The consumer transforms the timestamp into a suitable format for database storage.
- **Database Insertion**: The consumer inserts the extracted data into the `livetolldata` table in a MySQL database, allowing for storage and retrieval of traffic data.

Once the message is successfully inserted into the database, the consumer commits the transaction to ensure the data is saved.

---

## **Database Interaction**

The MySQL database is set up with a table named `livetolldata` to store the vehicle data. This table contains the following columns:
- **Timestamp**: A datetime field that stores the timestamp of when the vehicle passed through the toll plaza.
- **Vehicle ID**: An integer representing the unique identifier of the vehicle.
- **Vehicle Type**: A string representing the type of vehicle (e.g., car, truck, van).
- **Toll Plaza ID**: An integer representing the ID of the toll plaza where the vehicle passed.

The consumer continues to read messages from the Kafka topic and insert data into the database until the process is manually stopped or an error occurs.

---

## **Key Features**
- **Real-Time Data Streaming**: Simulated vehicle data is generated and streamed in real-time to Kafka.
- **Data Transformation**: The consumer transforms timestamps to the appropriate format before inserting them into the database.
- **Database Integration**: Data is stored in a MySQL database for easy querying and analysis of vehicle traffic at toll plazas.

--- 
