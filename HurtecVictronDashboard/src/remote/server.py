import threading
from flask import Flask, request, jsonify


def create_app(main_window):
    app = Flask(__name__)

    @app.route('/tabs', methods=['GET'])
    def list_tabs():
        tabs = [main_window.tabs.tabText(i) for i in range(main_window.tabs.count())]
        return jsonify(tabs)

    @app.route('/tabs', methods=['POST'])
    def add_tab():
        data = request.get_json(force=True)
        url = data.get('url')
        name = data.get('name', url)
        username = data.get('username', '')
        password = data.get('password', '')
        if url:
            main_window.add_tab(url, name, username, password)
            return '', 204
        return 'missing url', 400

    @app.route('/tabs/<int:index>', methods=['DELETE'])
    def remove_tab(index):
        if 0 <= index < main_window.tabs.count():
            main_window.tabs.removeTab(index)
            return '', 204
        return 'invalid index', 404

    return app


def start_server(main_window, host='0.0.0.0', port=8765):
    app = create_app(main_window)
    thread = threading.Thread(target=lambda: app.run(host=host, port=port, debug=False, use_reloader=False))
    thread.daemon = True
    thread.start()
    return thread
