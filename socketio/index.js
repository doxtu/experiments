const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

const users = {};
const suffix = ['puppy','puff','weirdo','pug'];
const names = ['nick','kim','aloha','kimmy','nonpuppy','doxtu','yovo','ScumFuckFlowerGirl'];

app.get("/",(req,res)=>{
  res.sendFile(__dirname + '/index.html');
});

io.on('connection',(socket)=>{
  socket.on('disconnect',()=>{
	  // console.log('disconnect lmao');
  });
  
  socket.on('id',(id)=>{
    id = Number(id);
    if(typeof users[id] === "undefined"){
      users[id] = createUser(socket);
    }
    users[id].socket = socket; 
    io.emit('chat message', users[id].name + " has connected!");
  });
  
  socket.on('chat message',(msg)=>{
	  console.log('user sent:' + msg);
          msg = JSON.parse(msg);
	  io.emit('chat message',users[msg.id].name + ": " + msg.message);
  });
});

http.listen(8000,()=>{
  console.log('server running on port 8000');
});	

function createUser(sock){
  let name = names[getRandom(0,names.length)]+" "+ suffix[getRandom(0,suffix.length)];
 let user = {
    id: getRandom(0,10000),
	name: name,
	socket: sock
  };
  
  return user;
}

function getRandom(start,end){
  return Math.floor(Math.random()*end + start);
}
