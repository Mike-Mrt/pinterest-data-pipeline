# Pinterest Data Pipeline project
Pinterest is a platform which leverages immense amounts of data to personalise their users experience - this project aims to replicate a similar data pipeline system using the power of AWS Cloud.

## Table of Contents

- [Introduction](#introduction)
- [Learning Outcomes](#learning-outcomes)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure of the Project](#file-structure-of-the-project)
- [License Information](#license-information)

## Introduction

The current state of most companies, from large financial corporations to small businesses, is that they are becoming highly data driven. Therefore, understanding how to efficiently collect, transform and analyse data is essential to not only comptete but to thrive in this current environment. This project showcases a data pipeline that integrates both batch and streaming data processing. Through the integration of AWS cloud the system that has been designed is not only scalable and highly secure but also reliable and cost efficient by having the ability to adapt to flcutuating data volumes and computational demands. 

This system requires the use of several of the AWS services, including: 

- AWS EC2 (virtual servers in the cloud)
- AWS S3 (scalable storage in the cloud)
- AWS IAM (manage access to AWS resources)
- AWS MSK (fully managed, highly scalable, and secure service for Apache Kafka)
- AWS API Gateway (build, deploy and manage APIs)
- AWS MWAA (a managed service for Apache Airflow to orchestrate workflows)
- Kinesis (processing real-time streaming data)

To ensure that all fo these components work together to create a robust data pipeline we also require:

- Apache Kafka
- Apache Spark
- Apache Airflow
- Databricks
- Couple of GitHub packages which will aid in IAM authentication and package to communicate with the MSK cluster.
- GitHub (version control platform)

The details of all of the packages utilised within this project will be outlined in the [Installation Instructions](#installation-instructions).

## Learning Outcomes

The learning outcomes of the project can be laid out step by step as each section of the data pipeline gets implemented:

1. Creating a data creation file which outputs rows from 3 different tables stored in an S3 bucket that contain data for the users, geolocation and pinterest posts.
2. Setting up an AWS account (usually provided by organisation).
3. Setting up an EC2 instance and connect to it via the terminal using SSH, the keypair (.pem) file and the name of the EC2 instance. 
4. Downloading and setting up Apache Kafka on the EC2 instance, to do this you need to download Kafka directly onto the EC2 instace. However, to do this also need to install javajdk.
5. Downloading and setting up the IAM authentication package on the EC2 instance so that connectivity can be established to the MSK cluster via IAM authentication.
6. Now the topics can be created by editing the server.properties file appropriately with the Plaintext Apache Zookeeper connection string and using the Bootstrap server string in the command.
7. MSK cluster will then be connected to an S3 bucket so that any data going through the cluster will be automatically saved and stored in a dedicated S3 bucket. A custom plugin was created in MSK Connect and then a connector was created.
8. Creating and configuring an API in API gateway that will send data to the MSK cluster which in turn will be stored in an S3 bucket. Building a Proxy integration for the API and took note of the Invoke URL. Set up the Kafka REST proxy on the EC2 client and then the REST proxy can be initiated. By modifying the data creation file in step 1, we send the data created to the Kafka topics I created earlier using the API Invoke URL. 
9. Setting up a Databricks account and using a notebook within this to Mount the S3 bucket which contains JSON files as data for each of the 3 topics to Databricks. 
10. Once the S3 bucket has been mounted, the data can be read and 3 spark dataframes were created for each of the tables: users, geolocation and pinterest posts data. These 3 tables were then cleaned by changing columns orders, column data types, ensuring the data was coherent (e.g. follower_count had values such as 2M, 100k etc so had to change these to integers). 
11. Once the 3 tables were cleaned, analysis was performed on these tables by joining them when necessary and running computations on Databricks but utilising Spark. 
12. Writing up a DAG which will trigger the above Databricks notebook at a determined schedule through the use of the AWS MWAA. This will allow workflows to be managed on Databricks. 
13. The next step is setting up data streams to Kinesis and then reading the this data in Databricks. Firstly, 3 data streams were created in the AWS Kinesis for each of the 3 tables (Pinterest posts data, geolocation data and user data).
14. Configuring an API (in AWS API Gateway) with Kinesis proxy integration to allow it to invoke Kinesis actions. The API created will be able to invoke the following actions: list streams in Kinesis, create, describe and delete streams in Kinesis and add records to streams in Kinesis.
15. Updating the user_posting_emulation_streaming.py file to enable the data generated to be sent to the Kinesis streams by sending it as JSON payloads and invoking the API.
16. Reading the data into spark dataframes, however, the dataframe columns are as follows: partitionKey, data, stream, shardId, seuquenceNumber, approximateArrivalTimestamp.
17. The data column of the above dataframe is then deserialised and another dataframe is created with one column ('data') which contains rows of JSON strings. 
18. The 'data' column is then parsed by created a JSON schema and the dataframe is converted into the required dataframes: Pinterest posts, geolocation and user data.
19. Transformations are then performed on the 3 dataframes to ensure all data is coherent and ready for analytics. 
20. Writing the 3 dataframes to Databricks Delta tables, once this is done the Delta tables can be queried easily to extract business intelligence from the data. 


## Installation Instructions

The project is proprietary data and therefore, detailed instructions of how to install the exact packages required cannot be outlined. However, the programming language used is Python 3 and SQL for database querying purposes. All other AWS services and technologies used have been outlined in the [Introduction](#introduction).

## Usage Instructions

The project is proprietary, therefore not all files have been uploaded to the GitHub repository. Therefore, it is not possible to provide usage instructions. However, the [Learning Outcomes](#learning-outcomes) has outlined all the steps taken to get this system set up. 

## File Structure of the Project

The GitHub repo for this project can be found here: [Pinterest Data Pipeline project](https://github.com/Mike-Mrt/pinterest-data-pipeline).

The current filestructure is as follows:

- pinterest-data-pipeline
  - README.md
  - data_generation
    - db_creds.yaml (file containing credentials - not visible in GitHub)
    - user_posting_emulation.py
    - user_posting_emulation_kafka.py
    - user_posting_emulation_streaming.py
  - data_transformations
    - transformations.ipynb
  - batch_processing
    - batch_data_processing.ipynb
    - 0e1f6d6285c1_dag.py
  - stream_processing
    - stream_data_processing.ipynb

## License Information

This project is proprietary and is not open source. However, the code that has been designated as viewable may be used for educational purposes. 

