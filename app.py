from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify(status='healthy', service='FlowOps DevOps Control Center')

@app.route('/api/overview')
def overview():
    return jsonify({
        'build_success_rate': '98.6%',
        'deployments': 24,
        'average_build_time': '2m 18s',
        'open_issues': 3,
        'health': 'healthy'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
