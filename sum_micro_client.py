import zmq

context = zmq.Context()

# Connect to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# Sample data
nums = [1, 2, 5.5, 8, 14, 20]
socket.send_json(nums)

# Get and print the response
response = socket.recv_json()
if response['code'] == 0:
    print(f"Sum: {response['sum']}")
else:
    print(f"Error: {response['error']}")