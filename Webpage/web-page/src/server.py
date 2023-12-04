import sys
import os
sys.path.append(os.getcwd() + "\\..\\..\\AI")
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from traffic_volume_classification import TrafficModel
import torch
import numpy as np
import math

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
input_size = 3
output_size = 1
hidden_size = 32
num_layers = 1
model = TrafficModel(output_size, input_size, hidden_size, num_layers)

# @app.route('/process', methods=['POST'])
# async def process():
#     data = request.get_json()
#     start = data['start']
#     end = data['end']
    
#     res = {
#         "status": "success",
#         "message": "Data receieved successfully"
#     }
    
#     return jsonify(res)

@app.route('/process', methods=['GET'])
@cross_origin()
def query_model():
    # Pull the below from POST body instead...
    hour = 0
    minute = 0
    id = 1000
    sample = torch.Tensor(np.array([hour, minute, id]))
    sample = torch.reshape(sample, (1, 1, 3))
    return str(math.floor(model(sample)[0].item() * 500)) + " minutes"

if __name__ == "__main__":
    # Config AI model
    model.load_state_dict(torch.load("../../AI/models/model-1000.pt"))
    model.eval()
    
    # Start server
    app.run(port=8000, debug=True)