var Myclass = function() {};

Myclass.prototype.printlnMyPossesion = function(value) {
  return "this is my "+value;
};


Myclass.prototype.changeHtml = function(value) {
 //request AJAX
  return this.changeHtmlValueForId('#element_id',value)
};


Myclass.prototype.changeHtmlValueForId = function(element_id, new_html){
	$(element_id).append(new_html);

	return 'old html value' + new_html;
}