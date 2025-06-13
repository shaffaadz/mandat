from flask import Flask, render_template_string
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

# Data dummy
data = [10, 20, 30, 40, 50]
rata_rata = sum(data) / len(data)

@app.route('/')
def index():
    return "Aplikasi Analisa Data - Buka /analisa untuk lihat grafik hasil"

@app.route('/analisa')
def analisa():
    x = list(range(1, len(data)+1))
    trace_data = go.Scatter(x=x, y=data, mode='lines+markers', name='Data')
    trace_rata = go.Scatter(x=x, y=[rata_rata]*len(data), mode='lines', name='Rata-rata', line=dict(dash='dash'))

    layout = go.Layout(title='Visualisasi Data dan Rata-rata', xaxis=dict(title='Index'), yaxis=dict(title='Nilai'))
    fig = go.Figure(data=[trace_data, trace_rata], layout=layout)
    plot_div = pyo.plot(fig, output_type='div')

    return render_template_string("""
        <html>
        <head><title>Grafik Analisa Data</title></head>
        <body>
            <h1>Grafik Analisa Data</h1>
            {{ plot_div|safe }}
        </body>
        </html>
    """, plot_div=plot_div)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
