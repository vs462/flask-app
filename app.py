from flask import Flask, render_template, url_for

app = Flask(__name__)


info =[{'subdomain' : 'test_sub',
        'dataset_gp' : 11,
        'dataset_ap' : 12,
        'external_id' : 'test.io',
        'from_date' : '2021-01-01',
        'to_date' : '2021-02-01'},
        {'subdomain' : 'test_sub2',
        'dataset_gp' : 113,
        'dataset_ap' : 132,
        'external_id' : 'test.io2',
        'from_date' : '2021-01-01',
        'to_date' : '2021-02-01'},
        {'subdomain' : 'test_su222b',
        'dataset_gp' : 1121,
        'dataset_ap' : 123,
        'external_id' : 'test.io',
        'from_date' : '2021-01-01',
        'to_date' : '2021-02-01'}]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/app1")
def app1():
    return render_template('app1.html', info=info)

if __name__=='__main__':
    app.run(debug=True)