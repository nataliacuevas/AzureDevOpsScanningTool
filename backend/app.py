from flask import Flask, jsonify, request
from flask_cors import CORS
from ADOrequester import ADOrequester
from ADOgroup import ADOgroup
from ADOuser import ADOuser
from yamlHandler import reportHandler, reportWarning
app = Flask(__name__)
# CORS open for all origins, TODO: restrict for security
CORS(app) 

@app.route('/api/message', methods=['POST'])
def get_message():
    data = request.get_json()
    PAT : str = data.get('PAT', '')
    org : str = "testOrgpf" # todo: get it from payload/frontend

    requester = ADOrequester(PAT, org)
    adminDict : dict[ADOgroup, list[ADOuser]] = requester.getAllProjectAdmins()
    report = reportHandler()
    warnings: list[reportWarning] = reportWarning.createMaxAdminWarningList(adminDict)
    report.addWarnings(warnings)
    report.addBody(org, adminDict)
    return jsonify(report.content)
    # return jsonify({"PAT": f"{PAT}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)