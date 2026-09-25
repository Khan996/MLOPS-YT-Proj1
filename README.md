

 # 🚀 End-to-End MLOps Machine Learning Platform

 > **Production-oriented machine learning project demonstrating the complete ML lifecycle — from data ingestion and validation to model training, evaluation, deployment, and CI/CD on AWS.**

 

---

 ## 🎯 Project Overview

 This project is designed as a **complete end-to-end MLOps system**, covering the major stages required to move a machine learning solution from experimentation into a deployable production environment.

 Instead of treating machine learning as simply:


Dataset → Model → Prediction


 this project implements a structured workflow:


                         ┌─────────────────────┐
                         │      MongoDB Atlas   │
                         │    Data Repository  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Data Ingestion     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Data Validation    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Data Transformation  │
                         │ + Feature Engineering│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Model Training    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Model Evaluation   │
                         └──────────┬──────────┘
                                    │
                           Model meets threshold?
                              /            \
                            YES             NO
                             │               │
                             ▼               └──► Stop / Retrain
                    ┌─────────────────┐
                    │   Model Pusher  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    AWS S3       │
                    │ Model Registry   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Docker Image    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    │     CI/CD       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ AWS EC2 Server  │
                    │   Production    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Prediction App  │
                    │     /training   │
                    │     /predict    │
                    └─────────────────┘


---

 # 🧠 What This Project Demonstrates

 This project showcases practical experience across several areas of modern machine learning engineering.

 ### Machine Learning

- Exploratory Data Analysis (EDA)
- Feature engineering
- Data validation
- Data transformation
- Model training
- Model evaluation
- Model selection
- Model registry / model storage
- Prediction pipeline

 ### Software Engineering

- Modular project architecture
- Custom configuration management
- Entity/artifact based design
- Logging
- Exception handling
- Reusable utility modules
- Package management
- Virtual environments
- Separation of components and responsibilities

 ### Data Engineering

- MongoDB Atlas integration
- Python-to-MongoDB connectivity
- Dataset ingestion
- NoSQL document retrieval
- Data transformation into Pandas DataFrames

 ### Cloud & MLOps

- AWS IAM
- AWS S3
- AWS ECR
- AWS EC2
- Docker
- GitHub Actions
- Self-hosted GitHub Actions runner
- Automated deployment
- Model artifact management

 ### Application Development

- Flask-based prediction application
- Training endpoint
- Prediction endpoint
- Static assets
- HTML templates

---

 # 🏗️ Project Architecture

 The application follows a component-based architecture where each stage of the ML lifecycle has a dedicated responsibility.


src/
│
├── components/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   ├── model_evaluation.py
│   └── model_pusher.py
│
├── configuration/
│   ├── mongo_db_connections.py
│   └── aws_connection.py
│
├── data_access/
│   └── proj1_data.py
│
├── entity/
│   ├── config_entity.py
│   ├── artifact_entity.py
│   ├── estimator.py
│   └── s3_estimator.py
│
├── utils/
│   └── main_utils.py
│
├── constants/
│   └── __init__.py
│
└── pipeline/
    └── training_pipeline.py


 Application layer:


app.py
│
├── /predict
│
└── /training


 Supporting infrastructure:


.github/
└── workflows/
    └── aws.yaml

Dockerfile
.dockerignore
requirements.txt
setup.py
pyproject.toml
config/
└── schema.yaml

notebook/
├── dataset
├── mongoDB_demo.ipynb
└── EDA / Feature Engineering notebooks


---

 # 🔄 ML Pipeline

 ## 1\. Data Ingestion

 The pipeline connects to **MongoDB Atlas**, retrieves documents in key-value format, and converts them into a structured Pandas DataFrame.

 ### Workflow


MongoDB Atlas
      ↓
MongoDB Connection
      ↓
Data Access Layer
      ↓
Document Retrieval
      ↓
DataFrame
      ↓
Ingestion Artifact


 The ingestion component is responsible for:

- Connecting to MongoDB
- Reading the dataset
- Converting NoSQL documents into tabular data
- Persisting the required artifacts
- Passing structured data to downstream components

---

 # ✅ 2. Data Validation

 The validation layer ensures that incoming data conforms to the expected dataset structure.

 The project uses a schema configuration file:


config/schema.yaml


 The schema can define information such as:

- Number of columns
- Column names
- Data types
- Numerical features
- Categorical features
- Required fields
- Dataset structure

 ### Validation workflow


Incoming Dataset
       ↓
Schema Configuration
       ↓
Data Validation
       ↓
Validation Report
       ↓
Valid Dataset


 This creates a separation between **data expectations** and **validation implementation**.

---

 # 🛠️ 3. Data Transformation

 After validation, the dataset enters the transformation stage.

 This stage handles:

