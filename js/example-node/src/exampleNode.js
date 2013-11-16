var $ = require('jQuery');

var MyClass = function() {};

MyClass.prototype.println = function(value) {
  return "this is my "+value;
};

MyClass.prototype.changeHtml = function(value) {
  $('#domElementId').html(value);
};

MyClass.prototype.checkTwitterTimeLine = function(user_timeline){
	$.getJSON('http://twitter.com/status/'+user_timeline+'/treason.json?count=10&callback=?',function(data) {
	  return data.errors[0].message;
	});
}

exports.exampleModule = MyClass;