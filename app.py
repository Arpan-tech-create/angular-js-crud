from flask import Flask, jsonify, render_template,request
import db  # Importing the database functions from db.py

app = Flask(__name__)

@app.route('/')
def index():
  
    return render_template('index.html')

@app.route('/get_regions', methods=['GET'])
def get_data():
 
    regs = db.get_distinct_regions()
    if regs is not None:
        return jsonify([region[0] for region in regs])
    return jsonify([]), 500




@app.route("/get_details",methods=["GET"])

def get_det():
    region=request.args.get("region")
    if region:
        details=db.get_details(region)
        if details is not None:
            return jsonify(details)
    
    return jsonify([]),500

if __name__ == "__main__":
    app.run(port=5045,host='0.0.0.0',debug=True)