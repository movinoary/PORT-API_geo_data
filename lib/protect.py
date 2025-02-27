import requests
from utils.generate_env  import generate_env

def protect_decode():
    url = f"{generate_env()['api_module']}/decode"
    body={
        'encoded':"QUFBQWV3QUFBQ0lBQUFCZkFBQUFhUUFBQUdRQUFBQWlBQUFBT2dBQUFDQUFBQUFpQUFBQU5nQUFBRFlBQUFCaEFBQUFNUUFBQUdRQUFBQm1BQUFBTUFBQUFHVUFBQUJsQUFBQU13QUFBRFlBQUFCaUFBQUFOUUFBQURFQUFBQmhBQUFBTlFBQUFETUFBQUJrQUFBQU53QUFBRE1BQUFCbEFBQUFaQUFBQURVQUFBQm1BQUFBSWdBQUFDd0FBQUFnQUFBQUlnQUFBR2tBQUFCa0FBQUFYd0FBQUdzQUFBQmxBQUFBZVFBQUFDSUFBQUE2QUFBQUlBQUFBQ0lBQUFCV0FBQUFUd0FBQUZNQUFBQlRBQUFBVHdBQUFDMEFBQUF6QUFBQU1BQUFBREVBQUFBd0FBQUFMUUFBQUVFQUFBQk1BQUFBU2dBQUFGQUFBQUJDQUFBQUxRQUFBRGdBQUFBeUFBQUFOQUFBQURZQUFBQTRBQUFBU0FBQUFGY0FBQUF0QUFBQVFnQUFBRllBQUFCYUFBQUFSQUFBQUUwQUFBQlRBQUFBUkFBQUFFb0FBQUEyQUFBQVR3QUFBQzBBQUFCVEFBQUFPUUFBQUVNQUFBQkJBQUFBU0FBQUFDSUFBQUFzQUFBQUlBQUFBQ0lBQUFCMUFBQUFjd0FBQUdVQUFBQnlBQUFBYmdBQUFHRUFBQUJ0QUFBQVpRQUFBQ0lBQUFBNkFBQUFJQUFBQUNJQUFBQjFBQUFBY3dBQUFHVUFBQUJ5QUFBQWJnQUFBR0VBQUFCdEFBQUFaUUFBQUNJQUFBQXNBQUFBSUFBQUFDSUFBQUJsQUFBQWJRQUFBR0VBQUFCcEFBQUFiQUFBQUNJQUFBQTZBQUFBSUFBQUFDSUFBQUJ5QUFBQWJ3QUFBR01BQUFCbEFBQUFkZ0FBQUc4QUFBQXVBQUFBYVFBQUFHUUFBQUJBQUFBQVp3QUFBRzBBQUFCaEFBQUFhUUFBQUd3QUFBQXVBQUFBWXdBQUFHOEFBQUJ0QUFBQUlnQUFBSDA9"
    }
    response = requests.post(url, json=body)
    data = response.json()
    
    isProtec=""
    if data['message'] == 'Success':
        isProtec = True
    elif data['message'] == 'Error':
        isProtec = False
    return isProtec

