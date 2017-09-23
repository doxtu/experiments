const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get("/",(req,res)=>{
  res.sendFile(__dirname + '/index.html');
});

io.on('connection',(socket)=>{
	console.log('user connected');
	socket.on('disconnect',()=>{
		console.log('disconnect lmao');
	});
	
	socket.on('chat message',(msg)=>{
		console.log('user sent:' + msg);
		io.emit('chat message',msg);
	});
});

http.listen(8000,()=>{
  console.log('server running on port 8000');
});	