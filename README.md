# Explore With Us
## Overveiw
Explore With Us is a vacation destination catalog website build with Django, Bootstrap and MongoDB Atlas.
I created this website to take part in MongoDB Atlas Hackathon hosted by DEV.to

<br>
<h4>Tech I used:</h4>
<ul>
    <li>HTML,CSS,JS and Bootstrap 4</li>
    <li>Django</li>
    <li>MongoDB Atlas<ul>
<li>I used MongoDB Atlas to store the database by creating a cluster on  [MongoDB](https://www.mongodb.com/cloud/atlas/register) </li>
<li>I used the Atlas search feature to implement a fast, relevance-based full-text search for the destinations that I have in my database.</li>
</ul>
</li>
</ul>


## How I used Atlas Search feature:
I used MongoDB Atlas search to implement the autocomplete feature in my "Search Destination" Search Bar.
So that users can easily find their suitable destination within few seconds without scrolling.
First I made a search index for my collection "main_destination".
<br>


The Search Index I used:
``` 
{
  "mappings": {
    "dynamic": false,
    "fields": {
      "name": [
        {
          "foldDiacritics": false,
          "maxGrams": 7,
          "minGrams": 3,
          "tokenization": "edgeGram",
          "type": "autocomplete"
        }
      ]
    }
  }
}
```
__All the collection in Project_data database:__
<img src="./readme_img/databaseAndCollection.png" alt="myCollection">


Then in backend I created Connect.py in main folder to connect with the cluster for searching the index from views.py search action. using pymongo package built for python to connect with MongoDB, as djongo does not support aggregate function.

So that once the user starts searching particular destination it will suggest them destinations automatically.


<img src="./readme_img/demo.gif" height="260px">

_views.py>search :_

<img src="./readme_img/views_py.png" alt="views.py">

This is how the function looks like:
``` 
add_result = collection.aggregate(
           [
               {
                   "$search": {
                       "autocomplete": {
                           "query": address,
                           "path": "name",
                           "fuzzy": {
                               "maxEdits": 2
                           }
                        }
                   }
               }
           ]
      )
```
This function build a pipeline that searches using the address parameter automatically from the collection as defined in MongoDB Atlas search index as I demoed at the top in my demo video.


## How you will see this project

#### **STEP 1:**
Fork this repo and clone it using:
```angular2html
git clone https://github.com/mr-palindrome/Explore-With-Us.git
```
<br>
The Django skeleton is look like this:
<br>

<img src="./readme_img/Django_skeleton.png" alt="Django skeleton">

<br>


#### **STEP 2:**
Install virtualenv then create a virtual environment test:
```
pip3 install virtualenv
virtualenv test
source test/bin/activate
```

Install all the dependencies using:
```angular2html
pip3 install -r requirements.txt
```


#### **STEP 3:**
Create a Django SECRET_KEY using following command in python3 terminal:
```
python3
>>>from django.core.management.utils import get_random_secret_key  
>>>>get_random_secret_key()
```
Create a .env file in explore_with_us folder to store all the environment and secret keys, like Django SECRET_KEY, mongoDB connection string.

But, for demonstration purpose you don't have to create your own cluster, I have provided my own connection string to access all the data present in my Atlas cluster database(AtlasHackathon>Project_data)


<img src="./readme_img/clusterimage.png" alt="MyCluster">


Now store the Django SECRET_KEY and my connection string in .env, it will look like:
``` 
SECRET_KEY = <django SECRET_KEY>
HOST = mongodb+srv://user_demo:demo123@atlashackathon.nhdkl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
```
#### **STEP 4:**
Now you can see the website in your localhost:8000 using:
``` 
python3 manange.py runserver
```

## Additional Resources / Info
This was my first time using MongDB as the database for a website which was a really great experience of using noSQL specially MongoDB Atlas, I'm also planning to use it in my future projects.
I learned about [pymongo package](https://pymongo.readthedocs.io/en/stable/) and [djongo](https://www.djongomapper.com/) availabe for python. I took help from [How to Use Django with MongoDB](https://www.mongodb.com/compatibility/mongodb-and-django) document.
Initially I started researching about Atlas search and how to use them using the [Atlas Search Docs](https://docs.atlas.mongodb.com/atlas-search/).

And another resource that help me to build my frontend was [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/).