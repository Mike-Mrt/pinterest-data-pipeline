# Pinterest Data Pipeline project
Pinterest utilises billions of data to ensure its customers are provided with their preferences. In this project, a similar system is designed utilising AWS Cloud, the details of this will follow.

## Table of Contents

- [Introduction](#introduction)
- [Learning Outcomes](#learning-outcomes)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure of the Project](#file-structure-of-the-project)
- [License Information](#license-information)

## Introduction

The Pinterest data pipeline simulation project will in effect use many components of the AWS ecosystem combined with Databricks to build a data pipeline. Ths pipeline will incorporate both batch data and streaming data to ensure that the pipeline is robust and utilise the cloud so that the the pipeline is scalable, cost- efficient, highly secure, reliable and completely flexible according to the volume of data and compute resources utilised by the system. This will ensure the incoming data is clean and ready to be analysed to ensure the customer has the most optimised Pinterest feed according to their personal preferences. 

This project utilises many components from the AWS ecosystem to build the pipeline, these include:

- AWS EC2 (virtual servers in the cloud)
- AWS S3 (scalable storage in the cloud)
- AWS IAM (manage access to AWS resources)
- AWS MSK (fully managed, highly scalable, and secure service for Apache Kafka)
- AWS API Gateway (build, deploy and manage APIs)
- AWS MWAA (a managed service for Apache Airflow to orchestrate workflows)

To ensure that all fo these components work together to create a robust data pipeline we also require:

- Apache Kafka
- Apache Spark
- Apache Airflow
- Apache Kinesis
- Databricks
- Couple of GitHub packages which will aid in IAM authentication and package to communicate with the MSK cluster.
- GitHub (version control platform)

The details of all of the packages utilised within this project will be outlined in the [Installation Instructions](#installation-instructions).

## Learning Outcomes

The learning outcomes of the project can be laid out step by step as each section of the data pipeline gets implemented:

1. Creating a data creation file which outputs rows from 3 different tables stored in an S3 bucket that contain data for the users, geolocation and pinterest posts.
2. Set up an AWS account (usually provided by organisation).
3. Set up an EC2 instance and connect to it via the terminal using SSH, the keypair (.pem) file and the name of the EC2 instance. 
4. Download and set up Apache Kafka on the EC2 instance, to do this you need to download Kafka directly onto the EC2 instace. However, to do this also need to install javajdk.
5. Download and set up the IAM authentication package on the EC2 instance so that connectivity can be established to the MSK cluster via IAM authentication.
6. Now the topics can be created by editing the server.properties file appropriately with the Plaintext Apache Zookeeper connection string and using the Bootstrap server string in the command.
7. MSK cluster will then be connected to an S3 bucket so that any data going through the cluster will be automatically saved and stored in a dedicated S3 bucket. A custom plugin was created in MSK Connect and then a connector was created.
8. Create and configure an API in API gateway that will send data to the MSK cluster which in turn will be stored in an S3 bucket. Built a Proxy integration for the API and took note of the Invoke URL. Set up the Kafka REST proxy on the EC2 client and then the REST proxy can be initiated. By modifying the data creation file in step 1, we send the data created to the Kafka topics I created earlier using the API Invoke URL. 
9. Need to set up a Databricks account and use a notebook within this to Mount the S3 bucket which contains JSON files as data for each of the 3 topics to Databricks. 
10. Once the S3 bucket has been mounted, the data can be read and 3 spark dataframes were created for each of the tables: users, geolocation and pinterest posts data. These 3 tables were then cleaned by changing columns orders, column data types, ensuring the data was coherent (e.g. follower_count had values such as 2M, 100k etc so had to change these to integers). 
11. Once the 3 tables were cleaned, analysis was performed on these tables by joining them when necessary and running computations on Databricks but utilising Spark. 
12. Writing up a DAG which will trigger the above Databricks notebook at a determined schedule through the use of the AWS MWAA. This will allow workflows to be managed on Databricks. 

## Installation Instructions

Detailed steps on how to install the project.

## Usage Instructions

Instructions on how to use the project if you want to test it.

## File Structure of the Project

The GitHub repo for this project can be found here: [Pinterest Data Pipeline project](https://github.com/Mike-Mrt/pinterest-data-pipeline).

The current filestructure is as follows:

- pinterest-data-pipeline
  - README.md
  - Batch_Data_processing.ipynb
  - 0e1f6d6285c1_dag.py

## License Information

Licensing details for the project.



