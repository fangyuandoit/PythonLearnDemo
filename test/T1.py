import js2py

jsCode = "function addOne(i){return i+1;}    function addTwo(i){return i+2}"
context = js2py.EvalJs()

context.execute(jsCode)
print(context.addOne(1))
print(context.addTwo(1))

