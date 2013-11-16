var db = require('mongodb').Db;

exports.connect = function (callback) {
	db.connect("mongodb://"+user+":"+password+"@"+host+":27017/notifications", function(err, db) {
		if(err)
			return callback(err)

		console.log('Database connected')
		return callback(null, db)
	})
}