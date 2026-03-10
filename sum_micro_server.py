# Sum Microservice

import zmq

def compute_sum(nums):
    # Calculates sum and returns result, or error if one occurs
    try:
        total = sum(nums)
    except TypeError as e:
        return {"error": "Error computing sum: " + str(e), "code": 1}
    except Exception as e:
        return {"error": "An unexpected error occurred: " + str(e), "code": 1}
    else:
        return {"sum": total, "code": 0}

# Establish server and attach to port
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    print("Listening on 5556")
    # Get data from client
    data = socket.recv_json()
    # Compute sum and generate response
    results = compute_sum(data)
    # Send response
    socket.send_json(results)