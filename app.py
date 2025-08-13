from flask import Flask, render_template,request
from scraper import scrape_news

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def home():
    results = []
    keyword = ""
    error_message = ""
    
    if request.method == "POST":
        keyword = request.form['keyword']
        if keyword:
            keyword = keyword.lower().strip()
        print("Keyword nhận được: ",keyword)
        
        try:
            results = scrape_news(keyword)
            print("Kết quả của Scraper: ",results)
        except Exception as e: 
            error_message = "Đã xảy ra lỗi tìm kiếm. Vui lòng thử lại sau. "
            print("Lỗi khi scraper",e)
        
    return render_template('index.html',results=results,keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)
       