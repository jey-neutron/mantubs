# Library
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time
import datetime
import pandas as pd
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# import csv
# from pathlib import Path
import streamlit as st
# from streamlit.components.v1 import html
import random
import requests
#import gspread
#from google.oauth2.service_account import Credentials



# config
import warnings
warnings.filterwarnings("ignore")
# init spin
def make_spinner(text="Loading..."): 
    with st.spinner(text):
        yield

#this_path = Path().resolve()
# logging (use logger.info di anaknya instead of print)
import logging
from streamlit.logger import get_logger

class StreamlitLogHandler(logging.Handler):
    def __init__(self, widget_update_func):
        super().__init__()
        self.widget_update_func = widget_update_func

    def emit(self, record):
        msg = self.format(record)
        self.widget_update_func(msg)
# Main View
# header html
st.set_page_config(page_title="ManTubs", layout="wide",page_icon=":material/panorama:")
st.logo("asset/mantubs-full.png", size='large')
icon = f"""<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,200,0,0&icon_names=calendar_add_on,chat,near_me,schedule,thumb_down,thumb_up" />"""
#next(sp0) # start spin on load web
st.markdown(f"""
    <style>
        {icon}"""+"""    
        * {
            box-sizing: revert !important; 
            font-family: Roboto, Arial, sans-serif !important; 
            scrollbar-width: none;  
        }
        .streamlit-wide{
            background-color: #0f0f0f !important; 
            overflow-x:hidden;  
            scrollbar-width: none;  
            color: white;
        }
        button[kind="primary"] {
            width: 100%;
            align-items:center;
            justify-content: center;  
            border-radius: 25px;          
            animation: zoom-in-zoom-out 2s ease infinite;
        }

          @keyframes zoom-in-zoom-out {
            0% {
              scale: 90%;
            }
            50% {
              scale: 105%;
            }
            100% {
              scale: 90%;
            }
          }

        .material-symbols-rounded.detail{
            width:fit-content;
            display:inline-block;
            font-size: 2rem !important;
        }
        .material-symbols-rounded.komen{
            width:fit-content;
            display:inline-block;
            font-size: 0.8rem !important;
        }
        .pfp{
            display:flex; 
            margin-bottom: 1rem;
        }
        .komen-text{
            font-size: 0.9rem;
            margin-bottom:0;
        }
        .komen-avatar{
            font-size: 30px;
            padding: 3px 10px;
            
        }
        .stButtonGroup label{
            display:none;
        }
        .stButtonGroup{
            width: 100%;
            overflow-x: scroll;
            overflow-y: hidden;
            max-height: 2.4rem;
        }
        .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak{
            margin:5px;
            display: ruby-text;
        }
        .footer{
            text-align: center;
            margin-bottom: -10rem;
        }
        .footer-small{
            color: lightgrey;
            font-size: 0.6rem;
        }
        button.st-ec.st-ed.st-ee.st-ef.st-eg.st-eh.st-bi.st-ei.st-ax.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-au.st-av.st-ej.st-ek.st-el.st-em.st-en.st-dj.st-cp.st-eo.st-ep.st-eq.st-er.st-ae.st-cx.st-es.st-et{
            display:none;
        }
    </style>
""", unsafe_allow_html=True) #css

if 'submit_disabled' not in st.session_state:
    st.session_state.submit_disabled = False

def fsubmit_disabled():
    st.session_state.submit_disabled = True

def fill_form(avatar='',nama='',pesan='',hadir=''):
    if hadir == "Hadir":
      value = {
          "entry.599393996": avatar,
          "entry.262422911": nama,
          "entry.2138165091": pesan,
          "entry.301499260": [hadir],
      }
    else :
      value = {
          "entry.599393996": avatar,
          "entry.262422911": nama,
          "entry.2138165091": pesan
      }
    #print(value, flush = True)
    return value
def submit_form(url, data):
    try:
        requests.post(url, data = data)
        return("Success")
    except:
        return("Error")

