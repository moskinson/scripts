@Grapes(
	@Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.6')
)

import groovyx.net.http.HTTPBuilder
import groovyx.net.http.HttpResponseException
import static groovyx.net.http.Method.POST
import static groovyx.net.http.Method.GET
import static groovyx.net.http.Method.HEAD
import static groovyx.net.http.ContentType.JSON
import static groovyx.net.http.ContentType.TEXT



def validateUrlLinkContentResponse = { url ->
	try{ 
		
		def http = new HTTPBuilder(url)
		println "request to url $url"
		http.request( GET ) { req ->

			headers.'User-Agent' = 'Mozilla/5.0 Firefox/3.0.4'
			def timeout = 10000
			req.getParams().setParameter("http.socket.timeout", new Integer(timeout)) 
        	req.getParams().setParameter("http.connection.timeout", new Integer(timeout)) 


			response.success = { resp ->
				println "Success status code ${resp.status}"
				return true
			}

			response.failure = { resp -> 
				println "Failure status code ${resp.status}"
				return false 
			}
	 	}

	}catch(Exception e){
		println "Not valid link content"
		println e 
		return false
	}		
}

def url =  'http://www.google.com'

if (args) url = args[0]

validateUrlLinkContentResponse url
