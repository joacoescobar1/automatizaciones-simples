import csv
CSS="""<style>@font-face{font-family:I;src:url('file:///usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf')}
*{box-sizing:border-box;margin:0}body{width:1280px;height:720px;overflow:hidden;font-family:I,sans-serif;background:radial-gradient(circle at 85% 0%,#ccfbf1 0,#f8fafc 45%,#fafaf9 100%);color:#0f172a;letter-spacing:-.025em}
.c{height:100%;display:flex;flex-direction:column;justify-content:center;padding:0 96px}
h1{font-size:80px;font-weight:780;line-height:1.04}h2{font-size:48px;font-weight:720;line-height:1.1}.t{color:#0d9488}.k{display:inline-block;align-self:flex-start;font-size:17px;font-weight:650;letter-spacing:.14em;text-transform:uppercase;color:#0f766e;background:#ccfbf1;padding:8px 16px;border-radius:99px;margin-bottom:26px}
.s{font-size:30px;color:#64748b;margin-top:24px;font-weight:450}
.win{background:#fff;border-radius:20px;box-shadow:0 1px 2px #0f172a0d,0 24px 60px -12px #0f172a26;border:1px solid #e2e8f0;overflow:hidden;color:#111}.bar{height:36px;background:#f8fafc;border-bottom:1px solid #eef2f6;display:flex;gap:8px;align-items:center;padding:0 16px}.bar i{width:11px;height:11px;border-radius:50%;background:#e2e8f0}
.row{display:flex;gap:48px;align-items:center}
table{border-collapse:collapse;font-size:17px;width:100%}td,th{color:#0f172a;border-bottom:1px solid #f1f5f9;padding:12px 14px;text-align:left}th{background:#fff;font-weight:600;color:#94a3b8;font-size:14px;text-transform:uppercase;letter-spacing:.05em}.n{color:#cbd5e1;width:36px;text-align:center}
.p{padding:4px 12px;border-radius:99px;font-size:14px;font-weight:600}.ok{background:#dcfce7;color:#166534}.pe{background:#fef3c7;color:#92400e}.ca{background:#fee2e2;color:#991b1b}
.hl td{background:#f0fdfa}
.msg{background:#fff;border:1px solid #e2e8f0;border-radius:22px;padding:24px 28px;font-size:25px;max-width:450px;box-shadow:0 24px 60px -12px #0f172a2e;line-height:1.4}.msg b{color:#0d9488}.msg small{display:block;color:#94a3b8;font-size:15px;margin-top:10px;text-align:right}.msg .wa{font-size:14px;font-weight:650;color:#16a34a;letter-spacing:.06em;text-transform:uppercase;margin-bottom:10px}
.step{flex:1;background:#fff;border:1px solid #e2e8f0;box-shadow:0 18px 40px -16px #0f172a22;border-radius:22px;padding:36px}.step b{font-size:22px;color:#fff;background:#0d9488;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:22px}.step span{font-size:30px;font-weight:650}
.price{font-size:110px;font-weight:800;color:#0f172a;letter-spacing:-.04em}.btn{display:inline-block;background:#0d9488;color:#fff;font-size:34px;font-weight:700;padding:24px 44px;border-radius:18px;margin-top:40px;box-shadow:0 18px 40px -10px #0d948880}
</style>"""
rows=list(csv.DictReader(open('../../demos/demo2-turnos-recordatorios/turnos_template.csv')))
cls={'confirmado':'ok','pendiente':'pe','cancelado':'ca'}
def sheet(hl=None,sent=False):
  h='<table><tr><th class=n></th><th>Cliente</th><th>Fecha</th><th>Hora</th><th>Servicio</th><th>Estado</th><th>Recordatorio</th></tr>'
  for i,r in enumerate(rows):
    rec='✓ enviado' if sent and r['estado']!='cancelado' else '—'
    h+=f"<tr class='{'hl' if i==hl else ''}'><td class=n>{i+2}</td><td>{r['cliente']}</td><td>{r['fecha'][5:].replace('-','/')}</td><td>{r['hora']}</td><td>{r['servicio']}</td><td><span class='p {cls[r['estado']]}'>{r['estado']}</span></td><td>{rec}</td></tr>"
  return h+'</table>'
