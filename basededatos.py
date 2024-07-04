import pymysql

def basededatos_inferno():
    conn = pymysql.connect( 
        host='193.144.42.124', 
        user='Misaki',  
        password = "1Super-Password", 
        db='inferno',
        port=33306
        )
    cur = conn.cursor() 
    cur.execute("select nivel, nome_nivel from admision where nome = 'Misaki'") 
    output = cur.fetchone() 
    conn.close() 
    nivel, pecado = output
    return("Nivel de inferno: " + str(nivel) + ", pecado cometido: " + pecado + ".")