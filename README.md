# Noxtton



## Brief overview
    This application searches and retrieves GitHub repositories in ascending or descending order.
     
    
 ## Instructions
    Step 1: Clone Git repository https://github.com/metacomplex/Noxtton.git
    Step 2: Navigate to the directory where the project was cloned. example: cd D:\Noxtton\main
    Step 3: Launch the application using following command: python Main.py param1 param2 param3
    
    Parameters above correspond to the following function: get_repos(query, sort_order=None, ignore=None) 
    param1 (query) the keyword for searching among the repositories. 
    param2 (sort_order) provides the output in ascending or descending order. Accepted values for this parameter are "asc" or "desc". Otherwise the exception will be raised.
    param3 (ignore) if present repositories containing param3 will be ignored and not retrieved.
    
    param2, param3 are optional.

 ## Sample input/output
    Input: python Main.py rammstein desc ram
    Output: https://api.github.com/search/repositories?q=rammstein&page=1&per_page=100
            https://api.github.com/search/repositories?q=rammstein&page=2&per_page=100
            Number of retrieved repositories - 4
            songPopularity
            rt-blinder
            a-song
            Arduino_Du_Hast
    
    Sent requests will be saved in requests.log