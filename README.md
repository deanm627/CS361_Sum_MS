# Sum Microservice
Calculates the sum of a set of numbers 

## Uses ZeroMQ
Set up client like so:
```
import zmq

context = zmq.Context()

# Connect to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")
```

## Request Format
List of numbers
Example:
```
nums = [1, 2, 5.5, 8, 14, 20]
socket.send_json(nums)
```

## Response Format
JSON with sum and success code (0)
{"sum": sum, "code": 0}

If error occurred, then code will be 1 with error message
{"error": error_msg, "code": 1}

Example:
```
response = socket.recv_json()
if response['code'] == 0:
    print(f"Sum: {response['sum']}")
else:
    print(f"Error: {response['error']}")
```
