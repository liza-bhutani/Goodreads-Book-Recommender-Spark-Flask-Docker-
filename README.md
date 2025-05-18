#### A book recommendation system using Spark's ALS algorithm, served via Flask API, with Docker containerization

Features:
1. Personalized Recommendations: Collaborative filtering with Spark ML
2. Modern Web Interface: Beautiful Bootstrap 5 UI
3. Easy Deployment: Dockerized for one-command setup
4. Scalable: Handles large datasets efficiently.

Tech Stack :
1. Spark ALS: Core recommendation engine
2. Flask: REST API and web interface
3. Docker: Containerized environment
4. Bootstrap 5: Responsive frontend

Build and run with Docker:
docker-compose up --build

Access the system:
Web UI: http://localhost:5000 , 
API Endpoint: GET /recommend/<user_id>

Usage Examples:
Get recommendations for user 42: curl http://localhost:5000/recommend/42

Sample response:
[
  {
    "book_id": 123,
    "title": "The Great Gatsby",
    "rating": 4.8,
    "author": "F. Scott Fitzgerald"
  }
]

Sample Images :![image](https://github.com/user-attachments/assets/245b6c6d-f86b-4a82-baee-7a6ded2c0484)
![image](https://github.com/user-attachments/assets/2ab2d58e-9328-40fe-8b19-fa08c5265efa)

