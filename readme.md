# Enhancing Search Relevance: SBERT and ANNOY Algorithm Implementation for News Articles with AWS Deployment

## Project Overview

Search relevance is a critical factor in improving user experience and engagement in information-rich industries such as e-commerce, content platforms, and news outlets. This project focuses on leveraging Sentence-BERT (SBERT) encoding and the ANNOY library to enhance the search relevance of news articles. Additionally, the deployment of the solution on AWS using Docker containers and a Flask API allows users to interact seamlessly with the system.

**Key Industries Benefiting from Improved Search Relevance:**

- **E-commerce**: Ensuring users find products quickly on platforms like Amazon or eBay.

- **Content Platforms**: Recommending relevant videos or movies on platforms like YouTube or Netflix.

- **News Articles**: Facilitating quick and accurate retrieval of relevant news stories.

---

## Aim

The primary goal is to elevate the search experience for news articles through the utilization of SBERT and ANNOY. The solution, deployed on AWS with Docker containers, provides a Flask API interface for users to effortlessly query and retrieve pertinent news articles.

---

## Data Description

The dataset comprises 22,399 articles, each characterized by the following attributes:

- `article_id`: Unique identifier for each article.
- `category`: Broad classification of the article's content.
- `subcategory`: More specific classification within the category.
- `title`: Headline of the news article.
- `published date`: Date of article publication.
- `text`: Main body of the news article.
- `source`: Publication source of the article.

---

## Tech Stack

- Language: `Python`
- Libraries: `pandas`, `numpy`, `spacy`, `sentence transformers`, `annoy`, `flask`, `AWS`

---

## Approach

### Data Preprocessing

- Clean and preprocess the news article dataset, including tokenization, stop word removal, and normalization.

### SBERT Training

- Train the Sentence-BERT (SBERT) model using preprocessed news articles to generate semantically meaningful sentence embeddings.

### ANNOY Indexing

- Use the ANNOY library to create an index of SBERT embeddings, enabling efficient approximate nearest neighbor search.

### Deployment on AWS with Docker

- Containerize project components, including the Flask API, SBERT model, and ANNOY index, using Docker.
- Deploy Docker containers on an AWS EC2 Instance.

---

## Modular Code Overview

1. `data`
2. `notebooks`
3. `src`
4. `server.py`
5. `requirements.txt`
6. `Dockerfile`
7. `docker-compose.yml`

- The `notebooks` folder contains reference materials.
- The `src` folder organizes Python functions into different files, called by `server.py` for project execution.
- `Dockerfile` and `docker-compose.yml` facilitate the deployment of the model on AWS cloud.
- `requirements.txt` lists all required libraries with respective versions.

---

