from flask import *
import os
from logo import *

app=Flask(__name__)
app.config['SECRET_KEY']='logo'
app.config['UPLOAD_FOLDER']='H:/SEM 3/cloud lab/LOGO Project/img'

@app.route('/',methods=['GET','POST'])
def homepage():

    if request.method=='POST':
        file=request.files['file']
        file_loc=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_loc)
        out=detect_logos(file_loc)
        if out=='':
            return render_template('result.html',data=['NO LOGO PRESENT IN THE UPLOADED IMAGE'],image=file_loc)
        else:
            return render_template('result.html',data=out,image=file_loc)
    return render_template('LOGO.html')
        
        
        
    
