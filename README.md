# Dictionary

#### This English to Bangla dictionary is developed with perfect hashing. 

I've made this application as a part of my CSE-3203 course assignment.
I've stored over 16 thousands words in sqlite database and for each word I generated 
an unique combination of primary hash key and secondary hash key using the concept 
of perfect hashing and save those information to database also. In case of searching i used those 
hashing keys generated from the word 

##Statistics 
_This result may vary_ <br>
**Total slot :** 9931 <br>
**Total word :** 16912 <br>
**Total bucket:** 45329 <br>
**Longest chain for a single slot:** 81 <br>
**Most collision in a slot:** 9 <br>
**Empty Slot:** 1786


#### The backbone of this application is in Python (Django Framework)   

##Installation on local machine
1. Create a virtual environment. 
```python3 -m venv [name]```
2. Activate the virtual environment.
3. Clone this repository locally.
```git clone https://github.com/vugichugi/Dictionary.git```
4. Install all required module. 
```pip install -r requirements.txt```
5. Run all migrations file
```python manage.py makemigrations```
```python manage.py migrate```
6. Create a superuser for admin panel.
```python manage.py createsuperuser```
7. Run the server
```python manage.py runserver```

##Dataset
Dataset collected and combined from this [repository](https://github.com/MinhasKamal/BengaliDictionary).

