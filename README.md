Miembros del Grupo:
1. Anthony Márquez Camacho: anthony.marquez@upr.edu
2. David Carrión Beníquez: david.carrion@upr.edu
3. Estefanía Torres Collado: estefania.torres1@upr.edu
4. Christopher Vegerano López: christopher.vegerano@upr.edu

Video de Fase 1: https://youtu.be/Vogf6cMRgPo

Rest API

  -Ruta Principal: https://pichon-azul.herokuapp.com/PichonAzul
  
  1. Usuarios

    -Obtener todos los usuarios: https://pichon-azul.herokuapp.com/PichonAzul/users
    
    -Crear nuevo usuario: https://pichon-azul.herokuapp.com/PichonAzul/users
    
    -Obtener usuario por id: https://pichon-azul.herokuapp.com/PichonAzul/users/uid 
    
    -Poner o cambiar informacion en usuario existente: https://pichon-azul.herokuapp.com/PichonAzul/users/uid
    
    -Borrar usuario: https://pichon-azul.herokuapp.com/PichonAzul/users/uid 
    
  2. Mensajes
  
    -Obtener todos los mensajes: https://pichon-azul.herokuapp.com/PichonAzul/msg
    
    -Obtener mensaje por id: https://pichon-azul.herokuapp.com/PichonAzul/msg/mid 
    
    -Crear un nuevo mensaje: https://pichon-azul.herokuapp.com/PichonAzul/posts
    
    -Responder a un mensaje existente: https://pichon-azul.herokuapp.com/PichonAzul/reply
    
    -Compartir un mensaje: https://pichon-azul.herokuapp.com/PichonAzul/share
    
  3. Seguidores

    -Seguir un usuario en específico: https://pichon-azul.herokuapp.com/PichonAzul/follow/fid

    -Obtener todos los usuarios seguidos por un usuario: https://pichon-azul.herokuapp.com/PichonAzul/followedby/fid

    -Obtener todos los usuarios que siguen a un usuario: https://pichon-azul.herokuapp.com/PichonAzul/follows/fid

    -Parar de seguir un usuario específico : https://pichon-azul.herokuapp.com/PichonAzul/unfollow/fid

  4. Me gusta

    -Obtener todos los likes por mensaje: https://pichon-azul.herokuapp.com/PichonAzul/liked/mid 
    
    -Crear un like al mensaje: https://pichon-azul.herokuapp.com/PichonAzul/like/mid
    
    -Remover like del mensaje: https://pichon-azul.herokuapp.com/PichonAzul/like/remove/mid
    
  5. No me gusta

    -Obtener todos los dislikes por mensaje: https://pichon-azul.herokuapp.com/PichonAzul/disliked/mid 
    
    -Crear un dislike al mensaje: https://pichon-azul.herokuapp.com/PichonAzul/dislike/mid
    
    -Remover dislike del mensaje: https://pichon-azul.herokuapp.com/PichonAzul/dislike/remove/mid
    
  6. Bloqueos
  
    -El usuario registrado bloquea a un usuario:  https://pichon-azul.herokuapp.com/PichonAzul/block/uid
    
    -Obtener todos los usuarios blockeados por el id: https://pichon-azul.herokuapp.com/PichonAzul/blockedby/uid
    
    -Obtener todos los usuarios que blockean a un id en particular: https://pichon-azul.herokuapp.com/PichonAzul/blocking/uid
    
    -El usuario registrado desbloquea a un usuario: https://pichon-azul.herokuapp.com/PichonAzul/unblock/uid
   
  7. Credenciales de la Base de Datos
      
    {
     
    'host': 'ec2-34-233-0-64.compute-1.amazonaws.com',
    
    'user': 'qxnzmozhofunpq',
    
    'password': '2fcc078dcb79a138242190ef2becdf2241b919f495e0bff0561cba47112529dd',
    
    'dbname': 'd5mdc734arlvfo',
    
    'dbport': 5432
    
    }
   
