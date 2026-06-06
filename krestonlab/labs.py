LABS = {
    "DVWA": {
        "image": "vulnerables/web-dvwa",
        "internal_port": 80,
        "default_port": 8089,
        "description": "Damn Vulnerable Web Application",
        "env": {},
        "volumes": []
    },

    "Mutillidae": {
        "image": "citizenstig/nowasp",
        "internal_port": 80,
        "default_port": 8081,
        "description": "OWASP Mutillidae II",
        "env": {},
        "volumes": []
    },

    "WebGoat": {
        "image": "szsecurity/webgoat",
        "internal_port": 80,
        "default_port": 8082,
        "description": "OWASP WebGoat",
        "env": {},
        "volumes": []
    },

    "bWAPP": {
        "image": "raesene/bwapp",
        "internal_port": 80,
        "default_port": 8083,
        "description": "Buggy Web Application",
        "env": {},
        "volumes": []
    },

    "JuiceShop": {
        "image": "bkimminich/juice-shop",
        "internal_port": 3000,
        "default_port": 8084,
        "description": "OWASP Juice Shop",
        "env": {},
        "volumes": []
    },
"XVWA": {
    "image": "teejaymehta/xvwa",
    "internal_port": 80,
    "default_port": 8087,
    "description": "Xtreme Vulnerable Web Application",
    "env": {},
    "volumes": []
},

"AltoroMutual": {
    "image": "eystsen/altoro-mutual",
    "internal_port": 8080,
    "default_port": 8088,
    "description": "Altoro Mutual Banking Application",
    "env": {},
    "volumes": []
},

"Hackazon": {
    "image": "mutzel/all-in-one-hackazon",
    "internal_port": 80,
    "default_port": 8090,
    "description": "Hackazon Vulnerable E-Commerce",
    "env": {},
    "volumes": []
},

"NodeGoat": {
    "image": "owasp/nodegoat",
    "internal_port": 4000,
    "default_port": 8085,
    "description": "OWASP NodeGoat",
    "env": {},
    "volumes": []
}
    
}
# krestonlab - http://rodrigoviana.dev.br
