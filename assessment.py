"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    Polymorphism: Polymorphsim the the concept of adding flexibilty to you class
                  code and making it easy and effective to use the same code to
                  create different types of objects. For example, if two classes
                  subclass the same super, the super's methods should be set up
                  in such a way that both classes can call the method and achieve
                  the same results. An example of this would be the speak()
                  method from the lectures and how we edited it to account for
                  Cats, Dogs, and Animals whose greeting we specified.


    Abstraction: Part of writing good code is making it easy for other people to
                 use. Abstraction in OO serves this by hiding some of the 
                 complexity of the code from the user through the use of class
                 methods and attributes and inheritance. The user doesn't need to
                 know how the data is stored, processed, or altered internally to 
                 interact well with the class object.


    Encapsulation: Data and attributes should be defined close to where 
                   they are worked with and the methods that work on them. By 
                   making an class, you are showing a user/maintainer that those 
                   pieces of code are meant to work together. This can also help
                   a user understand the functionality of the code by 
                   "protecting" methods so they can only be used by the correct
                   objects.


2. What is a class?

    A class is like a smarter dictionary. It stores information about an object
    (the object's attributes), but is more structured than a dictionary and
    contains its own "smarts" (the class methods). A class is a kind of 
    blueprint for an object that indicates how it should look and function.


3. What is an instance attribute?

    An instance attribute is a piece of information specific to that object. We
    may have created many cats from our Cat class, but that cat in particular
    has a post-it stuck to it that tells us its name is Auden. Instance attributes
    are the first things that will be found if we start looking for a certain
    attribute on our object (the class, superclass, etc.).


4. What is a method?

    A method is the smarts behind the class. It is a class specific function 
    that indicates how this type of object should behave and modify itself. 
    Methods can only be accessed by objects of the class (or the class's 
    subclasses) where the method is defined. 


5. What is an instance in object orientation?

    An instance is another term for an object. When we say auden = Cat("Auden"),
    we are telling the Cat class "Make me an object/instance from your blueprint
    and give it these attributes and bind it to this variable". 


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    A class attribute is a piece of information that all objects of that class
    share. Where our instance attributes were post-its on the object itself,
    class attributes are not on the instance (and can therefore be overwritten)
    by instance attributes). A good time to use class attributes is when every
    instance of your class shares the same value (the Cat class species is
    always "cat"). A good time to use instance attributes is when each object
    made by the class needs to have unique information (a Cat class object
    shouldn't share its name value with every other Cat object).

"""


# Parts 2 through 5:
# Create your classes and class methods