- Feature engineering
- Data preprocessing
- Numerical transformations
- Categorical transformations
- Missing-value handling
- Preparation of model-ready features

 The transformation process produces artifacts that can be consumed consistently by the model training component.

---

 # 🤖 4. Model Training

 The model trainer receives transformed training data and trains the machine learning model.

 The project uses an estimator abstraction to keep model-related functionality organized.


Transformed Dataset
        ↓
Model Trainer
        ↓
Estimator
        ↓
Trained Model
        ↓
Model Artifact


 The training component can be extended to support different machine learning algorithms without redesigning the complete pipeline.

---

 # 📊 5. Model Evaluation

 A trained model is not automatically considered production-ready.

 The model evaluation component compares the newly trained model against the existing/reference model using a configurable performance threshold.

 Example configuration:


MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02


 Conceptually:


New Model
    │
    ▼
Evaluate Performance
    │
    ▼
Compare Against Existing Model
    │
    ├── Improvement ≥ Threshold
    │          ↓
    │      Accept Model
    │
    └── Improvement < Threshold
               ↓
          Reject Model
```

 This introduces an important MLOps concept:

 > **Model deployment should be conditional on measurable performance rather than simply occurring after every training run.**

---

 # ☁️ 6. Model Registry / Model Pusher

 Approved models are pushed to **AWS S3**, providing centralized model artifact storage.

 Example configuration:


MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"


 The project includes:


entity/
└── s3_estimator.py


 for model-related S3 operations.

 ### Model lifecycle


Trained Model
      ↓
Model Evaluation
      ↓
Performance Threshold
      ↓
Approved?
      ↓
AWS S3
      ↓
Model Registry


---

 # 🌐 Prediction Pipeline

 The project includes a separate prediction pipeline to make the trained model accessible through a web application.


User Input
    ↓
Flask Application
    ↓
Prediction Pipeline
    ↓
Preprocessing
    ↓
Loaded Model
    ↓
Prediction
    ↓
Web Response


 The application contains routes such as:


/predict
/training


 ### `/predict`

 Provides an interface for generating predictions from user-provided input.

 ### `/training`

 Triggers the model training pipeline and allows the complete ML workflow to be executed through the deployed application.

---

 # 🐳 Containerization

 The application is packaged using Docker.

 Project files include:


Dockerfile
.dockerignore


 Containerization provides:

- Reproducible runtime environments
- Dependency isolation
- Consistent deployment
- Easier cloud deployment
- Simplified application portability

 Conceptually:


Source Code
     ↓
Dockerfile
     ↓
Docker Image
     ↓
AWS ECR
     ↓
EC2
     ↓
Running Container


---

 # 🔁 CI/CD Pipeline

 The project implements automated CI/CD using **GitHub Actions**.

 Workflow configuration:


.github/
└── workflows/
    └── aws.yaml


 The deployment pipeline is triggered when changes are pushed to the repository.

 ### CI/CD workflow


Developer
    │
    ▼
Git Commit
    │
    ▼
GitHub Push
    │
    ▼
GitHub Actions
    │
    ▼
Build Docker Image
    │
    ▼
Authenticate with AWS
    │
    ▼
Push Image → Amazon ECR
    │
    ▼
Deploy to EC2
    │
    ▼
Application Updated


 This removes the need to manually rebuild and deploy the application after every code change.

---

 # ☁️ AWS Infrastructure

 The deployment architecture uses multiple AWS services.

 ## Amazon S3

 Used for:

- Model artifact storage
- Model registry
- Model retrieval


Model
  ↓
S3 Model Registry


 ## Amazon ECR

 Used as the Docker image registry.


Docker Build
     ↓
Docker Image
     ↓
Amazon ECR


 ## Amazon EC2

 Acts as the application host.


EC2 Ubuntu Server
       ↓
Docker
       ↓
Application Container
       ↓
Flask Application


 ## AWS IAM

 IAM credentials are used for programmatic interaction with AWS services.

 For production environments, credentials should be managed through **least-privilege IAM policies, GitHub secrets, or instance roles rather than committed to source code**.

---

 # 🔐 Configuration & Secrets

 The application uses environment variables for sensitive configuration.

 ### MongoDB

export MONGODB_URL="mongodb+srv://<username>:<password>@<cluster>/..."


 ### AWS

export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_DEFAULT_REGION="us-east-1"
```

 Sensitive values should never be committed to Git.

 Recommended configuration:


Environment Variables
        +
GitHub Repository Secrets
        +
.gitignore
        ↓
Secure Runtime Configuration


 > ⚠️ **Security note:** For a production deployment, avoid `0.0.0.0/0` for database access or public S3 buckets unless there is a specific, reviewed requirement. Prefer restricted IP ranges, private networking, IAM roles, and least-privilege policies.

---

 # 📝 Logging & Exception Handling

 The project includes dedicated logging and exception-handling functionality.

 This improves observability by making it easier to understand:

