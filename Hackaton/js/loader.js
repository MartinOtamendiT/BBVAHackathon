window.addEventListener('load', function(){

    req = new XMLHttpRequest();
    req.open('GET', 'py/main.py', true);
    req.onload = function(){

    	brython();
    	src = __BRYTHON__.python_to_js(this.responseText);
    	eval(src);

    }

    req.send();

});