#st.button("reset-debug", on_click=btn_callback)
#if st.session_state.btn_show == True:

###########
# SET VARIABEL, ini yg perlu diganti, sama cek yg lain jugasi
###########
# set tanggal
future_date = datetime.datetime(2025, 11, 23, 9,0,0)
tanggal = "23 November 2025"
hari = "Minggu"
pukula = "09"
pukulb = "12"
countdown = future_date-datetime.datetime.now()
#
akun = "The Jeremy"
pp_akun = "https://conferenceoeh.com/wp-content/uploads/profile-pic-dummy.png"
# 
alamat = "Jl. Raya Darmasaba No.28, Darmasaba, Kec. Abiansemal, Kabupaten Badung, Bali 80352"
linkshare = "whatsapp://send?text=Lihat+undangannya+ini!"
linkcalendar = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text=GANTI+DISINI+EVENT&details=Untuk+detail+kunjungi:+SITE&dates=20251123T{pukula}0000/20251123T{pukulb}0000"
#
url_form = "https://docs.google.com/forms/d/e/1FAIpQLSeKN4CCWMiCu2BnojpyVSs1hCWfbT3S2-74R-sYh_moBl1JPA/formResponse"
#
#avatar = ["😸","🙀","🙊","🦄","🐶","🦊","🦁","🐯","🐭","🐰","🐼","🐻","🐸","🐲"]
avatar = ["😍","😇","😄","🤤","🫢","😳","😱","🥹","🤧","😭","🫠","😋","😏"]

# Kepada siapa
try:
  nama = st.query_params['kepada']
except:
  nama = ""

