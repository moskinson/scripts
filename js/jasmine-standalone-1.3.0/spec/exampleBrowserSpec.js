
describe("My calculator", function() {
  var calculator = new Myclass();

  beforeEach(function() {

  });

  it("should be able to say this is mine", function() {
    
    expect( calculator.printlnMyPossesion('macmosca') ).toEqual('this is my macmosca');

  });


  describe("to test with a Spy", function() {

  	beforeEach(function() {
  		var obj = {}
  	});

  	it("should be able to check changeHTml have been called", function() {
	    
  		spyOn(calculator, 'changeHtmlValueForId').andCallThrough();

  		expect( calculator.changeHtml('my text')).toEqual('old html valuemy text');

	    expect( calculator.changeHtmlValueForId  ).toHaveBeenCalled();

	  });

  	});

  	describe("What to test with a mocking Stub", function() {

		beforeEach(function() {
		   spyOn(calculator, 'changeHtmlValueForId').andReturn('fixed');

		});

		it("should be able to append html value for a DOM Element and return value", function() {
			expect(calculator.changeHtml('my text') ).toEqual('fixed');
			expect( calculator.changeHtmlValueForId  ).toHaveBeenCalled();

		});

	});


});
