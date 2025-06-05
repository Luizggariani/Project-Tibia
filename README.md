# Project-Tibia

![Tibia icon](https://www.tibiabr.com/wp-content/uploads/2017/12/TibiaDragonLogo_HighRes.png)

## 📖 Project Overview

This project is focused on building a Tibia-themed chatbot that integrates Python, SQL, and modern database technologies. The chatbot is designed to extract data from the Tibia API, store it in a PostgreSQL database enhanced with `pgvector` for embeddings, and provide semantic search capabilities through a FastAPI backend. The project is both a learning opportunity for beginners and a practical application for experienced data engineers.

---

## 🛠️ Technologies and Tools Used

- **Programming Language**: Python (3.9)
- **Database**: PostgreSQL (16) with `pgvector` extension for vector embeddings
- **Backend Framework**: FastAPI
- **Database Management**: pgAdmin (Windows or Docker-based)
- **Containerization**: Docker (running on WSL)
- **VPN for Remote Access**: Tailscale or WireGuard
- **Python Libraries**: `requests`, `psycopg2`, `pgvector`, `fastapi`, `uvicorn`

---

## 🎯 Objectives

1. **Data Extraction**:
   - Extract data from the Tibia API, including creatures, characters, guilds, highscores, houses, kill statistics, and worlds.
   - Use the endpoint `https://api.tibiadata.com/v4/creatures` as the starting point for data ingestion.

2. **Database Management**:
   - Store the extracted data in a PostgreSQL database running in a Docker container.
   - Use the `pgvector` extension to enable vector embeddings for semantic search capabilities.
   - Organize the database with a schema named `tibia_api` and tables for each data type (e.g., `creatures`, `characters`, etc.).

3. **Backend Development**:
   - Build a FastAPI backend to query the database and provide endpoints for the chatbot.
   - Implement semantic search functionality using vector similarity over character data.

4. **Remote Access and Security**:
   - Secure remote access to the database using a VPN solution like Tailscale or WireGuard.

5. **Database Management Tools**:
   - Use pgAdmin (either on Windows or Docker-based) for managing and visualizing the PostgreSQL database.

6. **Chatbot Functionality**:
   - Develop a chatbot capable of performing semantic searches over the data.
   - Provide meaningful responses based on vector similarity, enhancing the user experience.

---

## 🚀 Step-by-Step Guide

### 1. **Environment Setup**
   - Install Python (3.9) and required libraries.
   - Install Docker and configure it to run on WSL.
   - Set up PostgreSQL (16) in a Docker container and install the `pgvector` extension.

### 2. **Database Creation**
   - Create a PostgreSQL database named `Tibia`.
   - Define a schema called `tibia_api` and create tables for creatures, characters, guilds, highscores, houses, kill statistics, and worlds.
   - Enable vector embeddings using `pgvector` for semantic search.

### 3. **Data Extraction**
   - Use Python's `requests` library to fetch data from the Tibia API.
   - Parse and clean the data to match the database schema.
   - Insert the data into the PostgreSQL database.

### 4. **Backend Development**
   - Build a FastAPI application to provide RESTful endpoints for querying the database.
   - Implement semantic search functionality using vector similarity over character data.

### 5. **Remote Access and Security**
   - Configure a VPN (Tailscale or WireGuard) to secure remote access to the database.
   - Test the connection to ensure secure and reliable access.

### 6. **Database Management**
   - Use pgAdmin to manage and visualize the database.
   - Perform routine maintenance and monitor database performance.

### 7. **Chatbot Development**
   - Integrate the FastAPI backend with the chatbot interface.
   - Enable the chatbot to perform semantic searches and provide meaningful responses.

---

## 💡 Lessons Learned and Considerations

This project provided an excellent opportunity to explore and apply various technologies, including:

- **Data Extraction**: Automating the process of fetching and cleaning data from APIs.
- **Database Management**: Setting up and managing a PostgreSQL database with advanced features like vector embeddings.
- **Backend Development**: Building a FastAPI backend to serve as the foundation for the chatbot.
- **Semantic Search**: Implementing vector similarity for advanced search capabilities.
- **Security**: Securing remote access to the database using VPN solutions.
- **Containerization**: Running the database in a Docker container for portability and scalability.

Each stage of the project presented unique challenges and valuable learning experiences, making it a comprehensive and rewarding endeavor.

---

## 🌟 Future Enhancements

- Expand the chatbot's functionality to include more advanced natural language processing (NLP) features.
- Integrate additional APIs to enrich the dataset.
- Deploy the chatbot as a web application or integrate it with messaging platforms.
- Optimize the database for handling larger datasets and more complex queries.

<<<<<<< HEAD
This project serves as a foundation for further exploration and development in the fields of data engineering, backend development, and AI-powered applications.

## Project Progress

So far, we have successfully:
- Set up Git and SSH for secure code management.
- Configured the PostgreSQL 16 database with the pgvector extension inside a Docker container running on WSL.
- Established the initial project structure and repository on GitHub.
>>>>>>> bc2cacd (Clean up temporary text and add project progress note to README)
