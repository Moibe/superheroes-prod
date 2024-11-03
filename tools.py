def actualizar_creditos(nuevos_creditos, usuario):

     html_credits = f"""
     <div>
     <div style="text-align: left;">👤<b>Username: </b> {usuario}</div><div style="text-align: right;">💶<b>Credits Available: </b> {nuevos_creditos}</div>
     </div>
                       """
     
     return html_credits