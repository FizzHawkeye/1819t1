## Lecture Schedule

### Lecture 01 (06 Sep)

- Course Introduction
- [Lecture slides](lectures/lecture-01.html), [PDF Version](lectures/pdfs/lecture-01.pdf)
- References:
    - [Think Python 2nd Edition](https://greenteapress.com/wp/think-python-2e/)
    - [The Python (3.6) Tutorial](https://docs.python.org/3.6/tutorial/)


### Lecture 02 (13 Sep)

- Introduction to Machine Learning
- [Lecture slides](lectures/lecture-02.html), [PDF Version](lectures/pdfs/lecture-02.pdf)
- References:
    - [scikit-learn Tutorials](http://scikit-learn.org/stable/tutorial/index.html)
    - [Machine Learning Yearning](http://www.mlyearning.org/) by Andrew Ng


### Lecture 03 (20 Sep)

- Text Classification (1)
- [Lecture slides](lectures/lecture-03.html), [PDF Version](lectures/pdfs/lecture-03.pdf)
- Notebooks:
    - [Text classification using logistic regression](https://github.com/iems5780/1819t1/blob/master/notebooks/l3_text_logistic_regression.ipynb)
    - [Text classification using naive Bayes classifier](https://github.com/iems5780/1819t1/blob/master/notebooks/l3_text_naive_bayes.ipynb)
    - [SMS Spam Classification](https://github.com/iems5780/1819t1/blob/master/notebooks/l3-sms-spam-example.ipynb)
- References:
    - [Working with Text Data - scikit-learn](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)
    - [Natural Language Processing with Python](http://nltk.org/book/)

### Lecture 04 (27 Sep)

- Text Classification (2)
- [Lecture slides](lectures/lecture-04.html), [PDF Version](lectures/pdfs/lecture-04.pdf)
- References:
    - [Word2Vec Tutorail](https://rare-technologies.com/word2vec-tutorial/)
    - [Text Understanding from Scratch](https://arxiv.org/abs/1502.01710). Xiang Zhang, Yann LeCun. 2015.
    - [fasText](https://fasttext.cc/) by Facebook Research


### Lecture 05 (04 Oct)

- Recommender Systems
- [Lecture slides](lectures/lecture-05.html), [PDF Version](lectures/pdfs/lecture-05.pdf)
- Notebooks:
    - [User-based Collaborative Filtering](https://github.com/iems5780/1819t1/blob/master/notebooks/l5-user-based-cf.ipynb)
    - [Gradient Descent Example](https://github.com/iems5780/1819t1/blob/master/notebooks/l5-gradient-descent-example.ipynb)
- References:
    - [Google News Personalization: Scalable Online Collaborative Filtering](https://www2007.org/papers/paper570.pdf). Das et al., 2007.
    - [Amazon.com Recommendations: Item-to-Item Collaborative Filtering](https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf). Linden et al., 2003.
    - [Browsemap: Collaborative Filtering at LinkedIn](https://engineering.linkedin.com/recommender-systems/browsemap-collaborative-filtering-linkedin)
    - [Building Large Scale Real World Recommender Systems (Netflix)](https://www.slideshare.net/xamat/building-largescale-realworld-recommender-systems-recsys2012-tutorial)

### Lecture 06 (11 Oct)

- Image Classification
- [Lecture slides](lectures/lecture-06.html), [PDF Version](lectures/pdfs/lecture-06.pdf)
- Notebooks:
    - Testing ResNet pre-trained model in Keras: [l6_example_keras_resnet50.ipynb](https://github.com/iems5780/1819t1/blob/master/notebooks/l6_example_keras_resnet50.ipynb)
    - Testing Inception V3 pre-trained model in PyTroch: [l6_example_pytorch_inceptionv3.ipynb](https://github.com/iems5780/1819t1/blob/master/notebooks/l6_example_pytorch_inceptionv3.ipynb)
- References:
    - [ImageNet](http://image-net.org/)

### Lecture 07 (18 Oct)

- Network Programming
- [Lecture slides](lectures/lecture-07.html), [PDF Version](lectures/pdfs/lecture-07.pdf)
- Sample Scripts:
    - [TCP Server](https://github.com/iems5780/1819t1/blob/master/scripts/tcp_simple_server.py), [TCP Client](https://github.com/iems5780/1819t1/blob/master/scripts/tcp_simple_client.py)
    - [UDP Server](https://github.com/iems5780/1819t1/blob/master/scripts/udp_simple_server.py), [UDP Client](https://github.com/iems5780/1819t1/blob/master/scripts/udp_simple_client.py)

### Lecture 08 (25 Oct)

- Concurrent Programming (1)
- [Lecture slides](lectures/lecture-08.html), [PDF Version](lectures/pdfs/lecture-08.pdf)
- Sample Scripts:
    - [Daemonic Threads](https://github.com/iems5780/1819t1/blob/master/scripts/multithreading/daemonic_threads.py)
    - [Multithreaded Server](htps://github.com/iems5780/1819t1/blob/master/scripts/multithreading/multithreaded_server.py)
    - [Multiprocess Server](https://github.com/iems5780/1819t1/blob/master/scripts/multithreading/multiprocess_pool_server.py)
    - [Logging Thread Names](https://github.com/iems5780/1819t1/blob/master/scripts/multithreading/logging_thread_names.py)

### Lecture 09 (01 Nov)
- Concurrent Programming (2)
- [Lecture slides](lectures/lecture-09.html), [PDF Version](lectures/pdfs/lecture-09.pdf)
- Sample Scripts:
    - [Non-blocking TCP Server](https://github.com/iems5780/1819t1/blob/master/scripts/async/socket_server_async.py)
    - [Image downloading using aiohttp](https://github.com/iems5780/1819t1/blob/master/scripts/async/image_downloading.py)

### Lecture 10 (08 Nov)
- Web Server and Applications
- [Lecture slides](lectures/lecture-10.html), [PDF Version](lectures/pdfs/lecture-10.pdf)
- Sample Scripts:
    - [HTTP on TCP](https://github.com/iems5780/1819t1/blob/master/scripts/http/http_on_tcp.py)
    - [HTTP using requests](https://github.com/iems5780/1819t1/blob/master/scripts/http/http_requests.py)
    - [Hello World Web Application using Flask](https://github.com/iems5780/1819t1/blob/master/scripts/http/flask_hello_world.py)
    - [Query String and JSON Response in Flask](https://github.com/iems5780/1819t1/blob/master/scripts/http/flask_data_format.py)

### <strike>(15 Nov) (Graduation Ceremony)</strike>

### Lecture 11 (22 Nov)

- Asynchronous Tasks and Message Queues
- [Lecture slides](lectures/lecture-11.html), [PDF Version](lectures/pdfs/lecture-11.pdf)
- Sample Scripts:
    - Redis [Publisher](https://github.com/iems5780/1819t1/blob/master/scripts/redis/redis_pub.py), [Subscriber](https://github.com/iems5780/1819t1/blob/master/scripts/redis/redis_sub.py)
    - Celery [Task](https://github.com/iems5780/1819t1/blob/master/scripts/celery/task.py), [App](https://github.com/iems5780/1819t1/blob/master/scripts/celery/app.py)

### Lecture 12 (29 Nov)

- Scaling Network Applications
- [Lecture slides](lectures/lecture-12.html), [PDF Version](lectures/pdfs/lecture-11.pdf)

### Lecture 13 (04 Dec) (YIA LT4)

- Deploying Network Applications and Other Topics
- Lecture slides, PDF Version

