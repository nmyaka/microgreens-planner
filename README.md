# Microgreens Planner Project

## Overview
The **Microgreens Planner** is a cloud-based application designed to help users track the growth stages of their microgreens batches. It provides endpoints to add, update, retrieve, and delete batch details, enabling streamlined monitoring and management.

This project utilizes **AWS Lambda**, **API Gateway**, and **DynamoDB**, allowing for a fully serverless implementation. The application integrates with AWS services and offers scalability, low-cost operation, and ease of deployment.

---

## Features
- **Add Batch**: Create a new microgreens batch with details such as plant date, harvest date, and condition.
- **Update Batch**: Update specific attributes of an existing batch.
- **Retrieve Batch**: Fetch the details of a specific batch by ID.
- **Retrieve All Batches**: List all stored batches.
- **Delete Batch**: Remove a batch from the tracker.

---

## Architecture
This project follows a serverless architecture leveraging:
1. **AWS Lambda** for backend logic.
2. **API Gateway** for RESTful API endpoints.
3. **DynamoDB** as the data store.

---

## Prerequisites
1. **AWS Account**.
2. Installed tools:
   - [AWS CLI](https://aws.amazon.com/cli/)
   - [Postman](https://www.postman.com/) or any API testing tool.
   - [Git](https://git-scm.com/).
   - Python 3.x (if developing locally).
3. Knowledge of Python and AWS services.

---

## Project Setup

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd microgreens-planner
```

### Step 2: Deploy the Project to AWS

#### Create DynamoDB Table
1. Go to the **AWS Console** → DynamoDB.
2. Create a new table with the following details:
   - **Table Name**: `MicrogreensTable` (or your preferred name)
   - **Primary Key**: `id` (String)

#### Deploy Lambda Functions
1. Navigate to the AWS Lambda console.
2. Create separate functions for `POST`, `GET`, `GETALL`, `DELETE`, and `PUT` requests.
3. Upload the respective function code from the `src/` directory.
4. Add an environment variable for the table name:
   - Key: `TABLE_NAME`
   - Value: `MicrogreensTable`

#### Configure API Gateway
1. Create a REST API in **API Gateway**.
2. Define the following endpoints:
   - `POST /microgreens`
   - `GET /microgreens/{id}`
   - `GET /microgreens`
   - `PUT /microgreens/{id}`
   - `DELETE /microgreens/{id}`
3. Integrate each endpoint with the corresponding Lambda function using the **AWS_PROXY** integration.

#### Test the API
- Use Postman or curl to test each endpoint.

### Step 3: Deploy the Application
After testing, deploy the API to a stage (e.g., `dev`, `prod`).

---

## Sample API Requests

### Add a Batch (POST)
**Endpoint**: `/microgreens`
```json
{
  "batchName": "Sunflower Batch",
  "plantDate": "2025-01-10",
  "harvestDate": "2025-01-20",
  "status": "Planted"
}
```

### Update a Batch (PUT)
**Endpoint**: `/microgreens/{id}`
```json
{
  "status": "Harvested"
}
```

### Get a Batch by ID (GET)
**Endpoint**: `/microgreens/{id}`

### Get All Batches (GET)
**Endpoint**: `/microgreens`

### Delete a Batch (DELETE)
**Endpoint**: `/microgreens/{id}`

---

## Future Enhancements
- Add a simple front-end interface for visualizing batches.
- Integrate notifications for batch status updates.

---

## License
This project is personal project.

---

## Acknowledgements
- AWS Documentation
- OpenAI ChatGPT for guidance
