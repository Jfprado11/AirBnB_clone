# 0x00. AirBnB clone - The console
![](https://revistasumma.com/wp-content/uploads/2019/10/airbnb-678x381.png)

- Foundations > Higher-level programming > AirBnB clone
- By Guillaume, CTO at Holberton School
- This project was done in teams of 2 people, Alexander Cardona and Juan Felipe Prado Cruz

## Resources

-   [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw "cmd module")
-   **packages**  concept page
-   [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g "uuid module")
-   [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q "datetime")
-   [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g "unittest module")
-   [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg "args/kwargs")
-   [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A "Python test cheatsheet")

## **About the Project**

This project is carried out in order to test the knowledge acquired throughout the months spent at Holberton while seeking to contribute a little more knowledge and experience. In addition to this, develop soft skills in the area of   teamwork, collaborative synergy and problem solving along the way.

It was created looking simple and elegant but at the same time efficiency, following the framework and respecting what Holberton as a "final client" ask us to do.

The AirBnB clone project try to replicated the behavior of the website of the company AirBnB, witch needs to store lots of information from his users and his branch offices, and for this they are implementing json files, and a program to serializate and deserializates this information and store it prperly.

## How to install it

To use this AirBnB clone implementation you must clone the following repository on your local machine  <https://github.com/Jfprado11/AirBnB_clone.git>, once you has the repository on your machine you must give permissions of execution with the command `chmod u+x console.py`, and preferably use it in a version of `python 3`  

To make this AirBnB works you need to have in your machine the next files:

                console.py
                models > __init__.py
			 basemodel.py
			 user.py
			 amenity.py
			 city.py
			 place.py
			 state.py
			 review.py
			 engine > __init__.py
			          file_storage.py
                

Also in the same directory you can have the next files if you want to test it:
                
		 tests > __init__.py
		         test_models > __init__.py
			               test_basemodel.py
				       test_user.py
				       test_amenity.py
				       test_city.py
				       test_place.py
				       test_state.py
				       test_review.py
				       test_engine > __init__.py
				       		     test_file_storage.py

To run all tests pls use the command `python3 -m unittest discover tests`
## **Features**
This project allows the next commands
- help: Shows the docummentatios of the command asked
	+ `(hbnb) help <command name>`

- quit: Command to exit the prompt directly
	+ `(hbnb) quit`

- EOF: Allows to exit the prompt by typing ctrl^D
	+ `(hbnb) ctrl^D`

- create: Creates a new instance of a class, saves it, and print his id
	+ `(hbnb) create <class name>`

- show: Prints the string representation of an instance based on the class name and id
	+ `(hbnb) show <class name> <id>`

- destroy: Deletes an instance based on the class name and id
	+ `(hbnb) destroy <class name> <id>`

- all: Prints all string representation of all instances based or not on the class name.
	+ `(hbnb) all`
	+ `(hbnb) all <class name>`

- update: Updates an instance based on the class name and id by adding or updating attribute
	+ `(hbnb) update <class name> <id> <attribute name> "<attribute value>"`


## **About the Authors**

**_Juan Felipe Prado:_**
Junior Developer in process, passionate about video games and soccer. He just graduated from High School, but he find that becoming a software developer would be where he best fits.

**_Alexander Cardona:_**
Junior developer in process, sports coach and passionate about computer science, he studied geological engineering and sports management before finding the opportunity in Holberton where he plans to become an outstanding developer.
## **Special Thanks**

_This project is made with love and that is why the love of all those people who believe in us converges here_

-   _Luisa Cardenas_
-   _Hernan Dario Cardona_
-   _Juan Pablo Prado_
-   _Viviana Cruz_