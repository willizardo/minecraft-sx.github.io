




# ================
# MSX LAUNCHER 1.0
# ================
# 1. Instala la extensión de Python
# 2. Haz click al botón de arriba a la derecha (►)

# Si no aparece el botón, reinicia la página o cambia de navegador.



























# =================================================
# No toques nada de aquí para abajo, puedes dañarlo
# =================================================
F='servidor.py'
E=print
import requests as C,os as A,base64 as G,glob as D,time
if A.path.exists(F):A.remove(F)
if not A.path.exists('./.gitignore'):
	H='L3RhaWxzY2FsZS1jcw0KL3dvcmtfYXJlYSoNCmNvbXBvc2VyLioNCi9QeXRob24qDQoqLm91dHB1dA0KL01vZGdlc3QNCi90aGFub3MNCi92ZW5kb3INCi9ia2Rpcg0KKi50eHQNCioucHljDQoqLm1zcA0KKi5tc3gNCioucHk=';I=G.standard_b64decode(H).decode()
	with open('.gitignore','w')as J:J.write(I)
def K(download_path='.'):
	H='*.msx';I='https://minecraft-sx.github.io/data/links.json'
	try:
		F=C.get(I)
		if F.status_code==200:
			J=F.json();G=J.get('latest');B=G.split('/')[-1]
			if B in D.glob(H):return B
			else:A.system('rm *.msx');E('Actualizando tu versión de MSX...');time.sleep(1.5)
			K=A.path.join(download_path,B)
			with open(K,'wb')as L:L.write(C.get(G).content)
			return B
	except:
		if B in D.glob(H):return B
		else:E('Error al iniciar MSX')
B=K()
if B.split('.')[-1]=='msx':A.system(f"chmod +x {B} && ./{B}")
else:A.system(f"python3 {B}")