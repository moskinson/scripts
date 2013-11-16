var myMongo = require('./mongo-connection'),
    myDb;



exports.findById = function(req, res) {
    myMongo.connect(function(err, db) {
                            if (err) {
                                console.log('ERROR CONNECTING TO DATABASE');
                                console.log(err);
                                process.exit(1);
                            }
                            myDb = db
                        })

    console.log(req.params);
    console.log('findById: ' + req.params.id);
    myDb.collection('feeds', function(err, collection) {
        collection.findOne({'destination': req.params.id}, {limit:10},function(err, item) {
            console.log(item)
            res.jsonp(item);
        });
    });
}