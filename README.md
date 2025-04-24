# Todo Application with Flask Backend and Express Frontend

This is a full-stack Todo application with a Flask backend and Express frontend, containerized using Docker.

## Project Structure

```
project-root/
│
├── frontend/          # Node.js with Express
│   ├── Dockerfile
│   ├── package.json
│   ├── index.js
│   └── views/
│       └── form.ejs
│
├── backend/           # Flask backend
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│
├── docker-compose.yaml
└── README.md
```

## Prerequisites

- Docker
- Docker Compose
- Git

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Features

- Create and manage todo items
- MongoDB database integration
- Docker containerization
- Separate frontend and backend services

## Docker Images

The Docker images are available on Docker Hub:
- Frontend: `<your-dockerhub-username>/todo-frontend`
- Backend: `<your-dockerhub-username>/todo-backend`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 