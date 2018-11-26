# IEMS 5780 Mini Project

* Individual project: each student should work on his/her own project
* **Deadline**: 23:59, 22th December, 2018 (Saturday)
* **15%** of the final grade

## Overview

In this mini project, you will build a **machine learning application** utilizing what you have learnt in this course. You are free to choose a topic and a machine learning task in which you are interested.

The machine learning task does not have to be a very complicated one. The focus of this project should be on how the system is designed such that it is **scalable**.

Your system should be implemented using **Python 3.6**. You are free to use any open source packages or libraries in your project.

# Requirements

Your project should implement the following kinds of features/functions:

* **Machine Learning**
    - Your application should be powered by a machine learning model
    - You can collect data and train a model for the task all by yourself
    - You can also use existing pre-trained models available on the Internet, or even packages that implement specific machine learning applications
    - You should provide functions in addition to simply applying the model to the user's input, such as allowing the user to retrieve the most recent predictions, or configure some settings to choose different models
* **Network programming**
    - Using socket programming, HTTP, or asynchronous messaging to implement clients and servers
* **Concurrent programming**
    - Using multi-threading, multi-processing or asyncio to achieve concurrent execution of tasks
* **System design**
    - Consider which part(s) of the system is the bottleneck
    - Design your system in such a way that it allows horizontal scaling
    - Your system should be able to support multiple concurrent users
    - Use either asynchronous message queues, pub/sub systems, or caches to increase the throughput and scalability of your system
* **Robustness**
    - You should prevent the application from crashing by validating inputs and catch possible exceptions wherever necessary
* **User Interface**
    - You can use Telegram as your frontend (recommended), or you can develop your own interface using Python, or create a Web-based application

## Assessment Scheme

Your project will be assessed using the criteria listed below:

* **20% - Machine learning**
* **20% - Network programming**
* **20% - Concurrent programming**
* **20% - System design and complexity**
* **10% - Robustness**
* **10% - User Interface**

## Suggested Topics

Below are some possible topics for reference:

* Language detection
    - Allow user to type in a sentence in a certain language, the system will detect which language the sentence is written in
* Gender and age prediction
    - Take a photo of a person, and predict the gender and age of the person
* News classification
    - Given a URL to a news article, the system will classify the news article into one of the major categories (e.g. sports, finance, technology, science, etc.)
* Speaker classification
    - Let the user record a voice message in Telegram, the system will classify the speaker into female or male
* Book recommendation
    - Allow users to rate books and the system will recommend new books to the users
* ...

## References and Resources

### Pre-trained Machine Learning Models
* [https://modelzoo.co/](https://modelzoo.co/)
* [https://modeldepot.io/](https://modeldepot.io/)
* [https://deepmoji.mit.edu/](https://deepmoji.mit.edu/)

## Submission

You should submit the following files to Blackboard:
* A **README file** containing brief description of each Python script, the dependencies (i.e. open source packages or libraries you have used), and instructions on how to run your programs
* All **source codes**
* **Data files** (if the data is larger than 10MB, upload to cloud storage and include links in the README file)
* A **report in PDF format** of no more than **two pages**, with the following information:
    - Functions/features of your system
    - Description of your machine learning task (e.g. where did you get the data, what ML algorithm did you use, what is the performance of your model)
    - A diagram of the system architecture
    - Description of how your system is designed to be scalable
