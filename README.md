# Image Translation System

A simple web service that translates images using AWS-managed infrastructure and a Python/Flask backend.

## 🚀 Architecture Overview

![Architecture Diagram](docs/architecture.png)

1. **AWS Cognito**  
   - User pools for authentication.
   - Hosted UI for login/registration.
2. **API Gateway**  
   - Secures HTTP endpoints.
   - Integrates with Cognito authorizer.
3. **Flask Service**  
   - `/auth` routes handle sign-in/sign-out callbacks.
   - `/translate` route accepts images and returns translated output.
4. **DynamoDB**  
   - Stores user profiles and translation request metadata.
5. **Terraform**  
   - All infrastructure defined as code under `infrastructure/`.

## 📁 Repository Structure

See the tree at the top of this file.  
- **infrastructure/** – Terraform modules for each AWS service.  
- **src/flask_service/** – Flask app, routes, and AWS client helpers.  
- **docker/** – Container definitions for local development.  
- **scripts/** – Convenience scripts (deploy, run locally).  
- **docs/** – Architecture diagrams and design notes.

## 🔧 Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)  
- [Terraform 1.4+](https://www.terraform.io/)  
- [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)  
- [Docker & docker-compose](https://docs.docker.com/compose/install/)

## ⚙️ Setup & Deployment

### 1. Terraform Infrastructure

```bash
cd infrastructure
terraform init
terraform plan -out=plan.out
terraform apply plan.out
```

### 2. Configure Flask
Copy and edit `src/flask_service/config.ample.py` -> `config.py`, filling in:
```angular2html
COGNITO_USER_POOL_ID=…
COGNITO_CLIENT_ID=…
COGNITO_REGION=…
DYNAMODB_TABLE=…
API_GATEWAY_URL=https://…
```

Install python dependencies:
```bash
cd src/flask_service
pip install -r requirements.txt
```

### 3. Run Locally
Docker Compose (includes DynamoDB local)
```bash
cd docker
docker-compose up --build
```

### 4. Endppoints
- `GET /health` - Service health checl
- `POST /auth/login` - Redirects to Cognito Hosted UI
- `GET /auth/callback` - Process login callback
- `POST /translate` - Upload image JSON payload -> translation result (In progress)
