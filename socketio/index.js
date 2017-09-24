const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

const users = {};
const names = ['nick','kim','puppy','otherpuppy','nonpuppy','doxtu','yovo','sveox','ScumFuckFlowerGirl'];

app.get("/",(req,res)=>{
  res.sendFile(__dirname + '/index.html');
});

io.on('connection',(socket)=>{
  socket.on('disconnect',()=>{
	  // console.log('disconnect lmao');
  });
  
  socket.on('id',(id)=>{
    id = Number(id);
    let user = users[id];
    if(typeof user === "undefined"){
      user = createUser(socket);
    } 
    io.emit('chat message', user.name + " has connected!");
  });
  
  socket.on('chat message',(msg)=>{
	  // console.log('user sent:' + msg);
	  io.emit('chat message',msg);
  });
});

http.listen(8000,()=>{
  console.log('server running on port 8000');
});	

function createUser(sock){
  let user = {
    id: getRandom(0,10000),
	name: names[getRandom(0,names.length)],
	socket: sock
  };
  
  return user;
}

function getRandom(start,end){
  return Math.floor(Math.random()*end + start);
}
