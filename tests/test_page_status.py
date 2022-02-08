import requests

# credentials for testing account used to access protected pages
creds = {
    'user_email': 'testing@gmail.com',
    'user_password': 'TEMPTestingAccount'
}

# returns status of unprotected page
def unprotected_page_status(route):
    page = requests.get('http://127.0.0.1:5000/' + route)
    # makes sure that no protected page is accidentally input/tested as unprotected
    assert page.url is ('http://127.0.0.1:5000/' + route) or 'http://127.0.0.1:5000/'
    return page.status_code

# returns status of protected page
def protected_page_status(route):
    with requests.Session() as s:
        # uses test account credentials to access protected pages
        s.post('http://127.0.0.1:5000/login', data=creds)

        page = s.get('http://127.0.0.1:5000/' + route)
        # makes sure the page is not redirected back to login page or any other page
        assert page.url != 'http://127.0.0.1:5000/login'
        return page.status_code

# tests pages making sure they return 200 code (OK)
def test_page_status():
    # unprotected pages are pages that don't require an account to access
    assert unprotected_page_status('/') == 200
    assert unprotected_page_status('login') == 200
    assert unprotected_page_status('register') == 200
    
    # protected pages are pages that DO require an account to access
    assert protected_page_status('calendar') == 200
    assert protected_page_status('tasks') == 200
    assert protected_page_status('weekly') == 200
    assert protected_page_status('dashboard') == 200
   

test_page_status()