- What component is executing
- When failures occur
- Where failures originate
- What data or operation caused the failure
- How the pipeline progresses

 Example architecture:

Application
    │
    ├── Logger
    │
    ├── Exception Handler
    │
    └── Component


 The logger and exception framework are tested through a demo application before being integrated into the complete pipeline.

---

 # 📓 Experimentation & EDA

 The project also separates experimentation from production pipeline code.

 The `notebook/` directory contains:


notebook/
│
├── dataset/
│
├── mongoDB_demo.ipynb
│
└── EDA / Feature Engineering notebooks


 This provides a dedicated environment for:

- Dataset exploration
- Data visualization
- Distribution analysis
- Feature engineering experiments
- MongoDB integration testing
- Model-development experiments

 The resulting logic can then be promoted into reusable production components.

---

 # 📦 Python Project Packaging

 The project uses Python packaging configuration through:


setup.py
pyproject.toml


 This allows local project modules to be imported cleanly throughout the application.

 The environment can be initialized using:


python -m venv venv


 Activate the environment and install dependencies:


pip install -r requirements.txt


 The project template is generated using:

python template.py


---

 # 🗂️ End-to-End Development Workflow

 The complete implementation follows this progression:

```
01  Project Template
        ↓
02  Python Packaging
        ↓
03  Virtual Environment
        ↓
04  Dependencies
        ↓
05  MongoDB Atlas
        ↓
06  Dataset Upload
        ↓
07  Logging
        ↓
08  Exception Handling
        ↓
09  EDA
        ↓
10  Feature Engineering
        ↓
11  Data Ingestion
        ↓
12  Data Validation
        ↓
13  Data Transformation
        ↓
14  Model Training
        ↓
15  Model Evaluation
        ↓
16  Model Registry
        ↓
17  Prediction Pipeline
        ↓
18  Flask Application
        ↓
19  Docker
        ↓
20  AWS ECR
        ↓
21  AWS EC2
        ↓
22  GitHub Actions
        ↓
23  Automated Deployment


---

 # 🔧 Infrastructure Setup

 ## MongoDB Atlas

 The project uses MongoDB Atlas as the cloud database.

 High-level setup:

1. Create a MongoDB Atlas account.
2. Create an organization and project.
3. Create an M0 cluster.
4. Create a database user.
5. Configure network access appropriately.
6. Retrieve the Python driver connection string.
7. Store the connection string securely as `MONGODB_URL`.

 The notebook demonstrates loading the dataset into MongoDB and verifying the resulting documents through Atlas.

---

 # ☁️ AWS Setup

 The cloud deployment uses:


AWS Region
    us-east-1

        ┌─────────────┐
        │     S3      │
        │Model Storage│
        └──────┬──────┘
               │
        ┌──────▼──────┐
        │     ECR     │
        │Docker Image │
        └──────┬──────┘
               │
        ┌──────▼──────┐
        │     EC2     │
        │  Production │
        └─────────────┘


 Recommended IAM design is to create separate users/roles for separate responsibilities and grant only the permissions required by each workflow.

---

 # 🖥️ EC2 Deployment

 The application is deployed on an Ubuntu EC2 instance.

 Docker is installed on the machine and used to run the application container.

 Typical Docker installation:


curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
newgrp docker


 The EC2 machine is then connected to GitHub Actions through a **self-hosted runner**.

---

 # 🏃 GitHub Self-Hosted Runner

 The project demonstrates how a GitHub repository can communicate directly with an EC2 deployment machine.

 Architecture:


GitHub Repository
       │
       ▼
GitHub Actions
       │
       ▼
Self-Hosted Runner
       │
       ▼
EC2 Ubuntu Server
       │
       ▼
Docker Container


 The runner provides a bridge between the source repository and the deployment infrastructure.

---

 # 🔑 GitHub Secrets

 Deployment credentials are stored as GitHub repository secrets rather than hard-coded in the workflow.

 Example secrets:


AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO


 This allows the CI/CD pipeline to authenticate with AWS without exposing credentials in the source repository.

---

 # 🌍 Application Access

 Once the application is running on EC2, the configured application port can be exposed through the EC2 security group.

 Example:


EC2 Public IP
      +
Application Port
      ↓
Flask Application


 For example:


http://<EC2_PUBLIC_IP>:5080


 In a production-grade deployment, HTTPS, a domain name, a reverse proxy/load balancer, and restricted security-group rules should be considered.

---

 # 🧩 Key Engineering Practices Demonstrated

 | Area | Implementation |
| --- | --- |
| Programming | Python |
| Data Storage | MongoDB Atlas |
| Data Processing | Pandas |
| Experimentation | Jupyter Notebook |
| ML Pipeline | Modular Components |
| Validation | Schema-based validation |
| Configuration | YAML + Constants |
| Logging | Custom Logger |
| Error Handling | Custom Exceptions |
| Model Training | Estimator Architecture |
| Model Storage | AWS S3 |
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Compute | Amazon EC2 |
| Cloud | AWS |
| Automation | GitHub Actions |
| CI/CD | Automated Deployment |
| Web Application | Flask |
| Deployment | Docker + EC2 |
| Source Control | Git/GitHub |

---

 # ⭐ Project Highlights

 ### 🔹 End-to-End MLOps

 The project doesn't stop at model training. It demonstrates the complete lifecycle:

 **Data → Validation → Transformation → Training → Evaluation → Registry → Deployment → Prediction**

 ### 🔹 Modular Architecture

 Individual pipeline stages are isolated into components, making the system easier to maintain, test, debug, and extend.

 ### 🔹 Cloud-Native Workflow

 MongoDB Atlas and AWS services are integrated into the machine learning lifecycle.

 ### 🔹 Automated Deployment

 GitHub Actions automates the process of building and deploying the application.

 ### 🔹 Containerized Application

 Docker ensures that the application and its dependencies can run consistently across environments.

 ### 🔹 Model Governance

 Model evaluation is performed before a model is promoted to the model registry.

 ### 🔹 Production-Oriented Design

 Logging, exception handling, configuration management, artifacts, environment variables, and modular components make the project closer to a real-world ML engineering workflow.

---

 # 📈 Skills Demonstrated


                    MLOps
                      │
       ┌──────────────┼──────────────┐
       │              │              │
   Machine        Engineering      Cloud
  Learning          Practices    Infrastructure
       │              │              │
       ├─ EDA        ├─ Logging      ├─ AWS S3
       ├─ Features   ├─ Exceptions   ├─ AWS ECR
       ├─ Training   ├─ Packaging    ├─ AWS EC2
       ├─ Evaluation ├─ Components   └─ AWS IAM
       └─ Prediction └─ Artifacts
                      │
                      ▼
                   DevOps
                      │
              ┌───────┴────────┐
              │                │
          Docker          GitHub Actions
              │                │
              └───────┬────────┘
                      ▼
                 CI/CD Pipeline


---

 # 🏁 Final Outcome

 The completed system provides a reproducible path from raw data to a deployed machine learning application:


                DATA
                  │
                  ▼
           ┌─────────────┐
           │   MongoDB   │
           └──────┬──────┘
                  │
                  ▼
           DATA INGESTION
                  │
                  ▼
           DATA VALIDATION
                  │
                  ▼
        DATA TRANSFORMATION
                  │
                  ▼
          MODEL TRAINING
                  │
                  ▼
         MODEL EVALUATION
                  │
             ┌────┴────┐
             │         │
          Approved   Rejected
             │
             ▼
        MODEL PUSHER
             │
             ▼
          AWS S3
             │
             ▼
        DOCKER IMAGE
             │
             ▼
          AWS ECR
             │
             ▼
           AWS EC2
             │
             ▼
       DEPLOYED FLASK APP
             │
        ┌────┴─────┐
        ▼          ▼
    /predict    /training


---

 # 💼 Why This Project Matters

 This project demonstrates more than the ability to train a machine learning model.

 It demonstrates the ability to **engineer a machine learning system**.

 The implementation brings together:

 **Machine Learning + Software Engineering + Data Engineering + Cloud Infrastructure + Docker + CI/CD + Web Deployment**

 into one integrated workflow.

 > **From experimentation in notebooks to an automated, containerized cloud deployment.**

---

 ## 🚀 Quick Start


# Clone repository
git clone <repository-url>

# Create environment
python -m venv venv

# Activate environment
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
export MONGODB_URL="<mongodb-connection-string>"

# Run application
python app.py


 For PowerShell:


$env:MONGODB_URL="<mongodb-connection-string>"
python app.py


---

 # 📌 Future Enhancements

 Potential improvements for taking the project further include:

- Automated unit and integration testing
- Test coverage reporting
- HTTPS with a custom domain
- AWS IAM least-privilege roles
- Private MongoDB networking
- AWS Secrets Manager / Parameter Store
- CloudWatch monitoring
- Application health checks
- Model drift monitoring
- Data drift detection
- Automated model retraining
- Experiment tracking
- Model versioning
- Infrastructure as Code using Terraform
- Blue/green or rolling deployments
- Production reverse proxy using Nginx
- Load balancing and auto scaling
- Monitoring and alerting

---

 # 👨‍💻 Project Philosophy


                 "Build it"
                    ↓
              "Automate it"
                    ↓
             "Containerize it"
                    ↓
               "Deploy it"
                    ↓
              "Monitor it"
                    ↓
              "Improve it"


 **The goal is not simply to build a model — it is to build a reliable system around the model.**

 