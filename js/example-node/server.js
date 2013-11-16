var io = require('socket.io').listen(8889),
	feeds = require('./feeds')

io.sockets.on('connection', function (socket) {
	var feeds = setInterval(function () {
	      socket.emit('newFeeds', "Hola\n")
  		}, 2000)

	socket.on('disconnect', function () {
    	clearInterval(feeds);
  	})
})