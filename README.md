# Project README

## Overview

This project is a Django application running inside a Docker container. The project also includes a bot script. This README provides instructions on how to set up and run the project using Docker.
You can get random phrase using this app.

## Prerequisites

- Docker
- Docker Compose

## Setup

### Clone the Repository

   ```sh
   git clone https://github.com/test_proj.git
   cd test_proj
```
   
### Create and Configure Environment File

Create a `.env` file in the root directory of the project. This file should contain environment variables required by Django. You can see an example in `.env.sample`

### Build and Start the Containers

Use Docker Compose to build and start the containers:

```bash
docker-compose up --build
```

This command will:

Build the Docker image for the Django application.
Start the Django application and make it accessible on http://localhost:8000.


### Running the bot

To run the bot you need to write down in terminal:

```bash
cd app
py bot.py
```
