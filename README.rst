 simple rest
 -----------

 This is a toy app that returns a value for a given (existent) key.
 
 If key does not exist the expect result is:
    {<key>, "Not Found"} 
 
 If a key is not provided:
    {"undefined":"Not Found"}
 
 User can also creates its own dictonary file and define in the environment
 variable SIMPLE_REST_INPUT
 e.g.:
    $ export SIMPLE_REST_INPUT=/tmp/my_dict.in

    
 how to install::

 $ python3 -m pip install git+https://github.com/Fonseca-Rafael/simple_rest.git

 all dependencies are listed in the package configuration


 how to use::

 export SIMPLE_REST_INPUT=<dictionary filename>
 >>> import simple_rest
 >>> simple_rest.run()

 Now in another terminal you can check the app by::
 $  curl http://127.0.0.1:5000/?item=bar | jq
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100    13  100    13    0     0   5996      0 --:--:-- --:--:-- --:--:-- 13000
    {
    "bar": "foo"
    }


 testing::

 Tests are done in package building time.
 $ python3 setup.py test
