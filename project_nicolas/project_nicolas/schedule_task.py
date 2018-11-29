"""
File for task tab of python anywhere,

Call once a day by pythonanywhere task.
"""

import webbrowser


def call_check_link():
    """
    Call url to make the site execute the check_link view.
    :return: None
    """
    print("Call check link form the tasy system") #Note for the server.
    url = "ngagne.pythonanywhere.com/appBookmarks/check_link/"
    webbrowser.open(url)

    return None


call_check_link()