leads="<table><tr><th class=n></th><th>Fecha</th><th>Nombre</th><th>Teléfono</th><th>Mensaje</th></tr><tr><td class=n>2</td><td>24/10 18:02</td><td>Lucas Gómez</td><td>+54 9 379 4…</td><td>Precio envío a Corrientes?</td></tr><tr class=hl><td class=n>3</td><td>25/10 19:41</td><td>Carla Benítez</td><td>+54 9 362 4…</td><td>¿Turno jueves a la tarde?</td></tr></table>"
W=lambda inner,w=640:f"<div class=win style='width:{w}px'><div class=bar><i></i><i></i><i></i></div>{inner}</div>"
S={
'01':"<div class=c><div class=k>Pymes de Chaco y Corrientes</div><h1>Consultas que se pierden<br><span class=t>en WhatsApp.</span></h1><div class=s>Clientes que faltan al turno.</div></div>",
'02':"<div class=c><div class=k>Automatización 1</div><h1>Formulario → Planilla<br><span class=t>→ Aviso al celular.</span></h1></div>",
'03':f"<div class=c><div class=row><div style='flex:0 0 380px'><div class=k>Paso 1</div><h2>El cliente completa<br>un form simple.</h2></div>{W('<img src=form.png style=\"width:100%;display:block\">',700)}</div></div>",
'04':f"<div class=c><div class=row><div style='flex:0 0 330px'><div class=k>Paso 2</div><h2>Queda guardado<br><span class=t>solo</span>.</h2><div class=s>En tu Google Sheet.</div></div>{W(leads,760)}</div></div>",
'05':"<div class=c><div class=row><div style='flex:1'><div class=k>Paso 3</div><h1>Te avisa<br><span class=t>al toque.</span></h1><div class=s>Ninguna consulta perdida.</div></div><div class=msg><div class=wa>WhatsApp · ahora</div><b>Nueva consulta</b><br>Carla Benítez · +54 9 362…<br>“¿Turno jueves a la tarde?”<small>19:41</small></div></div></div>",
'06':f"<div class=c><div class=k>Automatización 2 · Turnos</div><h2 style='margin-bottom:28px'>Tu agenda, en una planilla.</h2>{W(sheet(),1100)}</div>",
'07':"<div class=c><div class=row><div style='flex:1'><div class=k>El día anterior</div><h1>Recordatorio<br><span class=t>automático.</span></h1></div><div class=msg><div class=wa>WhatsApp · 10:00</div>Hola Pedro 👋 Te recordamos tu turno <b>mañana 11:30</b>.<br>Respondé <b>SÍ</b> para confirmar.<small>Enviado 10:00 ✓✓</small></div></div></div>",
'08':f"<div class=c><div class=k>Resultado</div><h2 style='margin-bottom:28px'>Menos ausentes. <span class=t>Cero llamadas.</span></h2>{W(sheet(1,True),1100)}</div>",
'09x':"<div class=c><div class=k>Cómo trabajamos</div><div class=row style='align-items:stretch'><div class=step><b>1</b><span>Me contás por escrito</span></div><div class=step><b>2</b><span>Lo armo en 3–5 días</span></div><div class=step><b>3</b><span>Queda andando</span></div></div><div class=s>Sin reuniones. Sin tus contraseñas.</div></div>",
'10':"<div class=c><div class=k>Precio cerrado</div><div class=price>ARS 60–100k</div><div class=s style='font-size:36px'>Pago único. Sin reuniones. Sin claves.</div></div>",
'11':"<div class=c style='align-items:center;text-align:center'><h1>¿Lo armamos<br><span class=t>para tu negocio?</span></h1><div class=btn>Escribime en Workana →</div><div class=s>Listo en 3–5 días</div></div>",
}
for k,v in S.items(): open(f's{k}.html','w').write(f"<html><head><meta charset=utf-8>{CSS}</head><body>{v}</body></html>")
