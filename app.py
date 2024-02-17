from flask import Flask ,render_template
import pickle


popular_df = pickle.load(open('popular.pkl','rb'))
app = Flask(__name__)
book_names = list(popular_df['Book-Title'].values)
@app.route('/')




 

def index():
    
    return render_template('index.html',book_name=book_names)


if __name__ == '__main__':
    app.run(debug=True)