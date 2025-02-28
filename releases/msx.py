




# ================
# MSX LAUNCHER 1.0
# ================
# 1. Instala la extensión de Python
# 2. Haz click al botón de arriba a la derecha (►)

# Si no aparece el botón, reinicia la página o cambia de navegador.



























# =================================================
# No toques nada de aquí para abajo, puedes dañarlo
# =================================================
F='.'
G=print
E='nt'
import requests as I,os as B,base64 as H,glob as D,time
if B.name==E:
	C='MSX'
	if not B.path.exists(C):B.mkdir(C)
else:C=F
if B.name==E:A=f"{C}\\.gitignore"
else:A='.gitignore'
if not B.path.exists(A):
	J='L3RhaWxzY2FsZS1jcwovd29ya19hcmVhKgpjb21wb3Nlci4qCi9QeXRob24qCioub3V0cHV0Ci9Nb2RnZXN0Ci90aGFub3MKL3ZlbmRvcgovYmtkaXIKamF2YS8KKi5leGUKKi5tc2kKKi50eHQKKi5weWMKKi5tc3AKKi5tc3gKbXN4LnB5';K=H.standard_b64decode(J).decode()
	with open(A,'w')as L:L.write(K)
def M(download_path=C):
	F='*.msx';L='https://minecraft-sx.github.io/data/links.json'
	if B.name==E:A=D.glob(f"{C}\\sel*.exe")
	else:A=D.glob(F)
	if len(A)>0:A=A[0]
	else:A=''
	try:
		J=I.get(L)
		if J.status_code==200:
			K=J.json()
			if B.name==E:H=K.get('latest_win')
			else:H=K.get('latest')
			A=H.split('/')[-1]
			if A in D.glob(F)or A in D.glob(f"{C}\\sel*.exe"):return A
			else:
				if B.name!=E:B.system('rm *.msx >> /dev/null 2>&1')
				else:B.system(f"del /f /q {C}\\sel*.exe")
				G('Actualizando tu versión de MSX...');time.sleep(1.5)
			M=B.path.join(download_path,A)
			with open(M,'wb')as N:N.write(I.get(H).content)
			return A
		else:
			G('Error al actualizar MSX')
			if A in D.glob(F)or A in D.glob(f"{C}\\sel*.exe"):return A
	except Exception as O:
		G(f"Error general: {O}")
		if A in D.glob(F)or A in D.glob(f"{C}\\sel*.exe"):return A
def N():
	A=M()
	if A==None:return
	elif A.split(F)[-1]=='msx':B.system(f"chmod +x {A} && ./{A}")
	elif A.split(F)[-1]=='exe':B.system(f"start /D {C} {C}\\{A}")
	else:B.system(f"python3 {A}")
N()
