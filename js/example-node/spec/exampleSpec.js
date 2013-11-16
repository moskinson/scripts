var class_module = require('../src/exampleNode');
var $ = require('jQuery');

describe("My calculator", function() {
  var my_class;

  beforeEach(function() {
    my_class = new class_module.exampleModule();
  });

  it("should be able to say this is mine", function() {
    
    expect( my_class.println('test example') ).toEqual("this is my test example");

  });


});