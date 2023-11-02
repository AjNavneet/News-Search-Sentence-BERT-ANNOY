# Search Relevancy Algorithm using SBERT and ANNOY for Articles Data and AWS Deployment

## Project Overview

Search relevance refers to the measure of how well search results align with the user's intent or query. In industries where vast amounts of information are available, such as e-commerce, content platforms, or news outlets, search relevance plays a crucial role in enhancing user experience and driving user engagement. It ensures that users can quickly and accurately find the information they are looking for.

**Key Industries Where Search Relevance is Essential:**

- **E-commerce**: In online shopping platforms like Amazon or eBay, search relevance is critical to help users find the products they want.

- **Content Platforms**: Platforms like YouTube or Netflix rely on search relevance to recommend relevant videos or movies to users.

- **News Articles**: In the context of news articles, search relevance is crucial to help users find relevant news stories quickly.

This project involves three key steps:

1. **Sentence-BERT (SBERT) Encoding**: The SBERT model encodes news articles into semantically meaningful sentence embeddings, capturing contextual and semantic information.

2. **ANNOY Indexing**: Utilizing the ANNOY library to create an index of SBERT embeddings, enabling efficient approximate nearest neighbor search.

3. **Deployment on AWS with Docker**: The project is deployed on AWS using Docker containers, with a Flask API serving as the interface for users to interact with the system.

---

## Aim

This project aims to improve the search experience for news articles by leveraging the Sentence-BERT (SBERT) model and the ANNOY approximate nearest neighbor library. It will be deployed on AWS using Docker containers and exposed as a Flask API, allowing users to query and retrieve relevant news articles easily.

---

## Data Description

The dataset consists of 22,399 articles with the following attributes:

- `article_id`: A unique identifier for each article in the dataset.
- `category`: The broad category to which the article belongs, providing a high-level classification of the content.
- `subcategory`: A more specific classification within the category.
- `title`: The title or headline of the news article.
- `published date`: The date when the article was published.
- `text`: The main body of the news article, containing detailed information.
- `source`: The source or publication from which the article originated.

---

## Tech Stack

- Language: `Python`
- Libraries: `pandas`, `numpy`, `spacy`, `sentence transformers`, `annoy`, `flask`, `AWS`

---

## Approach

### Data Preprocessing

- Clean and preprocess the news article dataset, including tokenization, removal of stop words, and normalization.

### SBERT Training

- Train the Sentence-BERT (SBERT) model using the preprocessed news articles to generate semantically meaningful sentence embeddings.

### ANNOY Indexing

- Utilize the ANNOY library to create an index of the SBERT embeddings, enabling fast and efficient approximate nearest neighbor search.

### Deployment on AWS with Docker

- Containerize the project components, including the Flask API, SBERT model, and ANNOY index, using Docker.
- Deploy the Docker containers on AWS EC2 Instance.

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
- The `src` folder contains Python functions organized into different files, which are called by `server.py` to run the project.
- `Dockerfile` and `docker-compose.yml` are used to deploy the model on AWS cloud.
- `requirements.txt` lists all required libraries with respective versions.

---

## Key Concepts Explored

1. The importance of search relevance in enhancing user experience and engagement.
2. Understanding the transformers used in Large Language Models (LLMs).
3. Data preprocessing steps.
4. The concept and implementation of semantic embeddings using the SBERT model.
5. SBERT model training.
6. Utilizing ANNOY for indexing high-dimensional embeddings.
7. Docker containers for packaging and deployment.
8. Deployment on AWS using services like EC2.
9. Integrating SBERT and ANNOY to build an efficient search system.
10. Application of NLP techniques in improving search relevancy.
11. The end-to-end process of developing and deploying an ML project.

---

