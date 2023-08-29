from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

# 設定上傳圖片的保存資料夾
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # 確認請求中包含檔案
        if 'file' not in request.files:
            return 'No file uploaded'

        file = request.files['file']
        
        # 確認檔案名稱不為空
        if file.filename == '':
            return 'No file selected'
        
        # 確認檔案是圖片格式
        if not allowed_file(file.filename):
            return 'Invalid file format'

        # 保存圖片到指定的資料夾中
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File uploaded successfully'

    return '''
    <h1>Upload ImageV1</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

# 檢查檔案是否為圖片格式
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5000, debug=True)
