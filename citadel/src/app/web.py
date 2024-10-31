from quart import Quart, request, jsonify, render_template

app = Quart(__name__)

@app.route('/')
async def home():
    return await render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)