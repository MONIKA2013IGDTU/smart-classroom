# smart-classroom

SMART CLASSROOM SOLUTION
The SMART CLASSROOM SOLUTION is an automated system based on Raspberry Pi to access files remotely from a cloud platform with a user interface to download and open files along with notification capabilities. Using the Google API, the raspberry pi is connected to the google drive. The files from the drive can now be fetched easily.
This small piece of hardware works on the following:
I. It enables us to list and vies files submitted to the cloud platform.
II. It notifies the admin whenever a new file is submitted.
III. It notifies the Class Representative about the ETA of the teacher through a sms.
Prerequisites for the development of the project are:
I. Python: Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language.
II. Raspberry pi:  a low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse.
III. Twilio: Twilio is a cloud communications company based in San Francisco, California. Twilio allows software developers to programmatically make and receive phone calls and send and receive text messages using its web service APIs.


KEYWORDS

Raspberry Pi 2
Twilio API
Python
Py-Drive
Google API
Android

INTRODUCTION TO PYTHON

Python was created in the early 1990s by Guido van Rossum at Stichting Mathematisch Centrum (CWI, see https://www.cwi.nl/) in the Netherlands as a successor of a language called ABC. Guido remains Python’s principal author, although it includes many contributions from others.
In 1995, Guido continued his work on Python at the Corporation for National Research Initiatives (CNRI, see https://www.cnri.reston.va.us/) in Reston, Virginia where he released several versions of the software.
In May 2000, Guido and the Python core development team moved to BeOpen.com to form the BeOpen PythonLabs team. In October of the same year, the PythonLabs team moved to Digital Creations (now Zope Corporation; see http://www.zope.com/). In 2001, the Python Software Foundation (PSF, see https://www.python.org/psf/) was formed, a non-profit organization created specifically to own Python-related Intellectual Property. Zope Corporation is a sponsoring member of the PSF.
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.[25][26] The language provides constructs intended to enable clear programs on both a small and large scale.
Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or proceduralstyles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.
Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. Using third-party tools, such as Py2exe or Pyinstaller, Python code can be packaged into stand-alone executable programs for some of the most popular operating systems, so Python-based software can be distributed to, and used on, those environments with no need to install a Python interpreter.



Syntax and Semantics
INDENTATION
Python uses whitespace indentation, rather than curly braces or keywords, to delimit blocks; this feature is also termed the off-side rule. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block.
Statements and control flow
Python's statements include (among others):
The assignment statement (token '=', the equals sign). This operates differently than in traditional imperative programming languages, and this fundamental mechanism (including the nature of Python's version of variables) illuminates many other features of the language. Assignment in C, e.g., x = 2, translates to "typed variable name x receives a copy of numeric value 2". The (right-hand) value is copied into an allocated storage location for which the (left-hand) variable name is the symbolic address. The memory allocated to the variable is large enough (potentially quite large) for the declared type. In the simplest case of Python assignment, using the same example, x = 2, translates to "(generic) name x receives a reference to a separate, dynamically allocated object of numeric (int) type of value 2." This is termed binding the name to the object. Since the name's storage location doesn't contain the indicated value, it is improper to call it a variable. Names may be subsequently rebound at any time to objects of greatly varying types, including strings, procedures, complex objects with data and methods, etc. Successive assignments of a common value to multiple names, e.g., x = 2; y = 2; z = 2 result in allocating storage to (at most) three names and one numeric object, to which all three names are bound. Since a name is a generic reference holder it is unreasonable to associate a fixed data type with it. However at a given time a name will be bound to some object, which will have a type; thus there is dynamic typing.
The if statement, which conditionally executes a block of code, along with else and elif (a contraction of else-if).
The for statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block.
The while statement, which executes a block of code as long as its condition is true.
The try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses; it also ensures that clean-up code in afinally block will always be run regardless of how the block exits.
The class statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming.
The def statement, which defines a function or method.
The with statement (from Python 2.5), which encloses a code block within a context manager (for example, acquiring a lock before the block of code is run and releasing the lock afterwards, or opening a file and then closing it), allowing Resource Acquisition Is Initialization (RAII)-like behavior.
The pass statement, which serves as a NOP. It is syntactically needed to create an empty code block.
The assert statement, used during debugging to check for conditions that ought to apply.
The yield statement, which returns a value from a generator function. From Python 2.5, yield is also an operator. This form is used to implement coroutines.
The import statement, which is used to import modules whose functions or variables can be used in the current program.
The print statement was changed to the print() function in Python 3.

EXPRESSIONS
Some Python expressions are similar to languages such as C and Java, while some are not:
Addition, subtraction, and multiplication are the same, but the behavior of division differs (see Mathematics for details). Python also added the ** operator for exponentiation.
As of Python 3.5, it supports matrix multiplication directly with the @ operator, versus C and Java, which implement these as library functions. Earlier versions of Python also used methods instead of an infix operator.
In Python, == compares by value, versus Java, which compares numerics by value[61] and objects by reference. (Value comparisons in Java on objects can be performed with the equals() method.) Python's is operator may be used to compare object identities (comparison by reference). In Python, comparisons may be chained, for example a <= b <= c.
Python uses the words and, or, not for its boolean operators rather than the symbolic &&, ||, ! used in Java and C.
Python has a type of expression termed a list comprehension. Python 2.4 extended list comprehensions into a more general expression termed a generator expression.
Anonymous functions are implemented using lambda expressions; however, these are limited in that the body can only be one expression.
Conditional expressions in Python are written as x if c else y (different in order of operands from the ?: operator common to many other languages).
Python makes a distinction between lists and tuples. Lists are written as [1, 2, 3], are mutable, and cannot be used as the keys of dictionaries (dictionary keys must be immutable in Python). Tuples are written as (1, 2, 3), are immutable and thus can be used as the keys of dictionaries, provided all elements of the tuple are immutable. The parentheses around the tuple are optional in some contexts. Tuples can appear on the left side of an equal sign; hence a statement like x, y = y, x can be used to swap two variables.
Python has a "string format" operator %. This functions analogous to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2". In Python 3 and 2.6+, this was supplemented by the format() method of the str class, e.g. "spam={0} eggs={1}".format("blah", 2).
Python has various kinds of string literals:
Strings delimited by single or double quote marks. Unlike in Unix shells, Perl and Perl-influenced languages, single quote marks and double quote marks function identically. Both kinds of string use the backslash (\) as an escape character and there is no implicit string interpolation such as "$spam".
Triple-quoted strings, which begin and end with a series of three single or double quote marks. They may span multiple lines and function like here documents in shells, Perl and Ruby.
Raw string varieties, denoted by prefixing the string literal with an r. No escape sequences are interpreted; hence raw strings are useful where literal backslashes are common, such as regular expressions and Windows-style paths. Compare "@-quoting" in C#.
Python has array index and array slicing expressions on lists, denoted as a[key], a[start:stop] or a[start:stop:step]. Indexes are zero-based, and negative indexes are relative to the end. Slices take elements from the start index up to, but not including, the stop index. The third slice parameter, called step or stride, allows elements to be skipped and reversed. Slice indexes may be omitted, for example a[:] returns a copy of the entire list. Each element of a slice is a shallow copy.
In Python, a distinction between expressions and statements is rigidly enforced, in contrast to languages such as Common Lisp, Scheme, or Ruby. This leads to duplicating some functionality. For example:
List comprehensions vs. for-loops
Conditional expressions vs. if blocks
The eval() vs. exec() built-in functions (in Python 2, exec is a statement); the former is for expressions, the latter is for statements.
Statements cannot be a part of an expression, so list and other comprehensions or lambda expressions, all being expressions, cannot contain statements. A particular case of this is that an assignment statement such as a = 1 cannot form part of the conditional expression of a conditional statement. This has the advantage of avoiding a classic C error of mistaking an assignment operator = for an equality operator == in conditions: if (c = 1) { ... } is valid C code but if c = 1: ... causes a syntax error in Python.

METHODS
Methods on objects are functions attached to the object's class; the syntax instance.method(argument) is, for normal methods and functions, syntactic sugar forClass.method(instance, argument). Python methods have an explicit self parameter to access instance data, in contrast to the implicit self (or this) in some other object-oriented programming languages (e.g., C++, Java, Objective-C, or Ruby).
TYPING
Python uses duck typing and has typed objects but untyped variable names. Type constraints are not checked at compile time; rather, operations on an object may fail, signifying that the given object is not of a suitable type. Despite being dynamically typed, Python is strongly typed, forbidding operations that are not well-defined (for example, adding a number to a string) rather than silently attempting to make sense of them.
LIBRARIES
Python has a large standard library, commonly cited as one of Python's greatest strengths, providing tools suited to many tasks. This is deliberate and has been described as a "batteries included" Python philosophy. For Internet-facing applications, many standard formats and protocols (such as MIME and HTTP) are supported. Modules for creating graphical user interfaces, connecting to relational databases, pseudorandom number generators, arithmetic with arbitrary precision decimals,[77] manipulating regular expressions, and doing unit testing are also included.
As of January 2016, the Python Package Index, the official repository of third-party software for Python, contains more than 72,000 packages offering a wide range of functionality, including:
graphical user interfaces, web frameworks, multimedia, databases, networking and communications
test frameworks, automation and web scraping, documentation tools, system administration
scientific computing, text processing, image processing


INTRODUCTION TO RASPBERRY PI
The Raspberry Pi is a series of credit card–sized single-board computers developed in the United Kingdom by the Raspberry Pi Foundation with the intent to promote the teaching of basic computer science in schools and developing countries. The original Raspberry Pi and Raspberry Pi 2 are manufactured in several board configurations through licensed manufacturing agreements with Newark element14 (Premier Farnell), RS Components and Egoman. The hardware is the same across all manufacturers.
Several generations of Raspberry Pi's have been released.
All models feature a Broadcom system on a chip (SOC) which include an ARM compatible CPU and an on chip graphics processing unit GPU (aVideoCore IV). CPU speed range from 700 MHz to 1.2 GHz for the Pi 3 and on board memory range from 256 MB to 1 GB RAM. Secure Digital SD cards are used to store the operating system and program memory in either the SDHC or MicroSDHC sizes. Most boards have between one and four USB slots, HDMI and composite video output, and a 3.5 mm phono jack for audio. Lower level output is provided by a number of GPIO pins which support common protocols like I2C. Some models have an RJ45 Ethernet port and the Pi 3 has on board WiFi 802.11n and Bluetooth.
The Foundation provides Debian and Arch Linux ARM distributions for download, and promotes Python as the main programming language.




RAM
On the older beta model B boards, 128 MB was allocated by default to the GPU, leaving 128 MB for the CPU. On the first 256 MB release model B (and model A), three different splits were possible. The default split was 192 MB (RAM for CPU), which should be sufficient for standalone 1080p video decoding, or for simple 3D, but probably not for both together. 224 MB was for Linux only, with only a 1080p framebuffer, and was likely to fail for any video or 3D. 128 MB was for heavy 3D, possibly also with video decoding (e.g. XBMC). Comparatively the Nokia 701 uses 128 MB for the Broadcom VideoCore IV. For the new model B with 512 MB RAM initially there were new standard memory split files released( arm256_start.elf, arm384_start.elf, arm496_start.elf) for 256 MB, 384 MB and 496 MB CPU RAM (and 256 MB, 128 MB and 16 MB video RAM). But a week or so later the RPF released a new version of start.elf that could read a new entry in config.txt (gpu_mem=xx) and could dynamically assign an amount of RAM (from 16 to 256 MB in 8 MB steps) to the GPU, so the older method of memory splits became obsolete, and a single start.elf worked the same for 256 and 512 MB Raspberry Pis.













INTRODUCTION TO TWILIO
Twilio Messaging allows you to:
1. Receive SMS and MMS messages to your Twilio phone numbers and reply back with SMS and MMS messages
2. Send SMS MMS messages using Twilio's REST API
3. Track SMS conversations
4. Send SMS messages during phone calls

Receive and reply to SMS 
When you buy an SMS-enabled Twilio phone number, you can associate that phone number with a URL. When someone sends a text message to that phone number, Twilio makes an HTTP request to your URL with the body of the message and the sender's phone number. You can then respond to the Message by returning a reply message in the HTTP response to Twilio.
Send SMS messages via the REST API
You can also send messages using Twilio's REST API. To send a message, just make an HTTP POST to Twilio with the body of the message and the phone number you want to send it to. SMS messages must be sent from Twilio SMS-enabled phone numbers due to the architecture of the global SMS network.
To send an outgoing SMS message perform an HTTP POST to the Messages resource URI. We will also use the Twilio PHP Library for making REST requests.
<?php
/* Send an SMS using Twilio. You can run this file 3 different ways:
*
* - Save it as sendnotifications.php and at the command line, run 
* php sendnotifications.php
*
* - Upload it to a web host and load mywebhost.com/sendnotifications.php 
* in a web browser.
* - Download a local server like WAMP, MAMP or XAMPP. Point the web root 
* directory to the folder containing this file, and load 
* localhost:8888/sendnotifications.php in a web browser.
*/
// Step 1: Download the Twilio-PHP library from twilio.com/docs/libraries, 
// and move it into the folder containing this file.
require "Services/Twilio.php";
// Step 2: set our AccountSid and AuthToken from www.twilio.com/user/account
$AccountSid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
$AuthToken = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY";
// Step 3: instantiate a new Twilio Rest Client
$client = new Services_Twilio($AccountSid, $AuthToken);
// Step 4: make an array of people we know, to send them a message. 
// Feel free to change/add your own phone number and name here.
$people = array(
"+919654328695" => "Somya",
"+918010257683" => "Fatima",
"+919953159744" => "",
);
// Step 5: Loop over all our friends. $number is a phone number above, and 
// $name is the name next to it
foreach ($people as $number => $name) {
$sms = $client->account->messages->sendMessage(
// Step 6: Change the 'From' number below to be a valid Twilio number 
// that you've purchased, or the (deprecated) Sandbox number
"YYY-YYY-YYYY", 
// the number we are sending to - Any phone number
$number,
// the sms body
"Hey $name! Let’s see if this is working."
);
// Display a confirmation message on the screen
echo "Sent message to $name";
}

Let’s look at the details:
First, head over to the Twilio website and log into your Twilio Account page. On the Dashboard there is a section labeled "API Credentials". There you will find your Account SID and Auth Token. Copy those values and paste them into Account SID and Auth Token variables.
Next, we instantiate a new client object, set the request method to "POST", fill the 'To', 'From' and 'Body' parameters into an associative array, and make the REST API request to Twilio. The 'From' parameter should be the Sandbox phone number for trial accounts or a Twilio phone number you purchased for upgraded accounts.
If your REST request was successful, the SMS has been successfully queued for transmission. The SMS will be sent as soon as possible at a maximum rate of 1 message per second per 'From' phone number.

REFERENCES

http://www.tutorialspoint.com/python/
https://www.twilio.com/api
https://www.raspberrypi.org/documentation/
http://raspberrypi.stackexchange.com/
https://en.wikipedia.org/wiki/Python_(programming_language)
https://developers.google.com/web/quickstart/python
https://developer.android.com/guide/index.html


