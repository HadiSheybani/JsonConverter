


help_command = """
Convertor Will Convert a json array to nested dictionary of dictionaries of 
arrays.
********************************************************************************
Usage:

Commands:

    --runtests          will run all of tests (include Convertor API tests ans 
                        Rest API test)

        example:
            python run_converter --runtests

    --django-command    will execute django server command

        example:
            python run_convertor --django-command runserver


    --help              show usage

you can run program by console like this:
    Linux:
        cat input | python run_convertor.py nesting_level_1 nesting_level_2 ...

        example:
            cat samples/input.json | python run_convertor.py currency country city
            
    Windows:
        type input | python run_convertor.py nesting_level_1 nesting_level_2 ...

        example:
            type samples\input.json | python run_convertor.py currency country city
    

you can install requirements like this:
    pip install -r requirements.txt

********************************************************************************
"""