Tomato Timer (tomatotimer)
===============================================================================

Description
-------------------------------------------------------------------------------
Tomato Timer (tomatotimer) is a timer tool of The Pomodoro Technique.

Links
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- `The Promodoro Technique Offical Site <http://www.pomodorotechnique.com/>`_ 

Requirements
-------------------------------------------------------------------------------

Basic Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- python 2.5
- pip 0.3.1
- virtualenv 1.7

Pip Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Django==1.3.1
- distribute==0.6.24
- wsgiref==0.1.2

Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SQLite 3 (You can use any other `Django supported DBMS <https://docs.djangoproject.com/en/1.3/ref/databases/>`_ .)

Install
-------------------------------------------------------------------------------

Create a virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Get Source Code**

 $ mkdir tomatotimer

Then Unzip the zip package of tomatotimer into *tomatotimer* directory.

Or Clone from Github.com

 $ git clone git://github.com/richard-ma/tomatotimer.git tomatotimer

**Change Dir**

 $ cd tomatotimer

**Create Env**

 $ virtualenv venv --distribute

**Active Env**

 $ source venv/bin/activate

Install pip packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 $ pip install Django

Other package will be installed automaticly.

*If you choose any other DBMS for Django, you should install the interface package.*

Run Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Change Dir**

 $ cd rtools

**Start Server**

 $ python manage.py runserver

Use IT!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open your browser and type address: http://127.0.0.1:8000/tomatotimer/ . After that the main window will come out.

How to use?
-------------------------------------------------------------------------------
Tomato Timer is a web application made by Python and Javascript.

Task Life Circle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code::

      +---- New Task 
      |
 +----+---> Activity Inventory -------+-----+
 |                                    |     |
 +----+---- Todo List <---------------+     +----> Trash
      |                                     |
      +-------------------------------------+
      |
      +---> Doing Now ----+-----------+
              ^           |           |
              |           |           |
              +-----------+           |
                                      |
      +---- Done <--------------------+
      |
      +---> **To Be Continue**

Activity Inventory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can add or remove task here. Tasks in Activity Inventory can be done in the future.

Todo List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can Put any task into current task area, then start the timer. There are tasks you have to finish today.


Q&A
-------------------------------------------------------------------------------