#st.session_state.btn_show = False
col1,col2,col3 = st.columns([1,1.5,1])
with col2:
  with st.container(border=True):

    # Div Komentar
    st.subheader("Komentar Anda ")
    #st.markdown('''<hr style="padding:0;margin:0">''', unsafe_allow_html=True)

    # Read komentar from gsheet
    sheet_id = "1YQ8VRbooIUtK9GHueumjmFvF2n2DstMFPN7daZuTDBg"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    df = df.sort_values(by=['Timestamp'], ascending=False)
    #df['Avatar (emoji)'] = df['Avatar (emoji)'].astype("string")
    df = df.fillna(" ")
    #print(df)
    #st.write(df.iloc[10] )
    #st.write(df.iloc[0]['Avatar (emoji)'] )
    #st.write(df.iloc[0]['Avatar (emoji)'] == " " )
    

    # Rule Form
    @st.dialog("Error", width='large')
    def error_kosong(): 
        st.warning('Maaf, isi dulu yang lengkap', icon="🙇‍♀️")
        #st.session_state.submit_disabled = False
        if st.button('Tutup'): st.rerun()
    @st.dialog("Error")
    def error_submit(): 
        st.error('Terjadi kesalahan ketika submit', icon="⚠️")
        #st.session_state.submit_disabled = False
        if st.button('Tutup'): st.rerun()
    @st.dialog("Error")
    def error_(e): 
        st.error(f"Terjadi kesalahan! {e}", icon="⚠️")
        #st.session_state.submit_disabled = False
        if st.button('Tutup'): st.rerun()
    @st.dialog("Error")
    def sukses(nama): 
        st.success(f"Pesan '{nama}' berhasil dikirim", icon='✅')
        #st.session_state.submit_disabled = False
        if st.button('Tutup'): st.rerun()

    # Div Form
    with st.form(key="comment"):
      st.write("Kirimkan pesan anda") 
      komen_avatar = st.pills("Avatar", avatar)
      komen_nama = st.text_input(
          "Nama",
          label_visibility="collapsed", 
          placeholder="Nama",
          value=nama
      )
      komen_catatan = st.text_area(
          "Pesan",
          label_visibility="collapsed",
          placeholder="Komentar anda ...",
      )
      #komen_hadir = st.pills("Hadir", ["Hadir","Maaf, berhalangan"])
      komen_hadir = ""
      submit = st.form_submit_button("Kirim", type="primary", use_container_width=True, on_click=fsubmit_disabled, disabled=st.session_state.submit_disabled)
    
      if submit:
        if komen_avatar == None: komen_avatar = random.choice(avatar)
        #st.write({
        #  'avatar': komen_avatar,
        #  'nama': komen_nama,
        #  'catatan': komen_catatan,
        #  'hadir': komen_hadir,
        #})
        #if 'btn_show' not in st.session_state:
        #  st.session_state.btn_show = True
        if komen_hadir != None and komen_catatan != "" and komen_nama != "":
          # baru isi ke gform
          try:
              #payload = generate_request_body(url, only_required = only_required)
              res = submit_form(url_form, fill_form(komen_avatar,komen_nama,komen_catatan,komen_hadir))
              if res == "Success":
                #st.toast(f"{komen_nama[:10]}'s msg submitted", icon='✅')
                sukses(komen_nama)
              else:
                #st.toast(f"Error on submit", icon='⚠️')
                error_submit()
              #print("Done!!!")
          except Exception as e:
              #import sys
              #exc_type, exc_obj, exc_tb = sys.exc_info()
              #st.toast(f"Error! {e}", icon='⚠️')
              error_submit(e)
              #st.error(f"Error! {e}, on line: {exc_tb.tb_lineno} {exc_type}", icon='⚠️')
              #print("Error!", e)
          
        else: 
          #st.toast("Maaf, isi dulu", icon="🙇‍♀️" )
          error_kosong()

      
      # if already submit
      if st.session_state.submit_disabled == True:
        st.markdown(f"""<p style="font-size:0.8rem; color:lightgrey; margin-top:0">*Sudah submit, jika ingin mengulang, silakan refresh halaman</p>""", unsafe_allow_html=True)
    
    #
    st.markdown(f"""{icon} <a href="#deskripsi" style="position:fixed; bottom:2rem; right:2rem; background-color:rgba(229,9,19,0.5); color:inherit; text-decoration:inherit"> &nbsp;△&nbsp;</a> """, unsafe_allow_html=True)
    st.markdown(f"&#8756; **{len(df)}** pesan, diurutkan dari pesan terbaru")
    # Div Print komentars
    with st.container(border=True, height=700):
      for i in range(len(df)): 
      #for i in range(1,15): 
        if (df.iloc[i]["Avatar (emoji)"])==" ": 
          pp = random.choice(avatar)
        else: pp = df.iloc[i]["Avatar (emoji)"]
        #st.write(pp)
        st.markdown(f'''
        <div class="pfp komen-text">
          <div class="pfp komen-avatar"> {pp} </div>
          <div class="pfp-text" style="line-height:normal">
            <span style="font-size:0.7rem" >@{df.iloc[i].Nama} <span style="color:lightgrey" >• 
              {datetime.datetime.strptime(str(df.iloc[i].Timestamp), "%d/%m/%Y %H:%M:%S").strftime("%d %b")}
            </span></span> <br>
            {df.iloc[i].Catatan} <br>
            <div style="color:grey; letter-spacing: 20px; line-height:2rem">
              <span class="material-symbols-rounded komen">thumb_up</span>
              <span class="material-symbols-rounded komen">thumb_down</span>
              <span class="material-symbols-rounded komen">chat</span>
            </div>
          </div>
        </div>
        ''',unsafe_allow_html=True)
        #st.feedback('thumbs', disabled=True)
    
    #st.table(df)
    # form nama entry.262422911
    # form catatan entry.2138165091 
    # form kehadiran entry.301499260_sentinel


  # Div end
  st.markdown(f'''
  <br>
  <br>
  <div class="footer">
    Terima kasih telah berpartisipasi! <br> Semoga berjumpa lagi! <br><br>
    <span class="footer-small">Digital made by {akun} with 💖</span>
  </div>
  ''',unsafe_allow_html=True)