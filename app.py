from flask import Flask,render_template,url_for,redirect,request,send_file,send_from_directory
import os
from pytube import YouTube
from io import BytesIO
from tempfile import TemporaryDirectory

app = Flask(__name__)

uplaoad_folder = 'static/photos/'

@app.route('/',  methods = ['GET','POST'])
def ytdownloader():
    if request.method == 'POST':
        try:
            getvideourl = request.form['url']
            url = YouTube(getvideourl)
            return render_template('ytdownloader.html',url = url,getvideourl = getvideourl)    
        except:
            return render_template('ytdownloader.html',notfound = getvideourl )       
     
    return render_template('ytdownloader.html')

@app.route('/audio', methods = ['POST','GET'])
def see_audio():
    if request.method == 'POST':
            
        url = request.form.get('audiourl') 
        my_audio = YouTube(url)
        with TemporaryDirectory() as tmp_dir:
            title = my_audio.title
            audio = my_audio.streams.get_by_itag(140).download(tmp_dir)
            file_bytes = b""
            with open(audio, "rb") as f:
                file_bytes = f.read()
            return send_file(BytesIO(file_bytes),  attachment_filename=title + '.mp3' , as_attachment=True)

@app.route('/video', methods = ['POST','GET'])
def see_video():
    if request.method == 'POST':
            
        url = request.form.get('videourl') 
        my_audio = YouTube(url)
        with TemporaryDirectory() as tmp_dir:
            title = my_audio.title
            audio = my_audio.streams.get_highest_resolution().download(tmp_dir)
            file_bytes = b""
            with open(audio, "rb") as f:
                file_bytes = f.read()
            return send_file(BytesIO(file_bytes),  attachment_filename=title + '.mp4' , as_attachment=True)



### End YTDownloader #####


if __name__ == "__main__":

    app.run(debug=True)