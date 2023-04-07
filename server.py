from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    rows = 8
    cols = 8
    light_color = 'red'
    dark_color = 'black'
    return render_template('index.html', rows=rows, cols=cols, light_color=light_color, dark_color=dark_color)

@app.route('/<light_color>/<dark_color>')
def custom_colors(light_color, dark_color):
    rows = 8
    cols = 8
    return render_template('index.html', rows=rows, cols=cols, light_color=light_color, dark_color=dark_color)

@app.route('/<int:x>')
def custom_rows(x):
    rows = x
    cols = 8
    light_color = 'red'
    dark_color = 'black'
    return render_template('index.html', rows=rows, cols=cols, light_color=light_color, dark_color=dark_color)

@app.route('/<int:x>/<int:y>')
def custom_board(x, y):
    rows = x
    cols = y
    light_color = 'red'
    dark_color = 'black'
    return render_template('index.html', rows=rows, cols=cols,light_color=light_color, dark_color=dark_color)


if __name__ == '__main__':
    app.run(debug=True)